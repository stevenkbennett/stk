"""
Porphyrin
=========

"""

from ...topology_graph import Edge
from ..metal_complex import MetalComplex
from ..vertices import MetalVertex, UnaligningVertex


class Porphyrin(MetalComplex):
    """
    Represents a metal complex topology graph.

    .. moldoc::

        import moldoc.molecule as molecule
        import stk

        bb1 = stk.BuildingBlock(
            smiles='[Fe+2]',
            functional_groups=(
                stk.SingleAtom(stk.Fe(0, charge=2))
                for i in range(6)
            ),
            position_matrix=[[0, 0, 0]],
        )
        bb2 = stk.BuildingBlock(
            smiles=(
                'C1=CC2=CC3=CC=C([N]3)C=C4C=CC'
                '(=N4)C=C5C=CC(=N5)C=C1[N]2'
            ),
            functional_groups=[
                stk.SmartsFunctionalGroupFactory(
                    smarts='[#6]~[#7]~[#6]',
                    bonders=(1, ),
                    deleters=(),
                ),
            ],
        )
        complex = stk.ConstructedMolecule(
            topology_graph=stk.metal_complex.Porphyrin(
                metals=bb1,
                ligands=bb2,
            ),
        )

        moldoc_display_molecule = molecule.Molecule(
            atoms=(
                molecule.Atom(
                    atomic_number=atom.get_atomic_number(),
                    position=position,
                ) for atom, position in zip(
                    complex.get_atoms(),
                    complex.get_position_matrix(),
                )
            ),
            bonds=(
                molecule.Bond(
                    atom1_id=bond.get_atom1().get_id(),
                    atom2_id=bond.get_atom2().get_id(),
                    order=(
                        1
                        if bond.get_order() == 9
                        else bond.get_order()
                    ),
                ) for bond in complex.get_bonds()
            ),
        )

    Metal building blocks with at least four functional groups are
    required for this topology.

    Ligand building blocks with at least four functional group are
    required for this topology graph.

    When using a :class:`dict` for initialization, a
    :class:`.BuildingBlock` needs to be assigned to each of the
    following numbers:

        | metals: (0, )
        | ligands: (0, )

    See :class:`.MetalComplex` for more details and examples.

    """

    _metal_vertex_prototypes = (MetalVertex(0, (0, 0, 0)), )
    _ligand_vertex_prototypes = (UnaligningVertex(1, (0, 0, 0)), )

    _edge_prototypes = (
        Edge(
            id=0,
            vertex1=_metal_vertex_prototypes[0],
            vertex2=_ligand_vertex_prototypes[0],
            position=(0.1, 0, 0),
        ),
        Edge(
            id=1,
            vertex1=_metal_vertex_prototypes[0],
            vertex2=_ligand_vertex_prototypes[0],
            position=(0, 0.1, 0),
        ),
        Edge(
            id=2,
            vertex1=_metal_vertex_prototypes[0],
            vertex2=_ligand_vertex_prototypes[0],
            position=(-0.1, 0, 0),
        ),
        Edge(
            id=3,
            vertex1=_metal_vertex_prototypes[0],
            vertex2=_ligand_vertex_prototypes[0],
            position=(0, -0.1, 0),
        ),
    )
