# Copyright (c) 2025 Chair for Design Automation, TUM
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

"""Library of quantum gates.

This module defines a collection of quantum gate classes used in quantum simulations.
Each gate is implemented as a class derived from BaseGate and includes its matrix representation,
tensor form, interactions, and generator(s). The module provides concrete implementations
for standard gates. The GateLibrary class aggregates all these gate classes for easy access.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from ..data_structures.networks import MPO
from .observables_library import ObservablesLibrary

if TYPE_CHECKING:
    from numpy.typing import NDArray
    from qiskit.circuit import Parameter


def split_tensor(tensor: NDArray[np.complex128]) -> list[NDArray[np.complex128]]:
    """Splits a two-qubit tensor into two tensors using Singular Value Decomposition (SVD).

    Args:
        tensor (NDArray[np.complex128]): A 4-dimensional tensor with shape (2, 2, 2, 2).

    Returns:
        list[NDArray[np.complex128]]: A list containing two tensors resulting from the split.
            - The first tensor has shape (2, 2, bond_dimension, 1).
            - The second tensor has shape (2, 2, bond_dimension, 1).
    """
    assert tensor.shape == (2, 2, 2, 2)

    # Splits two-qubit matrix
    matrix = np.transpose(tensor, (0, 2, 1, 3))
    dims = matrix.shape
    matrix = np.reshape(matrix, (dims[0] * dims[1], dims[2] * dims[3]))
    u_mat, s_list, v_mat = np.linalg.svd(matrix, full_matrices=False)
    s_list = s_list[s_list > 1e-6]
    u_mat = u_mat[:, 0 : len(s_list)]
    v_mat = v_mat[0 : len(s_list), :]

    tensor1 = u_mat
    tensor2 = np.diag(s_list) @ v_mat

    # Reshape into physical dimensions and bond dimension
    tensor1 = np.reshape(tensor1, (2, 2, tensor1.shape[1]))
    tensor2 = np.reshape(tensor2, (tensor2.shape[0], 2, 2))
    tensor2 = np.transpose(tensor2, (1, 2, 0))

    # Add dummy dimension to boundaries
    tensor1 = np.expand_dims(tensor1, axis=2)
    tensor2 = np.expand_dims(tensor2, axis=3)
    return [tensor1, tensor2]


def extend_gate(tensor: NDArray[np.complex128], sites: list[int]) -> MPO:
    """Extends gate to long-range MPO.

    Extends a given gate tensor to a Matrix Product Operator (MPO) by adding identity tensors
    between specified sites.

    Args:
        tensor (NDArray[np.complex128]): The input gate tensor to be extended.
        sites (list[int]): A list of site indices where the gate tensor is to be applied.

    Returns:
        MPO: The resulting Matrix Product Operator with the gate tensor extended over the specified sites.

    Notes:
        - The function handles cases where the input tensor is split into either 2 or 3 tensors.
        - Identity tensors are inserted between the specified sites.
        - If the sites are provided in reverse order, the resulting MPO tensors are reversed and
          transposed accordingly.
    """
    tensors = split_tensor(tensor)
    if len(tensors) == 2:
        # Adds identity tensors between sites
        mpo_tensors = [tensors[0]]
        for _ in range(np.abs(sites[0] - sites[1]) - 1):
            previous_right_bond = mpo_tensors[-1].shape[3]
            identity_tensor = np.zeros((2, 2, previous_right_bond, previous_right_bond))
            for i in range(previous_right_bond):
                identity_tensor[:, :, i, i] = np.identity(2)
            mpo_tensors.append(identity_tensor)
        mpo_tensors.append(tensors[1])

        if sites[1] < sites[0]:
            mpo_tensors.reverse()
            for idx in range(len(mpo_tensors)):
                mpo_tensors[idx] = np.transpose(mpo_tensors[idx], (0, 1, 3, 2))

    elif len(tensors) == 3:
        mpo_tensors = [tensors[0]]
        for _ in range(np.abs(sites[0] - sites[1]) - 1):
            previous_right_bond = mpo_tensors[-1].shape[3]
            identity_tensor = np.zeros((2, 2, previous_right_bond, previous_right_bond))
            for i in range(previous_right_bond):
                identity_tensor[:, :, i, i] = np.identity(2)
            mpo_tensors.append(identity_tensor)
        mpo_tensors.append(tensors[1])
        for _ in range(np.abs(sites[1] - sites[2]) - 1):
            previous_right_bond = mpo_tensors[-1].shape[3]
            identity_tensor = np.zeros((2, 2, previous_right_bond, previous_right_bond))
            for i in range(previous_right_bond):
                identity_tensor[:, :, i, i] = np.identity(2)
            mpo_tensors.append(identity_tensor)
        mpo_tensors.append(tensors[2])

    mpo = MPO()
    mpo.init_custom(mpo_tensors, transpose=False)
    return mpo


class BaseGate:
    """Base class representing a quantum gate.

    Attributes:
        name (str): The name of the gate.
        matrix (NDArray[np.complex128]): The matrix representation of the gate.
        interaction (int): The interaction type or level of the gate.
        tensor (NDArray[np.complex128]): The tensor representation of the gate.
        generator (NDArray[np.complex128] | list[NDArray[np.complex128]]): The generator(s) for the gate.

    Methods:
        set_sites(*sites: int) -> None:
            Sets the sites on which the gate acts.
    """

    name: str
    matrix: NDArray[np.complex128]
    interaction: int
    tensor: NDArray[np.complex128]
    generator: NDArray[np.complex128] | list[NDArray[np.complex128]]

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites: list[int] = list(sites)


class X(BaseGate):
    """Class representing the X (NOT) gate.

    Attributes:
        name (str): "x".
        matrix (NDArray[np.complex128]): The 2x2 matrix representation.
        interaction (int): Interaction level (1 for single-qubit).
        tensor (NDArray[np.complex128]): The tensor representation (same as matrix).

    Methods:
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "x"
    matrix = ObservablesLibrary["x"]
    interaction = 1

    tensor = matrix

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class Y(BaseGate):
    """Class representing the Y gate.

    Attributes:
        name (str): "y".
        matrix (NDArray[np.complex128]): The 2x2 matrix representation.
        interaction (int): Interaction level (1 for single-qubit).
        tensor (NDArray[np.complex128]): The tensor representation (same as matrix).

    Methods:
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "y"
    matrix = ObservablesLibrary["y"]
    interaction = 1

    tensor = matrix

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class Z(BaseGate):
    """Class representing the Z gate.

    Attributes:
        name (str): "z".
        matrix (NDArray[np.complex128]): The 2x2 matrix representation.
        interaction (int): Interaction level (1 for single-qubit).
        tensor (NDArray[np.complex128]): The tensor representation (same as matrix).

    Methods:
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "z"
    matrix = ObservablesLibrary["z"]
    interaction = 1

    tensor = matrix

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class H(BaseGate):
    """Class representing the Hadamard (H) gate.

    Attributes:
        name (str): "h".
        matrix (NDArray[np.complex128]): The 2x2 Hadamard matrix.
        interaction (int): Interaction level (1 for single-qubit).
        tensor (NDArray[np.complex128]): The tensor representation (same as matrix).

    Methods:
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "h"
    matrix = np.array([[1 / np.sqrt(2), 1 / np.sqrt(2)], [1 / np.sqrt(2), -1 / np.sqrt(2)]])
    interaction = 1

    tensor = matrix

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class Id(BaseGate):
    """Class representing the identity gate.

    Attributes:
        name (str): "id".
        matrix (NDArray[np.complex128]): The 2x2 identity matrix.
        interaction (int): Interaction level (1 for single-qubit).
        tensor (NDArray[np.complex128]): The tensor representation (same as matrix).

    Methods:
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "id"
    matrix = np.array([[1, 0], [0, 1]])
    interaction = 1

    tensor = matrix

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class SX(BaseGate):
    """Class representing the square-root X (SX) gate.

    Attributes:
        name (str): "sx".
        matrix (NDArray[np.complex128]): The matrix representation of the SX gate.
        interaction (int): Interaction level (1 for single-qubit).
        tensor (NDArray[np.complex128]): The tensor representation (same as matrix).

    Methods:
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "sx"
    matrix = 0.5 * np.array([[1 + 1j, 1 - 1j], [1 - 1j, 1 + 1j]])
    interaction = 1

    tensor = matrix

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class Rx(BaseGate):
    """Represents a rotation gate about the x-axis.

    Attributes:
        name (str): "rx".
        interaction (int): Interaction level (1 for single-qubit).
        theta (Parameter): The rotation angle parameter.
        matrix (NDArray[np.complex128]): The matrix representation computed from theta.
        tensor (NDArray[np.complex128]): The tensor representation (same as matrix).
        sites (list[int]): The sites where the gate is applied.

    Methods:
        set_params(params: list[Parameter]) -> None:
            Sets the rotation parameter and updates the matrix, tensor, and generator.
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "rx"
    interaction = 1

    def set_params(self, params: list[Parameter]) -> None:
        """Sets the rotation parameter for the gate and updates internal representations.

        Parameters
        ----------
        params : list[Parameter]
            A list containing a single rotation angle (`theta`) parameter.

        Updates
        -------
        theta : Parameter
            The rotation angle parameter.
        matrix : NDArray[np.complex128]
            The gate's 2x2 unitary matrix.
        tensor : NDArray[np.complex128]
            The tensor representation, equivalent to the matrix representation.
        generator : list[NDArray[np.complex128]]
            The generator of the gate.
        """
        self.theta = params[0]
        self.matrix = np.array([
            [np.cos(self.theta / 2), -1j * np.sin(self.theta / 2)],
            [-1j * np.sin(self.theta / 2), np.cos(self.theta / 2)],
        ])
        self.tensor = self.matrix

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class Ry(BaseGate):
    """Represents a rotation gate about the y-axis.

    Attributes:
        name (str): "ry".
        interaction (int): Interaction level (1 for single-qubit).
        theta (Parameter): The rotation angle parameter.
        matrix (NDArray[np.complex128]): The matrix representation computed from theta.
        tensor (NDArray[np.complex128]): The tensor representation (same as matrix).
        sites (list[int]): The sites where the gate is applied.

    Methods:
        set_params(params: list[Parameter]) -> None:
            Sets the rotation parameter and updates the matrix, tensor, and generator.
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "ry"
    interaction = 1

    def set_params(self, params: list[Parameter]) -> None:
        """Sets the rotation parameter for the gate and updates internal representations.

        Parameters
        ----------
        params : list[Parameter]
            A list containing a single rotation angle (`theta`) parameter.

        Updates
        -------
        theta : Parameter
            The rotation angle parameter.
        matrix : NDArray[np.complex128]
            The gate's 2x2 unitary matrix.
        tensor : NDArray[np.complex128]
            The tensor representation, equivalent to the matrix representation.
        generator : list[NDArray[np.complex128]]
            The generator of the gate.
        """
        self.theta = params[0]
        self.matrix = np.array([
            [np.cos(self.theta / 2), -np.sin(self.theta / 2)],
            [np.sin(self.theta / 2), np.cos(self.theta / 2)],
        ])
        self.tensor = self.matrix

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class Rz(BaseGate):
    """Represents a rotation gate about the z-axis.

    Attributes:
        name (str): "rz".
        interaction (int): Interaction level (1 for single-qubit).
        theta (Parameter): The rotation angle parameter.
        matrix (NDArray[np.complex128]): The matrix representation computed from theta.
        tensor (NDArray[np.complex128]): The tensor representation (same as matrix).
        sites (list[int]): The sites where the gate is applied.

    Methods:
        set_params(params: list[Parameter]) -> None:
            Sets the rotation parameter and updates the matrix, tensor, and generator.
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "rz"
    interaction = 1

    def set_params(self, params: list[Parameter]) -> None:
        """Sets the rotation parameter for the gate and updates internal representations.

        Parameters
        ----------
        params : list[Parameter]
            A list containing a single rotation angle (`theta`) parameter.

        Updates
        -------
        theta : Parameter
            The rotation angle parameter.
        matrix : NDArray[np.complex128]
            The gate's 2x2 unitary matrix.
        tensor : NDArray[np.complex128]
            The tensor representation, equivalent to the matrix representation.
        generator : list[NDArray[np.complex128]]
            The generator of the gate.
        """
        self.theta = params[0]
        self.matrix = np.array([
            [np.exp(-1j * self.theta / 2), 0],
            [0, np.exp(1j * self.theta / 2)],
        ])
        self.tensor = self.matrix

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class Phase(BaseGate):
    """Class representing a phase gate.

    Attributes:
        name (str): "p".
        interaction (int): Interaction level (1 for single-qubit).
        theta (Parameter): The phase angle parameter.
        matrix (NDArray[np.complex128]): The matrix representation computed from theta.
        tensor (NDArray[np.complex128]): The tensor representation (same as matrix).
        sites (list[int]): The sites where the gate is applied.

    Methods:
        set_params(params: list[Parameter]) -> None:
            Sets the phase parameter and updates the matrix, tensor, and generator.
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "p"
    interaction = 1

    def set_params(self, params: list[Parameter]) -> None:
        """Sets the rotation parameter for the gate and updates internal representations.

        Parameters
        ----------
        params : list[Parameter]
            A list containing a single rotation angle (`theta`) parameter.

        Updates
        -------
        theta : Parameter
            The rotation angle parameter.
        matrix : NDArray[np.complex128]
            The gate's 2x2 unitary matrix.
        tensor : NDArray[np.complex128]
            The tensor representation, equivalent to the matrix representation.
        """
        # Phase gate has one parameter theta.
        self.theta = params[0]
        self.matrix = np.array([[1, 0], [0, np.exp(1j * self.theta)]])
        self.tensor = self.matrix

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class U3(BaseGate):
    """Class representing a U3 gate.

    Attributes:
        name (str): "u".
        interaction (int): Interaction level (1 for single-qubit).
        theta (Parameter): First rotation parameter.
        phi (Parameter): Second rotation parameter.
        lam (Parameter): Third rotation parameter.
        matrix (NDArray[np.complex128]): The matrix representation computed from the parameters.
        tensor (NDArray[np.complex128]): The tensor representation (same as matrix).
        sites (list[int]): The sites where the gate is applied.

    Methods:
        set_params(params: list[Parameter]) -> None:
            Sets the parameters (theta, phi, lambda) and updates the matrix and tensor.
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "u"
    interaction = 1

    def set_params(self, params: list[Parameter]) -> None:
        """Sets the rotation parameter for the gate and updates internal representations.

        Parameters
        ----------
        params : list[Parameter]
            A list containing a three rotation angle (theta, phi, lambda) parameters.

        Updates
        -------
        theta : Parameter
            The rotation angle parameter.
        matrix : NDArray[np.complex128]
            The gate's 2x2 unitary matrix.
        tensor : NDArray[np.complex128]
            The tensor representation, equivalent to the matrix representation.
        """
        self.theta, self.phi, self.lam = params
        self.matrix = np.array([
            [np.cos(self.theta / 2), -np.exp(1j * self.lam) * np.sin(self.theta / 2)],
            [
                np.exp(1j * self.phi) * np.sin(self.theta / 2),
                np.exp(1j * (self.phi + self.lam)) * np.cos(self.theta / 2),
            ],
        ])
        self.tensor = self.matrix

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class CX(BaseGate):
    """Class representing the controlled-NOT (CX) gate.

    Attributes:
        name (str): "cx".
        matrix (NDArray[np.complex128]): The 4x4 matrix representation.
        interaction (int): Interaction level (2 for two-qubit).
        tensor (NDArray[np.complex128]): The tensor representation reshaped to (2, 2, 2, 2).
        generator (list): The generator for the gate.
        mpo: An MPO representation generated from the gate tensor.
        sites (list[int]): The control and target sites.

    Methods:
        set_sites(*sites: int) -> None:
            Sets the sites and updates the tensor and MPO.
    """

    name = "cx"
    matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    interaction = 2

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)
        self.tensor: NDArray[np.complex128] = np.reshape(self.matrix, (2, 2, 2, 2))
        # Generator: π/4 (I-Z ⊗ I-X)
        self.generator = [(np.pi / 4) * np.array([[0, 0], [0, 2]]), np.array([[1, -1], [-1, 1]])]
        self.mpo = extend_gate(self.tensor, self.sites)
        if sites[1] < sites[0]:  # Adjust for reverse control/target
            self.tensor = np.transpose(self.tensor, (1, 0, 3, 2))


class CZ(BaseGate):
    """Class representing the controlled-Z (CZ) gate.

    Attributes:
        name (str): "cz".
        matrix (NDArray[np.complex128]): The 4x4 matrix representation.
        interaction (int): Interaction level (2 for two-qubit).
        tensor (NDArray[np.complex128]): The tensor representation reshaped to (2, 2, 2, 2).
        generator (list): The generator for the gate.
        sites (list[int]): The control and target sites.

    Methods:
        set_sites(*sites: int) -> None:
            Sets the sites and updates the tensor.
    """

    name = "cz"
    matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])
    interaction = 2

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)
        self.tensor: NDArray[np.complex128] = np.reshape(self.matrix, (2, 2, 2, 2))
        # Generator: π/4 (I-Z ⊗ I-Z)
        self.generator = [(np.pi / 4) * np.array([[0, 0], [0, 2]]), np.array([[1, -1], [-1, 1]])]
        if sites[1] < sites[0]:  # Adjust for reverse control/target
            self.tensor = np.transpose(self.tensor, (1, 0, 3, 2))


class CPhase(BaseGate):
    """Class representing the controlled phase (CPhase) gate.

    Attributes:
        name (str): "cp".
        interaction (int): Interaction level (2 for two-qubit).
        theta (Parameter): The phase parameter.
        matrix (NDArray[np.complex128]): The matrix representation computed from theta.
        tensor (NDArray[np.complex128]): The tensor representation reshaped to (2, 2, 2, 2).
        generator (list): The generator for the gate.
        sites (list[int]): The control and target sites.

    Methods:
        set_params(params: list[Parameter]) -> None:
            Sets the phase parameter and updates the matrix, tensor, and generator.
        set_sites(*sites: int) -> None:
            Sets the sites and may update the tensor based on site order.
    """

    name = "cp"
    interaction = 2

    def set_params(self, params: list[Parameter]) -> None:
        """Sets the rotation parameter for the gate and updates internal representations.

        Parameters
        ----------
        params : list[Parameter]
            A list containing a single rotation angle (`theta`) parameter.

        Updates
        -------
        theta : Parameter
            The rotation angle parameter.
        matrix : NDArray[np.complex128]
            The gate's 4x4 unitary matrix.
        tensor : NDArray[np.complex128]
            The tensor representation, transformed by reshaping the matrix
        generator : list[NDArray[np.complex128]]
            The generator of the gate.
        """
        self.theta = params[0]
        self.matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, np.exp(1j * self.theta)]])
        self.tensor: NDArray[np.complex128] = np.reshape(self.matrix, (2, 2, 2, 2))
        # Generator: θ/2 (Z ⊗ P), where P = diag(1, 0)
        self.generator = [(self.theta / 2) * np.array([[1, 0], [0, -1]]), np.array([[1, 0], [0, 0]])]

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)
        if self.interaction > 2:
            self.mpo = extend_gate(self.tensor, self.sites)
        elif sites[1] < sites[0]:  # Adjust for reverse control/target
            self.tensor = np.transpose(self.tensor, (1, 0, 3, 2))


class SWAP(BaseGate):
    """Class representing the SWAP gate.

    Attributes:
        name (str): "swap".
        matrix (NDArray[np.complex128]): The 4x4 matrix representation.
        interaction (int): Interaction level (2 for two-qubit).
        tensor (NDArray[np.complex128]): The tensor representation reshaped to (2, 2, 2, 2).
        generator (list): The generator for the gate.
        sites (list[int]): The sites involved in the swap.

    Methods:
        __init__() -> None:
            Initializes the gate and its generator.
        set_sites(*sites: int) -> None:
            Sets the sites and updates the tensor.
    """

    name = "swap"
    matrix = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    interaction = 2

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)
        self.tensor: NDArray[np.complex128] = np.reshape(self.matrix, (2, 2, 2, 2))


class Rxx(BaseGate):
    r"""Represents a two-qubit rotation gate about the xx-axis.

    Attributes:
        name (str): "rxx".
        interaction (int): Interaction level (2 for two-qubit).
        theta (Parameter): The rotation angle.
        matrix (NDArray[np.complex128]): The matrix representation computed from theta.
        tensor (NDArray[np.complex128]): The tensor representation reshaped to (2, 2, 2, 2).
        generator (list): The generator computed as :math:`(\theta/2)*(X \otimes X)`.
        sites (list[int]): The sites where the gate is applied.

    Methods:
        set_params(params: list[Parameter]) -> None:
            Sets the rotation angle and updates the matrix, tensor, and generator.
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "rxx"
    interaction = 2

    def set_params(self, params: list[Parameter]) -> None:
        """Sets the rotation parameter for the gate and updates internal representations.

        Parameters
        ----------
        params : list[Parameter]
            A list containing a single rotation angle (`theta`) parameter.

        Updates
        -------
        theta : Parameter
            The rotation angle parameter.
        matrix : NDArray[np.complex128]
            The gate's 2x2 unitary matrix.
        tensor : NDArray[np.complex128]
            The tensor representation, equivalent to the matrix representation.
        generator : list[NDArray[np.complex128]]
            The generator of the gate.
        """
        self.theta = params[0]
        self.matrix = np.array([
            [np.cos(self.theta / 2), 0, 0, -1j * np.sin(self.theta / 2)],
            [0, np.cos(self.theta / 2), -1j * np.sin(self.theta / 2), 0],
            [0, -1j * np.sin(self.theta / 2), np.cos(self.theta / 2), 0],
            [-1j * np.sin(self.theta / 2), 0, 0, np.cos(self.theta / 2)],
        ])
        self.tensor: NDArray[np.complex128] = np.reshape(self.matrix, (2, 2, 2, 2))
        # Generator: θ/2 (X ⊗ X)
        self.generator = [(self.theta / 2) * np.array([[0, 1], [1, 0]]), np.array([[0, 1], [1, 0]])]

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class Ryy(BaseGate):
    r"""Represents a two-qubit rotation gate about the yy-axis.

    Attributes:
        name (str): "ryy".
        interaction (int): Interaction level (2 for two-qubit).
        theta (Parameter): The rotation angle.
        matrix (NDArray[np.complex128]): The matrix representation computed from theta.
        tensor (NDArray[np.complex128]): The tensor representation reshaped to (2, 2, 2, 2).
        generator (list): The generator computed as :math:`(\theta/2)*(Y \otimes Y)`.
        sites (list[int]): The sites where the gate is applied.

    Methods:
        set_params(params: list[Parameter]) -> None:
            Sets the rotation angle and updates the matrix, tensor, and generator.
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "ryy"
    interaction = 2

    def set_params(self, params: list[Parameter]) -> None:
        """Sets the rotation parameter for the gate and updates internal representations.

        Parameters
        ----------
        params : list[Parameter]
            A list containing a single rotation angle (`theta`) parameter.

        Updates
        -------
        theta : Parameter
            The rotation angle parameter.
        matrix : NDArray[np.complex128]
            The gate's 2x2 unitary matrix.
        tensor : NDArray[np.complex128]
            The tensor representation, equivalent to the matrix representation.
        generator : list[NDArray[np.complex128]]
            The generator of the gate.
        """
        self.theta = params[0]
        self.matrix = np.array([
            [np.cos(self.theta / 2), 0, 0, 1j * np.sin(self.theta / 2)],
            [0, np.cos(self.theta / 2), -1j * np.sin(self.theta / 2), 0],
            [0, -1j * np.sin(self.theta / 2), np.cos(self.theta / 2), 0],
            [1j * np.sin(self.theta / 2), 0, 0, np.cos(self.theta / 2)],
        ])
        self.tensor: NDArray[np.complex128] = np.reshape(self.matrix, (2, 2, 2, 2))
        # Generator: θ/2 (Y ⊗ Y)
        self.generator = [(self.theta / 2) * np.array([[0, -1j], [1j, 0]]), np.array([[0, -1j], [1j, 0]])]

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class Rzz(BaseGate):
    r"""Represents a two-qubit rotation gate about the zz-axis.

    Attributes:
        name (str): "rzz".
        interaction (int): Interaction level (2 for two-qubit).
        theta (Parameter): The rotation angle.
        matrix (NDArray[np.complex128]): The matrix representation computed from theta.
        tensor (NDArray[np.complex128]): The tensor representation reshaped to (2, 2, 2, 2).
        generator (list): The generator computed as :math:`(\theta/2)*(Z \otimes Z)`.
        sites (list[int]): The sites where the gate is applied.

    Methods:
        set_params(params: list[Parameter]) -> None:
            Sets the rotation angle and updates the matrix, tensor, and generator.
        set_sites(*sites: int) -> None:
            Sets the site(s) for the gate.
    """

    name = "rzz"
    interaction = 2

    def set_params(self, params: list[Parameter]) -> None:
        """Sets the rotation parameter for the gate and updates internal representations.

        Parameters
        ----------
        params : list[Parameter]
            A list containing a single rotation angle (`theta`) parameter.

        Updates
        -------
        theta : Parameter
            The rotation angle parameter.
        matrix : NDArray[np.complex128]
            The gate's 2x2 unitary matrix.
        tensor : NDArray[np.complex128]
            The tensor representation, equivalent to the matrix representation.
        generator : list[NDArray[np.complex128]]
            The generator of the gate.
        """
        self.theta = params[0]
        self.matrix = np.array([
            [np.cos(self.theta / 2) - 1j * np.sin(self.theta / 2), 0, 0, 0],
            [0, np.cos(self.theta / 2) + 1j * np.sin(self.theta / 2), 0, 0],
            [0, 0, np.cos(self.theta / 2) + 1j * np.sin(self.theta / 2), 0],
            [0, 0, 0, np.cos(self.theta / 2) - 1j * np.sin(self.theta / 2)],
        ])
        self.tensor: NDArray[np.complex128] = np.reshape(self.matrix, (2, 2, 2, 2))
        # Generator: θ/2 (Z ⊗ Z)
        self.generator = [(self.theta / 2) * np.array([[1, 0], [0, -1]]), np.array([[1, 0], [0, -1]])]

    def set_sites(self, *sites: int) -> None:
        """Sets the sites for the gate.

        Args:
            *sites (int): Variable length argument list specifying site indices.
        """
        self.sites = list(sites)


class GateLibrary:
    """A collection of quantum gate classes for use in simulations.

    Attributes:
        x: Class for the X gate.
        y: Class for the Y gate.
        z: Class for the Z gate.
        sx: Class for the square-root X gate.
        h: Class for the Hadamard gate.
        id: Class for the identity gate.
        rx: Class for the rotation gate about the x-axis.
        ry: Class for the rotation gate about the y-axis.
        rz: Class for the rotation gate about the z-axis.
        u: Class for the U3 gate.
        cx: Class for the controlled-NOT gate.
        cz: Class for the controlled-Z gate.
        swap: Class for the SWAP gate.
        rxx: Class for the rotation gate about the xx-axis.
        ryy: Class for the rotation gate about the yy-axis.
        rzz: Class for the rotation gate about the zz-axis.
        cp: Class for the controlled phase gate.
        p: Class for the phase gate.
    """

    x = X
    y = Y
    z = Z
    sx = SX
    h = H
    id = Id
    rx = Rx
    ry = Ry
    rz = Rz
    u = U3
    cx = CX
    cz = CZ
    swap = SWAP
    rxx = Rxx
    ryy = Ryy
    rzz = Rzz
    cp = CPhase
    p = Phase
