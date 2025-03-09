# ==============================================================================
# @des: This file contains run functions for icepack data assimilation.
#       - contains different options of the EnKF data assimilation schemes.
# @date: 2024-11-4
# @author: Brian Kyanjo
# ==============================================================================

# --- python imports ---
import sys
import os
import tqdm
import numpy as np
from scipy.stats import multivariate_normal,norm

os.environ["OMP_NUM_THREADS"] = "1"

# firedrake imports
import firedrake
from firedrake import *
from firedrake.petsc import PETSc

# icepack imports
import icepack
import icepack.models.friction
from icepack.constants import (
    ice_density as rho_I,
    water_density as rho_W,
    gravity as g,
    weertman_sliding_law as m
)

# --- Utility imports ---
sys.path.insert(0, '../../../config')
from _utility_imports import icesee_get_index

# --- globally define the state variables ---
global vec_inputs 
vec_inputs = ['h','u','v','smb']

# --- model initialization ---
def initialize_model(physical_params, modeling_params, comm):
    """des: initialize the icepack model"""
    # get size and rank of the communicator
    size = comm.Get_size()
    rank = comm.Get_rank()

    # --- Geometry and Mesh ---
    PETSc.Sys.Print('Setting up mesh across %d processes' % size)
    Lx, Ly = int(float(physical_params["Lx"])), int(float(physical_params["Ly"]))
    nx, ny = int(float(physical_params["nx"])), int(float(physical_params["ny"]))
    PETSc.Sys.Print(f"Mesh dimensions: {Lx} x {Ly} with {nx} x {ny} elements")

    # --- make the comm object available to the mesh function
    mesh = firedrake.RectangleMesh(nx, ny, Lx, Ly, quadrilateral=True, comm=comm)

    # -- get the degree of the finite element space
    degree = int(float(physical_params["degree"]))
    Q = firedrake.FunctionSpace(mesh, "CG",degree)
    V = firedrake.VectorFunctionSpace(mesh, "CG", degree)
    x,y = firedrake.SpatialCoordinate(mesh)

    # --- Bedrock and Surface Elevations ---
    b_in, b_out = (float(physical_params["b_in"])), (float(physical_params["b_out"]))
    s_in, s_out = (float(physical_params["s_in"])), (float(physical_params["s_out"]))

    b = firedrake.interpolate(b_in - (b_in - b_out) * x / Lx, Q)
    s0 = firedrake.interpolate(s_in - (s_in - s_out) * x / Lx, Q)
    h0 = firedrake.interpolate(s0 - b, Q)

    # --- Driving Stress ---
    h_in = s_in - b_in
    ds_dx = (s_out - s_in) / Lx
    tau_D = -rho_I * g * h_in * ds_dx
    PETSc.Sys.Print(f"Driving stress = {1000*tau_D} kPa")

    # --- Initial Velocity ---
    u_in, u_out = float(physical_params["u_in"]), float(physical_params["u_out"])
    velocity_x = u_in + (u_out - u_in) * (x / Lx) ** 2
    u0 = firedrake.interpolate(firedrake.as_vector((velocity_x, 0)), V)

    # --- Friction Coefficient ---
    PETSc.Sys.Print("Importing icepack ...")
    T = firedrake.Constant(float(modeling_params["T"]))
    A = icepack.rate_factor(T)

    expr = (0.95 - 0.05 * x / Lx) * tau_D / u_in**(1 / m)
    C = firedrake.interpolate(expr, Q)

    p_W = rho_W * g * firedrake.max_value(0, h0 - s0)
    p_I = rho_I * g * h0
    phi = 1 - p_W / p_I

    # --- Friction Law ---
    def weertman_friction_with_ramp(**kwargs):
        u = kwargs["velocity"]
        h = kwargs["thickness"]
        s = kwargs["surface"]
        C = kwargs["friction"]

        p_W = rho_W * g * firedrake.max_value(0, h - s)
        p_I = rho_I * g * h
        phi = 1 - p_W / p_I
        return icepack.models.friction.bed_friction(
            velocity=u,
            friction=C * phi,
        )
    
    # --- Ice Stream Model ---
    model_weertman = icepack.models.IceStream(friction=weertman_friction_with_ramp)

    opts = {"dirichlet_ids": [1], "side_wall_ids": [3, 4]}
    solver_weertman = icepack.solvers.FlowSolver(model_weertman, **opts)

    u0 = solver_weertman.diagnostic_solve(
        velocity=u0,
        thickness=h0,
        surface=s0,
        fluidity=A,
        friction=C,
    )

    expr = -1e3 * C * phi * sqrt(inner(u0, u0)) ** (1 / m - 1) * u0
    tau_b = firedrake.interpolate(expr, V)

    # --- Accumulation ---
    a_in = firedrake.Constant(float(modeling_params["a_in"]))
    da   = firedrake.Constant(float(modeling_params["da"]))
    a    = firedrake.interpolate(a_in + da * x / Lx, Q)

    # nurged accumulation
    a_in_p  = firedrake.Constant(float(modeling_params["a_in_p"]))
    da_p    = firedrake.Constant(float(modeling_params["da_p"]))
    a_p     = firedrake.interpolate(a_in_p + da_p * x / Lx, Q)

    # --- Update h and u ---
    h = h0.copy(deepcopy=True)
    u = u0.copy(deepcopy=True)

    # print size h
    # print(f"Size of the function space: {h.dat.data.size} on rank {rank}")

    return nx,ny,Lx,Ly,x,y,h,u,a,a_p,b,b_in,b_out,h0,u0,solver_weertman,A,C,Q,V,

# --- icepack model ---
def Icepack(solver, h, u, a, b, dt, h0, **kwargs):
    """inputs: solver - icepack solver
                h - ice thickness
                u - ice velocity
                a - ice accumulation
                b - ice bed
                dt - time step
                h0 - ice thickness inflow
                *args - additional arguments for the model
        outputs: h - updated ice thickness
                 u - updated ice velocity
    """
    h = solver.prognostic_solve(
        dt = dt,
        thickness = h,
        velocity = u,
        accumulation = a,
        thickness_inflow = h0,
    )

    s = icepack.compute_surface(thickness = h, bed = b)

    u = solver.diagnostic_solve(
        velocity = u,
        thickness = h,
        surface = s,
        **kwargs
    )

    return h, u

# --- Run model for the icepack model ---
def run_model(ens, ensemble, nd, **kwargs):
    """des: icepack model function
        inputs: ensemble - current state of the model
                **kwargs - additional arguments for the model
        outputs: model run
    """

    # unpack the **kwargs
    # a = kwargs.get('a', None)
    b  = kwargs.get('b', None)
    dt = kwargs.get('dt', None)
    h0 = kwargs.get('h0', None)
    A  = kwargs.get('A', None)
    C  = kwargs.get('C', None)
    Q  = kwargs.get('Q', None)
    V  = kwargs.get('V', None)
    params = kwargs.get('params', None)
    solver = kwargs.get('solver', None)

    # --- define the state variables list ---
    global vec_inputs 

    # call the icesee_get_index function to get the indices of the state variables
    vecs, indx_map = icesee_get_index(ensemble, vec_inputs, **kwargs)
   
    ndim = nd // (params["num_state_vars"] + params["num_param_vars"])
    state_block_size = ndim*params["num_state_vars"]
    
    # unpack h,u,v from the ensemble member
    h_vec = ensemble[indx_map["h"],ens]
    u_vec = ensemble[indx_map["u"],ens]
    v_vec = ensemble[indx_map["v"],ens]

    # joint estimation
    if kwargs["joint_estimation"]:
        # Use analysis step to update the accumulation rate
        # - pack accumulation rate with the state variables to
        #   get ensemble = [h,u,v,a]
        a_vec = ensemble[indx_map["smb"],ens]

        a = Function(Q)
        # print(f"a size: {a.dat.data.size} avec {a_vec.shape} ensemble shape: {ensemble.shape}")
        a.dat.data[:] = a_vec.copy()
    else:
        # don't update the accumulation rate (updates smb)
        a = kwargs.get('a', None)

    # create firedrake functions from the ensemble members
    h = Function(Q)
    h.dat.data[:] = h_vec.copy()

    u = Function(V)
    u.dat.data[:,0] = u_vec.copy()
    u.dat.data[:,1] = v_vec.copy()

    # call the ice stream model to update the state variables
    h, u = Icepack(solver, h, u, a, b, dt, h0, fluidity = A, friction = C)

    # update the ensemble members with the new state variables and noise 
    ensemble[indx_map["h"],ens] = h.dat.data_ro
    ensemble[indx_map["u"],ens] = u.dat.data_ro[:,0]
    ensemble[indx_map["v"],ens] = u.dat.data_ro[:,1]

    return ensemble[:,ens]



