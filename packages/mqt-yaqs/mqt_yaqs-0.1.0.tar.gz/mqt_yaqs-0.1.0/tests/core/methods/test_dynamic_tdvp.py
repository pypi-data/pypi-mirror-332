# Copyright (c) 2025 Chair for Design Automation, TUM
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

"""Tests for the Dissipation module in YAQS.

This module provides tests for verifying the correctness of dissipation processes
applied to Matrix Product States (MPS) via the `apply_dissipation` method.

The tests ensure:
- Dissipation correctly modifies the canonical form of MPS, specifically shifting
the orthogonality center as expected.
- Correct behavior when applying simple noise models (e.g., relaxation processes)
with given strengths and small time steps.

These tests validate the functionality and correctness of dissipation handling
in quantum simulations performed using the YAQS framework.
"""

# ignore non-lowercase variable names for physics notation
# ruff: noqa: N806

from __future__ import annotations

from unittest.mock import patch

from mqt.yaqs.core.data_structures.networks import MPO, MPS
from mqt.yaqs.core.data_structures.simulation_parameters import Observable, PhysicsSimParams
from mqt.yaqs.core.methods.dynamic_tdvp import dynamic_tdvp


def test_dynamic_tdvp_one_site() -> None:
    """Test dynamic TDVP, single site.

    Test that dynamic_TDVP calls single_site_TDVP exactly once when the current maximum bond dimension
    exceeds sim_params.max_bond_dim.

    In this test, sim_params.max_bond_dim is set to 0 so that the current maximum bond dimension of the MPS,
    computed by state.write_max_bond_dim(), is greater than 0. Therefore, the else branch of dynamic_TDVP should be
    taken, and single_site_tdvp should be called exactly once.
    """
    # Define the system Hamiltonian.
    L = 5
    J = 1
    g = 0.5
    H = MPO()
    H.init_ising(L, J, g)

    # Define the initial state.
    state = MPS(L, state="zeros")

    # Define simulation parameters with max_bond_dim set to 0.
    elapsed_time = 0.2
    dt = 0.1
    sample_timesteps = False
    num_traj = 1
    max_bond_dim = 0  # Force condition for single_site_TDVP.
    threshold = 1e-6
    order = 1
    measurements = [Observable("x", site) for site in range(L)]
    sim_params = PhysicsSimParams(
        measurements, elapsed_time, dt, num_traj, max_bond_dim, threshold, order, sample_timesteps=sample_timesteps
    )

    with patch("mqt.yaqs.core.methods.dynamic_tdvp.single_site_tdvp") as mock_single_site:
        dynamic_tdvp(state, H, sim_params)
        mock_single_site.assert_called_once_with(state, H, sim_params)


def test_dynamic_tdvp_two_site() -> None:
    """Test dynamic TDVP, two site.

    Test that dynamic_TDVP calls two_site_TDVP exactly once when the current maximum bond dimension
    is less than or equal to sim_params.max_bond_dim.

    In this test, sim_params.max_bond_dim is set to 2, so if the current maximum bond dimension is ≤ 2,
    the if branch of dynamic_TDVP is executed and two_site_TDVP is called exactly once.
    """
    # Define the system Hamiltonian.
    L = 5
    J = 1
    g = 0.5
    H = MPO()
    H.init_ising(L, J, g)

    # Define the initial state.
    state = MPS(L, state="zeros")

    # Define simulation parameters with max_bond_dim set to 2.
    elapsed_time = 0.2
    dt = 0.1
    sample_timesteps = False
    num_traj = 1
    max_bond_dim = 2  # Force condition for two_site_tdvp.
    threshold = 1e-6
    order = 1
    measurements = [Observable("x", site) for site in range(L)]
    sim_params = PhysicsSimParams(
        measurements, elapsed_time, dt, num_traj, max_bond_dim, threshold, order, sample_timesteps=sample_timesteps
    )

    with patch("mqt.yaqs.core.methods.dynamic_tdvp.two_site_tdvp") as mock_two_site:
        dynamic_tdvp(state, H, sim_params)
        mock_two_site.assert_called_once_with(state, H, sim_params)
