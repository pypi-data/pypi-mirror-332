# ==============================================================================
# @des: This file contains run functions for icepack data assimilation.
#       - contains different options of the EnKF data assimilation schemes.
# @date: 2024-11-4
# @author: Brian Kyanjo
# ==============================================================================

import sys
import os
import numpy as np
import re
from scipy.stats import multivariate_normal,norm

# --- import run_simulation function from the available examples ---
from synthetic_ice_stream._icepack_model import *
from scipy import linalg

# --- Utility imports ---
sys.path.insert(0, '../../config')
from _utility_imports import icesee_get_index

# --- globally define the state variables ---
global vec_inputs 
vec_inputs = ['h','u','v','smb']

# --- Forecast step ---
def forecast_step_single(ens=None, ensemble=None, nd=None, **kwargs):
    """ensemble: packs the state variables:h,u,v of a single ensemble member
                 where h is thickness, u and v are the x and y components 
                 of the velocity field
    Returns: ensemble: updated ensemble member
    """
    #  call the run_model fun to push the state forward in time
    ensemble[:,ens] = run_model(ens, ensemble, nd, **kwargs)

    return ensemble[:,ens]

# --- Background step ---
def background_step(k=None, **kwargs):
    """ computes the background state of the model
    Args:
        k: time step index
        statevec_bg: background state of the model
        hdim: dimension of the state variables
    Returns:
        statevec_bg: updated background state of the model
    """
    # unpack the **kwargs
    # a = kwargs.get('a', None)
    b = kwargs.get('b', None)
    dt = kwargs.get('dt', None)
    h0 = kwargs.get('h0', None)
    A = kwargs.get('A', None)
    C = kwargs.get('C', None)
    Q = kwargs.get('Q', None)
    V = kwargs.get('V', None)
    solver = kwargs.get('solver', None)
    statevec_bg = kwargs["statevec_bg"]

    hb = Function(Q)
    ub = Function(V)

     # --- define the state variables list ---
    global vec_inputs 

    # call the icesee_get_index function to get the indices of the state variables
    vecs, indx_map = icesee_get_index(statevec_bg, vec_inputs, **kwargs)

    # fetch the state variables
    hb.dat.data[:]   = statevec_bg[indx_map["h"],k]
    ub.dat.data[:,0] = statevec_bg[indx_map["u"],k]
    ub.dat.data[:,1] = statevec_bg[indx_map["v"],k]

    # call the ice stream model to update the state variables
    hb, ub = Icepack(solver, hb, ub, a, b, dt, h0, fluidity = A, friction = C)

    # update the background state at the next time step
    statevec_bg[indx_map["h"],k+1] = hb.dat.data_ro
    statevec_bg[indx_map["u"],k+1] = ub.dat.data_ro[:,0]
    statevec_bg[indx_map["v"],k+1] = ub.dat.data_ro[:,1]

    if kwargs["joint_estimation"]:
        a = kwargs.get('a', None)
        statevec_bg[indx_map["smb"],0] = a.dat.data_ro
        statevec_bg[indx_map["smb"],k+1] = a.dat.data_ro

    return statevec_bg

# --- generate true state ---
def generate_true_state(**kwargs):
    """generate the true state of the model"""

    # unpack the **kwargs
    a  = kwargs.get('a', None)
    b  = kwargs.get('b', None)
    dt = kwargs.get('dt', None)
    A  = kwargs.get('A', None)
    C  = kwargs.get('C', None)
    Q  = kwargs.get('Q', None)
    V  = kwargs.get('V', None)
    h0 = kwargs.get('h0', None)
    u0 = kwargs.get('u0', None)
    solver = kwargs.get('solver', None)
    statevec_true = kwargs["statevec_true"]

    params = kwargs["params"]
    nt = params["nt"] - 1
    
    # --- define the state variables list ---
    global vec_inputs 

    # call the icesee_get_index function to get the indices of the state variables
    vecs, indx_map = icesee_get_index(statevec_true, vec_inputs, **kwargs)
    
    # --- fetch the state variables ---
    statevec_true[indx_map["h"],0] = h0.dat.data_ro
    statevec_true[indx_map["u"],0] = u0.dat.data_ro[:,0]
    statevec_true[indx_map["v"],0] = u0.dat.data_ro[:,1]

    # intialize the accumulation rate if joint estimation is enabled at the initial time step
    if kwargs["joint_estimation"]:
        statevec_true[indx_map["smb"],0] = a.dat.data_ro

    h = h0.copy(deepcopy=True)
    u = u0.copy(deepcopy=True)
    for k in range(nt):
        # call the ice stream model to update the state variables
        h, u = Icepack(solver, h, u, a, b, dt, h0, fluidity = A, friction = C)

        statevec_true[indx_map["h"],k+1] = h.dat.data_ro
        statevec_true[indx_map["u"],k+1] = u.dat.data_ro[:,0]
        statevec_true[indx_map["v"],k+1] = u.dat.data_ro[:,1]

        # update the accumulation rate if joint estimation is enabled
        if kwargs["joint_estimation"]:
            statevec_true[indx_map["smb"],k+1] = a.dat.data_ro

    return statevec_true

def generate_nurged_state(**kwargs):
    """generate the nurged state of the model"""
    
    params = kwargs["params"]
    nt = params["nt"] - 1

    # unpack the **kwargs
    a = kwargs.get('a_p', None)
    t = kwargs.get('t', None)
    x = kwargs.get('x', None)
    Lx = kwargs.get('Lx', None)
    b = kwargs.get('b', None)
    dt = kwargs.get('dt', None)
    A = kwargs.get('A', None)
    C = kwargs.get('C', None)
    Q = kwargs.get('Q', None)
    V = kwargs.get('V', None)
    h0 = kwargs.get('h0', None)
    u0 = kwargs.get('u0', None)
    solver = kwargs.get('solver', None)
    a_in_p = kwargs.get('a_in_p', None)
    da_p = kwargs.get('da_p', None)
    da = kwargs.get('da', None)
    h_nurge_ic      = kwargs.get('h_nurge_ic', None)
    u_nurge_ic      = kwargs.get('u_nurge_ic', None)
    nurged_entries  = kwargs.get('nurged_entries', None)

    statevec_nurged = kwargs["statevec_nurged"]

     # --- define the state variables list ---
    global vec_inputs 

    # call the icesee_get_index function to get the indices of the state variables
    vecs, indx_map = icesee_get_index(statevec_nurged, vec_inputs, **kwargs)

    #  create a bump -100 to 0
    # h_indx = int(np.ceil(nurged_entries+1))
    hdim = vecs['h'].shape[0]
    if 0.5*hdim > int(np.ceil(nurged_entries+1)):
        h_indx = int(np.ceil(nurged_entries+1))
    else:
        # 5% of the hdim so that the bump is not too large
        h_indx = int(np.ceil(hdim*0.05))
   
    # u_indx = int(np.ceil(u_nurge_ic+1))
    u_indx = 1
    h_bump = np.linspace(-h_nurge_ic,0,h_indx)
    u_bump = np.linspace(-u_nurge_ic,0,h_indx)
    # h_bump = np.random.uniform(-h_nurge_ic,0,h_indx)
    # u_bump = np.random.uniform(-u_nurge_ic,0,h_indx)
    # print(f"hdim: {hdim}, h_indx: {h_indx}")
    # print(f"[Debug]: h_bump shape: {h_bump.shape} h0_index: {h0.dat.data_ro[:h_indx].shape}")
    h_with_bump = h_bump + h0.dat.data_ro[:h_indx]
    u_with_bump = u_bump + u0.dat.data_ro[:h_indx,0]
    v_with_bump = u_bump + u0.dat.data_ro[:h_indx,1]

    h_perturbed = np.concatenate((h_with_bump, h0.dat.data_ro[h_indx:]))
    u_perturbed = np.concatenate((u_with_bump, u0.dat.data_ro[h_indx:,0]))
    v_perturbed = np.concatenate((v_with_bump, u0.dat.data_ro[h_indx:,1]))

    # if velocity is nurged, then run to get a solution to be used as am initial guess for velocity.
    if u_nurge_ic != 0.0:
        h = Function(Q)
        u = Function(V)
        h.dat.data[:]   = h_perturbed
        u.dat.data[:,0] = u_perturbed
        u.dat.data[:,1] = v_perturbed
        h0 = h.copy(deepcopy=True)
        # call the solver
        h, u = Icepack(solver, h, u, a, b, dt, h0, fluidity = A, friction = C)

        # update the nurged state with the solution
        h_perturbed = h.dat.data_ro
        u_perturbed = u.dat.data_ro[:,0]
        v_perturbed = u.dat.data_ro[:,1]

    statevec_nurged[indx_map["h"],0]          = h_perturbed
    statevec_nurged[indx_map["u"],0]          = u_perturbed
    statevec_nurged[indx_map["v"],0]          = v_perturbed

    h = Function(Q)
    u = Function(V)
    h.dat.data[:] = h_perturbed
    u.dat.data[:,0] = u_perturbed
    u.dat.data[:,1] = v_perturbed
    h0 = h.copy(deepcopy=True)

    tnur = np.linspace(.1, 2, nt)
    # intialize the accumulation rate if joint estimation is enabled at the initial time step
    if kwargs["joint_estimation"]:
        # aa   = a_in_p*(np.sin(tnur[0]) + 1)
        # daa  = da_p*(np.sin(tnur[0]) + 1)
        aa = a_in_p
        daa = da_p
        a_in = firedrake.Constant(aa)
        da_  = firedrake.Constant(daa)
        a    = firedrake.interpolate(a_in + da_ * x / Lx, Q)
        statevec_nurged[indx_map["smb"],0] = a.dat.data_ro

    for k in range(nt):
        # aa   = a_in_p*(np.sin(tnur[k]) + 1)
        # daa  = da_p*(np.sin(tnur[k]) + 1)
        aa = a_in_p
        daa = da_p
        a_in = firedrake.Constant(aa)
        da_  = firedrake.Constant(daa)
        a    = firedrake.interpolate(a_in + da_ * x / Lx, Q)
        # call the ice stream model to update the state variables
        h, u = Icepack(solver, h, u, a, b, dt, h0, fluidity = A, friction = C)

        statevec_nurged[indx_map["h"],k+1] = h.dat.data_ro
        statevec_nurged[indx_map["u"],k+1] = u.dat.data_ro[:,0]
        statevec_nurged[indx_map["v"],k+1] = u.dat.data_ro[:,1]

        if kwargs["joint_estimation"]:
            statevec_nurged[indx_map["smb"],k+1] = a.dat.data_ro

    return statevec_nurged


# --- initialize the ensemble members ---
def initialize_ensemble(**kwargs):
    
    """initialize the ensemble members"""

    # unpack the **kwargs
    h0 = kwargs.get('h0', None)
    u0 = kwargs.get('u0', None)
    params = kwargs["params"]
    # a  = kwargs.get('a', None)
    b  = kwargs.get('b', None)
    dt = kwargs.get('dt', None)
    A  = kwargs.get('A', None)
    C  = kwargs.get('C', None)
    Q  = kwargs.get('Q', None)
    V  = kwargs.get('V', None)
    solver = kwargs.get('solver', None)
    h_nurge_ic      = kwargs.get('h_nurge_ic', None)
    u_nurge_ic      = kwargs.get('u_nurge_ic', None)
    nurged_entries  = kwargs.get('nurged_entries', None)
    statevec_ens    = kwargs["statevec_ens"]
    statevec_bg     = kwargs["statevec_bg"]
    statevec_ens_mean = kwargs["statevec_ens_mean"]
    statevec_ens_full = kwargs["statevec_ens_full"]

    # extract the ensemble size
    N = params["Nens"]

     # --- define the state variables list ---
    global vec_inputs 

    # call the icesee_get_index function to get the indices of the state variables
    vecs, indx_map = icesee_get_index(statevec_ens, vec_inputs, **kwargs)

    # call the nurged state to initialize the ensemble
    statevec_nurged = generate_nurged_state(**kwargs)
                                           
    # fetch h u, and v from the nurged state
    h_perturbed = statevec_nurged[indx_map["h"],0]
    u_perturbed = statevec_nurged[indx_map["u"],0]
    v_perturbed = statevec_nurged[indx_map["v"],0]

    # initialize the ensemble members
    # h_indx = int(np.ceil(nurged_entries+1))
    # h_indx = int(np.ceil(nurged_entries+1))
    hdim = vecs['h'].shape[0]
    if 0.5*hdim > int(np.ceil(nurged_entries+1)):
        h_indx = int(np.ceil(nurged_entries+1))
    else:
        # 5% of the hdim so that the bump is not too large
        h_indx = int(np.ceil(hdim*0.05))

    for i in range(N):
        # intial thickness perturbed by bump
        # h_bump = np.random.uniform(-h_nurge_ic,0,h_indx)
        # h_bump = np.random.normal(-h_nurge_ic,0.1,h_indx)
        h_bump = np.linspace(-h_nurge_ic,0,h_indx)
        # h_with_bump = h_bump + h_perturbed[:h_indx]
        # h_perturbed = np.concatenate((h_with_bump, h_perturbed[h_indx:]))
        h_with_bump = h_bump + h0.dat.data_ro[:h_indx]
        h_perturbed = np.concatenate((h_with_bump, h0.dat.data_ro[h_indx:]))
        statevec_ens[:hdim,i] = h_perturbed 

        # intial velocity unperturbed
        # statevec_ens[hdim:2*hdim,i] = u_perturbed
        # statevec_ens[2*hdim:3*hdim,i]     = v_perturbed
        statevec_ens[indx_map["u"],i] = u0.dat.data_ro[:,0]
        statevec_ens[indx_map["v"],i] = u0.dat.data_ro[:,1]
        

        # add some kind of perturbations  with mean 0 and variance 1
        noise = np.random.normal(0, 0.1, hdim)
        # noise = multivariate_normal.rvs(np.zeros(hdim), np.eye(hdim)*0.01)

        statevec_ens[indx_map["h"],i] = statevec_ens[indx_map["h"],i] + noise
        statevec_ens[indx_map["u"],i] = statevec_ens[indx_map["u"],i] + noise
        statevec_ens[indx_map["v"],i] = statevec_ens[indx_map["v"],i] + noise
        
        # use the pseudo random field to perturb the state variables
        # field = generate_random_field(kernel='gaussian',**kwargs)


        # initilize the accumulation rate if joint estimation is enabled
        if kwargs["joint_estimation"]:
            # add some spread to the intial accumulation rate
            initial_smb = statevec_nurged[indx_map["smb"],0]

            # create a normal distribution spread for the accumulation rate
            spread = np.random.normal(0, 0.01, initial_smb.shape)
            # print(f"[Debug]: spread and initail_smb shapes: {spread.shape}, {initial_smb.shape}")
            statevec_ens[indx_map["smb"],i] = initial_smb + spread

            # statevec_ens[3*hdim:,i] = statevec_nurged[3*hdim:,0]

    statevec_ens_full[:,:,0] = statevec_ens
    noise = np.random.normal(0, 0.1, hdim)
    # noise = multivariate_normal.rvs(np.zeros(hdim), np.eye(hdim)*0.01)
    # initialize the background state
    statevec_bg[indx_map["h"],0] = h_perturbed + noise
    statevec_bg[indx_map["u"],0] = u_perturbed + noise
    statevec_bg[indx_map["v"],0] = v_perturbed + noise

    # initialize the ensemble mean
    statevec_ens_mean[indx_map["h"],0] = h_perturbed + noise
    statevec_ens_mean[indx_map["u"],0] = u_perturbed + noise
    statevec_ens_mean[indx_map["v"],0] = v_perturbed + noise

    # intialize the joint estimation variables
    if kwargs["joint_estimation"]:
        # a = kwargs.get('a', None)
        statevec_bg[indx_map["smb"],0] = statevec_nurged[indx_map["smb"],0]
        statevec_ens_mean[indx_map["smb"],0] = statevec_nurged[indx_map["smb"],0]

    return statevec_bg, statevec_ens, statevec_ens_mean, statevec_ens_full


def generate_random_field(kernel='gaussian',**kwargs):
    """
    Generate a 2D pseudorandom field with mean 0 and variance 1.
    
    Parameters:
    - size: tuple of (height, width) for the field dimensions
    - length_scale: float, controls smoothness (larger = smoother)
    - num_points: int, number of grid points per dimension
    - kernel: str, type of covariance kernel ('gaussian' or 'exponential')
    
    Returns:
    - field: 2D numpy array with the random field
    """

    Lx, Ly = kwargs["Lx"], kwargs["Ly"]
    nx, ny = kwargs["nx"], kwargs["ny"]

    length_scale = 0.2*max(Lx,Ly)
    
    # Create grid
    x = np.linspace(0, Lx, nx+1)
    y = np.linspace(0, Ly, ny+1)
    X, Y = np.meshgrid(x, y)
    
    # Compute distances between all points
    coords = np.stack([X.flatten(), Y.flatten()], axis=1)
    dist = np.sqrt(((coords[:, None, :] - coords[None, :, :]) ** 2).sum(axis=2))
    
    # Define covariance kernel
    if kernel == 'gaussian':
        cov = np.exp(-dist**2 / (2 * length_scale**2))
    elif kernel == 'exponential':
        cov = np.exp(-dist / length_scale)
    else:
        raise ValueError("Kernel must be 'gaussian' or 'exponential'")
    
    # Ensure positive definiteness and symmetry
    cov = (cov + cov.T) / 2  # Make perfectly symmetric
    cov += np.eye(cov.shape[0]) * 1e-6  # Add small jitter for stability
    
    # Generate random field using Cholesky decomposition
    L = linalg.cholesky(cov, lower=True)
    # z = np.random.normal(0, 1, size=num_points * num_points)
    z = np.random.normal(0, 1, size=(nx+1)*(ny+1))
    field_flat = L @ z
    
    # Reshape and normalize to mean 0, variance 1
    # field = field_flat.reshape(num_points, num_points)
    field = field_flat.reshape(nx+1, ny+1)
    field = (field - np.mean(field)) / np.std(field)
    
    return field
