# =============================================================================
# @author: Brian Kyanjo
# @date: 2025-01-13
# @description: ICESEE model applications utility imports
# =============================================================================

# --- Imports ---
import os
import sys
import h5py
import numpy as np
import warnings
from scipy.stats import norm, multivariate_normal
from tqdm import tqdm
import yaml
import argparse
from argparse import ArgumentParser

# Suppress warnings
warnings.filterwarnings("ignore")

def get_project_root():
    """Automatically determines the root of the project."""
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get absolute path of the current script
    
    # Traverse upwards until we reach the root of the project (assuming 'src' folder exists at root)
    while not os.path.exists(os.path.join(current_dir, 'src')):
        current_dir = os.path.dirname(current_dir)  # Move one level up
    
    return current_dir

# Get the root of the project
project_root = get_project_root()

# Construct the path to 'src/models' from the project root
models_dir = os.path.join(project_root, 'src', 'models')
utils_dir = os.path.join(project_root, 'src', 'utils')
run_model_da_dir = os.path.join(project_root, 'src', 'run_model_da')
config_loader_dir = os.path.join(project_root, 'config')
applications_dir = os.path.join(project_root, 'applications')
parallelization_dir = os.path.join(project_root, 'src', 'parallelization')

# Insert the models directory at the beginning of sys.path
sys.path.insert(0, models_dir)
sys.path.insert(0, utils_dir)
sys.path.insert(0, run_model_da_dir)
sys.path.insert(0, config_loader_dir)
sys.path.insert(0, parallelization_dir)

# import the necessary modules
from tools import save_arrays_to_h5, extract_datasets_from_h5, save_all_data
from tools import icesee_get_index
from utils import UtilsFunctions
from config_loader import load_yaml_to_dict, get_section

# Check if running in Jupyter notebook (for visualization)
flag_jupyter = False
if 'ipykernel' in sys.modules:
    print("Running in Jupyter - disabling command line arguments")
    # leave entire routine
    flag_jupyter = True

# =============================================================================
# --- Command Line Arguments ---
if not flag_jupyter:
    # Mapping for execution mode
    execution_modes_str = {
        "default_run": 0,
        "sequential_run": 1,
        "even_distribution": 2
    }
    execution_modes_int = {v: k for k, v in execution_modes_str.items()}  # Reverse mapping

    # CL args.
    parser = ArgumentParser(description='ICESEE: Ice Sheet Parameter and State Estimation model')
    parser.add_argument('--Nens', type=int, required=False, default=2, help='ensemble members')
    parser.add_argument('--verbose', action='store_true', help='verbose output')
    parser.add_argument('--default_run', action='store_true', help='default run')
    parser.add_argument('--sequential_run', action='store_true', help='sequential run')
    parser.add_argument('--even_distribution', action='store_true', help='even distribution')
    parser.add_argument('execution_mode', type=int, choices=[0, 1, 2], nargs='?', help='Execution mode: 0=default_run, 1=sequential_run, 2=even_distribution')

    args = parser.parse_args()

    # check if default run arugment is provided
    run_flag = False
    if (args.default_run or args.sequential_run or args.even_distribution):
        run_flag = True

    # Determine execution mode
    selected_mode = "default_run"  # Default mode

    if args.execution_mode is not None:
        selected_mode = execution_modes_int[args.execution_mode]  # Convert int to string
    else:
        for mode in execution_modes_str.keys():
            if getattr(args, mode):
                selected_mode = mode
                break

    # Set flags explicitly
    args.default_run = (selected_mode == "default_run")
    args.sequential_run = (selected_mode == "sequential_run")
    args.even_distribution = (selected_mode == "even_distribution")

    # Explicit use of parameters
    Nens = int(args.Nens)

    # Create params dictionary
    params = {
        "Nens": int(args.Nens),
        "default_run": args.default_run,
        "sequential_run": args.sequential_run,
        "even_distribution": args.even_distribution,
    }

    # print(f"Execution mode selected: {selected_mode}")
    # print(f"Params: {params}")

    # Load parameters from a YAML file
    parameters_file = "params.yaml"
    parameters = load_yaml_to_dict(parameters_file)

    physical_params = get_section(parameters, "physical-parameters")
    modeling_params = get_section(parameters, "modeling-parameters")
    enkf_params = get_section(parameters, "enkf-parameters")

    # --- Ensemble Parameters ---
    params.update({
        "nt": int(float(modeling_params["num_years"])) * int(float(modeling_params["timesteps_per_year"])),
        "dt": 1.0 / float(modeling_params["timesteps_per_year"]),
        "num_state_vars": int(float(enkf_params.get("num_state_vars", 1))),
        "num_param_vars": int(float(enkf_params.get("num_param_vars", 0))),
        "number_obs_instants": int(int(float(enkf_params.get("obs_max_time", 1))) / float(enkf_params.get("freq_obs", 1))),
        "inflation_factor": float(enkf_params.get("inflation_factor", 1.0)),
        "sig_model": float(enkf_params.get("sig_model", 0.01)),
        "sig_obs": float(enkf_params.get("sig_obs", 0.01)),
        "sig_Q": float(enkf_params.get("sig_Q", 0.01)),
        "freq_obs": float(enkf_params.get("freq_obs", 1)),
        "obs_max_time": int(float(enkf_params.get("obs_max_time", 1))),
        "obs_start_time": float(enkf_params.get("obs_start_time", 1)),
        "localization_flag": bool(enkf_params.get("localization_flag", False)),
        "parallel_flag": enkf_params.get("parallel_flag", "serial"),
        "n_modeltasks": int(enkf_params.get("n_modeltasks", 1)),
        "execution_flag": int(enkf_params.get("execution_flag", 0)),
    })

    # --- incase CL args not provided ---
    if Nens == 2:
        params["Nens"] = int(float(enkf_params.get("Nens", 2)))
    
    if run_flag:
        execution_flag = params.get("execution_flag")

        if execution_flag == 1:
            params.update({"sequential_run": True, "default_run": False})
        elif execution_flag == 2:
            params.update({"even_distribution": True, "default_run": False})
        else:
            params["default_run"] = True

    
    # update for time t
    params["t"] = np.linspace(0, int(float(modeling_params["num_years"])), params["nt"] + 1)
    params["total_state_param_vars"] = params["num_state_vars"] + params["num_param_vars"]

    # model kwargs
    kwargs = {
        "t": params["t"],
        "obs_index": (np.linspace(int(params["freq_obs"]/params["dt"]), \
                            int(params["obs_max_time"]/params["dt"]), int(params["number_obs_instants"]))).astype(int),
        "joint_estimation": bool(enkf_params.get("joint_estimation", False)),
        "parameter_estimation": bool(enkf_params.get("parameter_estimation", False)),
        "state_estimation": bool(enkf_params.get("state_estimation", False)),
    }

    # --- Observations Parameters ---
    obs_t, obs_idx, num_observations = UtilsFunctions(params).generate_observation_schedule(**kwargs)
    # print(obs_t)
    kwargs["obs_index"] = obs_idx
    params["number_obs_instants"] = num_observations
    kwargs["parallel_flag"]       = enkf_params.get("parallel_flag", "serial")
    kwargs["commandlinerun"]      = enkf_params.get("commandlinerun", False)