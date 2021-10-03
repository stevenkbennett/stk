"""
Primary Amino Factory
=====================

"""

from __future__ import annotations

import typing
from collections import abc

from .functional_group_factory import FunctionalGroupFactory
from .utilities import get_atom_ids
from ..functional_groups import PrimaryAmino
from ...molecule import Molecule
from ...atoms import N, H

__all__ = (
    'PrimaryAminoFactory',
)

_ValidIndex = typing.Literal[0, 1, 2, 3]


class PrimaryAminoFactory(FunctionalGroupFactory):
    """
    Creates :class:`.PrimaryAmino` instances.

    Creates functional groups from substructures, which match the
    ``[*][N]([H])[H]`` functional group string.

    Examples:

        *Creating Functional Groups with the Factory*

        You want to create a building block which has
        :class:`.PrimaryAmino` functional groups. You want the nitrogen
        atom to be the *bonder* atom, and the hydrogen atoms to be the
        *deleter* atoms.

        .. testcode:: creating-functional-groups-with-the-factory

            import stk

            building_block = stk.BuildingBlock(
                smiles='NCCCCN',
                functional_groups=(stk.PrimaryAminoFactory(), ),
            )

        .. testcode:: creating-functional-groups-with-the-factory
            :hide:

            assert all(
                isinstance(functional_group, stk.PrimaryAmino)
                for functional_group
                in building_block.get_functional_groups()
            )
            assert building_block.get_num_functional_groups() == 2

        *Changing the Bonder and Deleter Atoms*

        You want to create a building block which has
        :class:`.PrimaryAmino` functional groups. You want the
        non-hydrogen atom bonded to nitrogen to be the *bonder* atom
        and the nitrogen and hydrogen atoms to be *deleter* atoms.

        .. testcode:: changing-the-bonder-and-deleter-atoms

            import stk

            primary_amino_factory = stk.PrimaryAminoFactory(
                # The index of the atom attached to the nitrogen is 0
                # in the functional group string (see docstring).
                bonders=(0, ),
                # The indices of the nitrogen and hydrogen atoms in the
                # functional group string (see docstring) are 1, 2 and
                # 3.
                deleters=(1, 2, 3),
            )
            building_block = stk.BuildingBlock(
                smiles='NCCCCN',
                functional_groups=(primary_amino_factory, ),
            )

        .. testcode:: changing-the-bonder-and-deleter-atoms
            :hide:

            fg1, fg2 = building_block.get_functional_groups()
            assert fg1.get_num_bonders() == 1
            assert sum(1 for _ in fg1.get_deleters()) == 3
            assert fg2.get_num_bonders() == 1
            assert sum(1 for _ in fg2.get_deleters()) == 3

            assert all(
                isinstance(atom, stk.C)
                for functional_group
                in building_block.get_functional_groups()
                for atom
                in functional_group.get_bonders()
            )
            assert all(
                isinstance(atom, (stk.H, stk.N))
                for functional_group
                in building_block.get_functional_groups()
                for atom
                in functional_group.get_deleters()
            )

    See Also:

        :class:`.GenericFunctionalGroup`
            Defines *bonders* and  *deleters*.

    """

    def __init__(
        self,
        bonders: tuple[_ValidIndex, ...] = (1, ),
        deleters: tuple[_ValidIndex, ...] = (2, 3),
        placers: typing.Optional[tuple[_ValidIndex, ...]] = None,
    ) -> None:
        """
        Initialize a :class:`.PrimaryAminoFactory` instance.

        Parameters:

            bonders:
                The indices of atoms in the functional group string,
                which are *bonder* atoms.

            deleters:
                The indices of atoms in the functional group string,
                which are *deleter* atoms.

            placers:
                The indices of atoms in the functional group string,
                which are *placer* atoms. If ``None``, `bonders` will
                be used.

        """

        self._bonders = bonders
        self._deleters = deleters
        self._placers = bonders if placers is None else placers

    def get_functional_groups(
        self,
        molecule: Molecule,
    ) -> abc.Iterable[PrimaryAmino]:

        for atom_ids in get_atom_ids(
            query='[*][N]([H])[H]',
            molecule=molecule,
        ):
            atoms = tuple(molecule.get_atoms(atom_ids))
            yield PrimaryAmino(
                nitrogen=typing.cast(N, atoms[1]),
                hydrogen1=typing.cast(H, atoms[2]),
                hydrogen2=typing.cast(H, atoms[3]),
                atom=atoms[0],
                bonders=tuple(atoms[i] for i in self._bonders),
                deleters=tuple(atoms[i] for i in self._deleters),
                placers=tuple(atoms[i] for i in self._placers),
            )
