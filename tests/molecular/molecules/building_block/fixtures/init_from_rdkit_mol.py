import pytest
import rdkit.Chem.AllChem as rdkit

import stk

from ..case_data import CaseData


def _get_rdkit_molecule() -> rdkit.Mol:
    molecule = rdkit.MolFromSmiles('Br[C+2][C+2]Br')
    rdkit.EmbedMolecule(molecule, rdkit.ETKDGv2())
    return molecule


@pytest.fixture(
    scope='session',
    params=(
        lambda: CaseData(
            building_block=stk.BuildingBlock.init_from_rdkit_mol(
                molecule=_get_rdkit_molecule(),
            ),
            functional_groups=(),
            core_atom_ids=(0, 1, 2, 3),
            placer_ids=(0, 1, 2, 3),
        ),
        lambda: CaseData(
            building_block=stk.BuildingBlock.init_from_rdkit_mol(
                molecule=_get_rdkit_molecule(),
                functional_groups=[stk.BromoFactory()],
            ),
            functional_groups=(
                stk.Bromo(
                    bromine=stk.Br(0),
                    atom=stk.C(1, 2),
                    bonders=(stk.C(1, 2), ),
                    deleters=(stk.Br(0), ),
                ),
                stk.Bromo(
                    bromine=stk.Br(3),
                    atom=stk.C(2, 2),
                    bonders=(stk.C(2, 2), ),
                    deleters=(stk.Br(3), ),
                ),
            ),
            core_atom_ids=(1, 2),
            placer_ids=(1, 2),
        ),
        lambda: CaseData(
            building_block=stk.BuildingBlock.init_from_rdkit_mol(
                molecule=_get_rdkit_molecule(),
                placer_ids=(1, 2),
            ),
            functional_groups=(),
            core_atom_ids=(0, 1, 2, 3),
            placer_ids=(1, 2),
        ),
        lambda: CaseData(
            building_block=stk.BuildingBlock.init_from_rdkit_mol(
                molecule=_get_rdkit_molecule(),
                functional_groups=[stk.BromoFactory()],
                placer_ids=(0, 3),
            ),
            functional_groups=(
                stk.Bromo(
                    bromine=stk.Br(0),
                    atom=stk.C(1, 2),
                    bonders=(stk.C(1, 2), ),
                    deleters=(stk.Br(0), ),
                ),
                stk.Bromo(
                    bromine=stk.Br(3),
                    atom=stk.C(2, 2),
                    bonders=(stk.C(2, 2), ),
                    deleters=(stk.Br(3), ),
                ),
            ),
            core_atom_ids=(1, 2),
            placer_ids=(0, 3),
        ),
        lambda: CaseData(
            building_block=stk.BuildingBlock.init_from_rdkit_mol(
                molecule=_get_rdkit_molecule(),
                functional_groups=[stk.IodoFactory()],
            ),
            functional_groups=(),
            core_atom_ids=(0, 1, 2, 3),
            placer_ids=(0, 1, 2, 3),
        ),
    ),
)
def init_from_rdkit_mol(request) -> CaseData:
    return request.param()
