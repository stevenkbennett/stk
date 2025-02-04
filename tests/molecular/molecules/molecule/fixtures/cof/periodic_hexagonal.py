import pytest

import stk

from ...case_data import CaseData


@pytest.fixture(
    scope='session',
    params=(
        lambda name: CaseData(
            molecule=stk.ConstructedMolecule(
                topology_graph=stk.cof.PeriodicHexagonal(
                    building_blocks={
                        stk.BuildingBlock(
                            smiles='BrC1=C(Br)[C+]=N1',
                            functional_groups=[stk.BromoFactory()],
                        ): (
                            4, 5, 6, 7, 8, 9, 20, 21, 23, 24, 30, 36,
                            38, 40, 41, 42, 43, 46, 47, 52, 53, 60, 61,
                        ),
                        stk.BuildingBlock(
                            smiles='BrN1N(Br)[C+]=N1',
                            functional_groups=[stk.BromoFactory()],
                        ): (
                            10, 11, 12, 13, 14, 15, 22, 25, 26, 27, 28,
                            29, 37, 39, 44, 45, 54, 55, 56, 57, 58, 59,
                            31, 62, 63,
                        ),
                        stk.BuildingBlock(
                            smiles=(
                                'Br[C+]1[C+]2[N+][C+2]C2(Br)[C+](I)[C+'
                                '](I)[C+](Br)[C+]1Br'
                            ),
                            functional_groups=[
                                stk.BromoFactory(),
                                stk.IodoFactory(),
                                stk.FluoroFactory(),
                            ],
                        ): (0, 1, 18, 50, 51),
                        stk.BuildingBlock(
                            smiles=(
                                'Br[C+]1[C+]2[S][C+2]C2(Br)[C+](I)[C+]'
                                '(I)[C+](Br)[C+]1Br'
                            ),
                            functional_groups=[
                                stk.BromoFactory(),
                                stk.IodoFactory(),
                                stk.FluoroFactory(),
                            ],
                        ): (2, 16, 34, 49),
                        stk.BuildingBlock(
                            smiles=(
                                'Br[C+]1[C+]2[S][O]C2(Br)[C+](I)[C+](I'
                                ')[C+](Br)[C+]1Br'
                            ),
                            functional_groups=[
                                stk.BromoFactory(),
                                stk.IodoFactory(),
                                stk.FluoroFactory(),
                            ],
                        ): (3, 17, 19, 32, 33, 35, 48),
                    },
                    lattice_size=(2, 2, 1),
                    vertex_alignments={0: 5},
                ),
            ),
            smiles=(
                '[C+]1=NC2=C1[C+]1[C+]3[C+]4C5=C(N=[C+]5)[C+]5[C+]6[C+'
                ']7[C+]8[C+]9C%10=C(N=[C+]%10)[C+]%10[C+]%11C%12=C([C+'
                ']=N%12)[C+]%12[C+]%13[C+]%14[C+]%15C%16=C(N=[C+]%16)['
                'C+]%16[C+]%17C%18=C([C+]=N%18)[C+]%18[C+]([C+]%19[NH2'
                '+][C+2]C%19([C+]%19[C+]%20C%21=C(N=[C+]%21)[C+]%21[C+'
                ']%22C%23=C(N=[C+]%23)[C+]%23[C+]%24C%25=C([C+]=N%25)['
                'C+]%25[C+]%26[C+]%27C%28=C([C+]=N%28)C%28%29OS[C+]%28'
                '[C+]%28C%30=C(N=[C+]%30)[C+]([C+]%30[C+]%21N%21[C+]=N'
                'N%21[C+]%21[C+]%31C%32=C(N=[C+]%32)C%32%33[C+2][NH2+]'
                '[C+]%32[C+]%32C%34=C(N=[C+]%34)[C+]%34[C+]([C+](C%35='
                'C(N=[C+]%35)C5%35[C+2][NH2+][C+]9%35)[C+]5[C+]9[C+]%3'
                '5SOC%35%34C%34=C(N=[C+]%34)[C+]%31[C+]%31C%34=C(N=[C+'
                ']%34)C%34%35OS[C+]%34[C+]%34C%36=C(N=[C+]%36)[C+]([C+'
                ']%17N%17N=[C+]N%17[C+]%31[C+]%17S[C+2]C%17%21N%17N=[C'
                '+]N%17[C+]%18%20)[C+]%17SOC%17%18[C+]%16C%16=C([C+]=N'
                '%16)[C+]%16[C+]%17C%20=C([C+]=N%20)C%20%21OS[C+]%20[C'
                '+]%20C%31=C(N=[C+]%31)[C+]%31[C+]4N4[C+]=NN4[C+]([C+]'
                '%24N4N=[C+]N4[C+]%20[C+]4[C+](C%20=C(N=[C+]%20)[C+]%3'
                '4[C+]%20[C+]([C+]%35N%24N=[C+]N9%24)N9[C+]=NN9[C+]([C'
                '+]%10N9N=[C+]N59)[C+](N5N=[C+]N5[C+]%27[C+](N5N=[C+]N'
                '%205)C5([C+2][NH2+][C+]%255)N5N=[C+]N45)C4(OS[C+]%114'
                ')N4[C+]=NN4[C+]%29[C+]([C+]4[C+]%28N5[C+]=NN5[C+]([C+'
                '](C5=C([C+]=N5)[C+]([C+]%17C5=C(N=[C+]5)C%315[C+2][NH'
                '2+][C+]15)[C+]1S[C+2]C1([C+]%16N1N=[C+]N%141)N1N=[C+]'
                'N41)[C+]2%32)[C+]%33N1N=[C+]N%301)N1[C+]=NN%131)[C+]%'
                '21N1N=[C+]N1%18)[C+](N1N=[C+]N61)C1([C+2]S[C+]%231)N1'
                '[C+]=NN%191)N1[C+]=NN31)C1(OS[C+]%221)N1N=[C+]N%261)N'
                '1[C+]=NN71)N1[C+]=NN1[C+]%15C1([C+2]S[C+]%121)N1N=[C+'
                ']N81'
            ),
            name=name,
        ),
        lambda name: CaseData(
            molecule=stk.ConstructedMolecule(
                topology_graph=stk.cof.PeriodicHexagonal(
                    building_blocks={
                        stk.BuildingBlock(
                            smiles='BrC1=C(Br)[C+]=N1',
                            functional_groups=[stk.BromoFactory()],
                        ): (
                            4, 5, 6, 7, 8, 9, 20, 21, 23, 24, 30, 36,
                            38, 40, 41, 42, 43, 46, 47, 52, 53, 60, 61,
                        ),
                        stk.BuildingBlock(
                            smiles='BrN1N(Br)[C+]=N1',
                            functional_groups=[stk.BromoFactory()],
                        ): (
                            10, 11, 12, 13, 14, 15, 22, 25, 26, 27, 28,
                            29, 37, 39, 44, 45, 54, 55, 56, 57, 58, 59,
                            31, 62, 63,
                        ),
                        stk.BuildingBlock(
                            smiles=(
                                'Br[C+]1[C+]2[N+][C+2]C2(Br)[C+](I)[C+'
                                '](I)[C+](Br)[C+]1Br'
                            ),
                            functional_groups=[
                                stk.BromoFactory(),
                                stk.IodoFactory(),
                                stk.FluoroFactory(),
                            ],
                        ): (0, 1, 18, 50, 51),
                        stk.BuildingBlock(
                            smiles=(
                                'Br[C+]1[C+]2[S][C+2]C2(Br)[C+](I)[C+]'
                                '(I)[C+](Br)[C+]1Br'
                            ),
                            functional_groups=[
                                stk.BromoFactory(),
                                stk.IodoFactory(),
                                stk.FluoroFactory(),
                            ],
                        ): (2, 16, 34, 49),
                        stk.BuildingBlock(
                            smiles=(
                                'Br[C+]1[C+]2[S][O]C2(Br)[C+](I)[C+](I'
                                ')[C+](Br)[C+]1Br'
                            ),
                            functional_groups=[
                                stk.BromoFactory(),
                                stk.IodoFactory(),
                                stk.FluoroFactory(),
                            ],
                        ): (3, 17, 19, 32, 33, 35, 48),
                    },
                    lattice_size=(2, 2, 1),
                    vertex_alignments={0: 5},
                    optimizer=stk.PeriodicCollapser(),
                ),
            ),
            smiles=(
                '[C+]1=NC2=C1[C+]1[C+]3[C+]4C5=C(N=[C+]5)[C+]5[C+]6[C+'
                ']7[C+]8[C+]9C%10=C(N=[C+]%10)[C+]%10[C+]%11C%12=C([C+'
                ']=N%12)[C+]%12[C+]%13[C+]%14[C+]%15C%16=C(N=[C+]%16)['
                'C+]%16[C+]%17C%18=C([C+]=N%18)[C+]%18[C+]([C+]%19[NH2'
                '+][C+2]C%19([C+]%19[C+]%20C%21=C(N=[C+]%21)[C+]%21[C+'
                ']%22C%23=C(N=[C+]%23)[C+]%23[C+]%24C%25=C([C+]=N%25)['
                'C+]%25[C+]%26[C+]%27C%28=C([C+]=N%28)C%28%29OS[C+]%28'
                '[C+]%28C%30=C(N=[C+]%30)[C+]([C+]%30[C+]%21N%21[C+]=N'
                'N%21[C+]%21[C+]%31C%32=C(N=[C+]%32)C%32%33[C+2][NH2+]'
                '[C+]%32[C+]%32C%34=C(N=[C+]%34)[C+]%34[C+]([C+](C%35='
                'C(N=[C+]%35)C5%35[C+2][NH2+][C+]9%35)[C+]5[C+]9[C+]%3'
                '5SOC%35%34C%34=C(N=[C+]%34)[C+]%31[C+]%31C%34=C(N=[C+'
                ']%34)C%34%35OS[C+]%34[C+]%34C%36=C(N=[C+]%36)[C+]([C+'
                ']%17N%17N=[C+]N%17[C+]%31[C+]%17S[C+2]C%17%21N%17N=[C'
                '+]N%17[C+]%18%20)[C+]%17SOC%17%18[C+]%16C%16=C([C+]=N'
                '%16)[C+]%16[C+]%17C%20=C([C+]=N%20)C%20%21OS[C+]%20[C'
                '+]%20C%31=C(N=[C+]%31)[C+]%31[C+]4N4[C+]=NN4[C+]([C+]'
                '%24N4N=[C+]N4[C+]%20[C+]4[C+](C%20=C(N=[C+]%20)[C+]%3'
                '4[C+]%20[C+]([C+]%35N%24N=[C+]N9%24)N9[C+]=NN9[C+]([C'
                '+]%10N9N=[C+]N59)[C+](N5N=[C+]N5[C+]%27[C+](N5N=[C+]N'
                '%205)C5([C+2][NH2+][C+]%255)N5N=[C+]N45)C4(OS[C+]%114'
                ')N4[C+]=NN4[C+]%29[C+]([C+]4[C+]%28N5[C+]=NN5[C+]([C+'
                '](C5=C([C+]=N5)[C+]([C+]%17C5=C(N=[C+]5)C%315[C+2][NH'
                '2+][C+]15)[C+]1S[C+2]C1([C+]%16N1N=[C+]N%141)N1N=[C+]'
                'N41)[C+]2%32)[C+]%33N1N=[C+]N%301)N1[C+]=NN%131)[C+]%'
                '21N1N=[C+]N1%18)[C+](N1N=[C+]N61)C1([C+2]S[C+]%231)N1'
                '[C+]=NN%191)N1[C+]=NN31)C1(OS[C+]%221)N1N=[C+]N%261)N'
                '1[C+]=NN71)N1[C+]=NN1[C+]%15C1([C+2]S[C+]%121)N1N=[C+'
                ']N81'
            ),
            name=name,
        ),
    ),
)
def cof_periodic_hexagonal(request) -> CaseData:
    return request.param(
        f'{request.fixturename}{request.param_index}',
    )
