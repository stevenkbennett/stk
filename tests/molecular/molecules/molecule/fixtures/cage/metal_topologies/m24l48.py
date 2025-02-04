import pytest

import stk

from ....case_data import CaseData
from ...building_blocks import get_linker, get_pd_atom


@pytest.fixture(
    scope='session',
    params=(
        lambda name: CaseData(
            molecule=stk.ConstructedMolecule(
                topology_graph=stk.cage.M24L48(
                    building_blocks={
                        get_pd_atom(): range(24),
                        get_linker(): range(24, 72),
                    },
                    reaction_factory=stk.DativeReactionFactory(
                        stk.GenericReactionFactory(
                            bond_orders={
                                frozenset({
                                    stk.GenericFunctionalGroup,
                                    stk.SingleAtom,
                                }): 9,
                            },
                        ),
                    ),
                ),
            ),
            smiles=(
                '[H]C1=C([H])C2=C([H])C(=C1[H])C1=C([H])C([H])=N(->['
                'Pd+2]34<-N5=C([H])C([H])=C(C([H])=C5[H])C5=C([H])C(['
                'H])=C([H])C(=C5[H])C5=C([H])C([H])=N(->[Pd+2]67<-N8='
                'C([H])C([H])=C(C([H])=C8[H])C8=C([H])C([H])=C([H])C('
                '=C8[H])C8=C([H])C([H])=N(->[Pd+2]9%10<-N%11=C([H])C('
                '[H])=C(C([H])=C%11[H])C%11=C([H])C([H])=C([H])C(=C%1'
                '1[H])C%11=C([H])C([H])=N(->[Pd+2]%12%13<-N%14=C([H])'
                'C([H])=C(C([H])=C%14[H])C%14=C([H])C([H])=C([H])C(=C'
                '%14[H])C%14=C([H])C([H])=N(->[Pd+2]%15%16<-N%17=C([H'
                '])C([H])=C(C([H])=C%17[H])C%17=C([H])C([H])=C([H])C('
                '=C%17[H])C%17=C([H])C([H])=N(->[Pd+2]%18%19<-N%20=C('
                '[H])C([H])=C(C([H])=C%20[H])C%20=C([H])C([H])=C([H])'
                'C(=C%20[H])C%20=C([H])C([H])=N(->[Pd+2]%21%22<-N%23='
                'C([H])C([H])=C(C([H])=C%23[H])C%23=C([H])C(=C([H])C('
                '[H])=C%23[H])C%23=C([H])C([H])=N(->[Pd+2]%24%25<-N%2'
                '6=C([H])C([H])=C(C([H])=C%26[H])C%26=C([H])C([H])=C('
                '[H])C(=C%26[H])C%26=C([H])C([H])=N(->[Pd+2](<-N%27=C'
                '([H])C([H])=C(C([H])=C%27[H])C%27=C([H])C([H])=C([H]'
                ')C(=C%27[H])C%27=C([H])C([H])=N->%15C([H])=C%27[H])('
                '<-N%15=C([H])C([H])=C(C([H])=C%15[H])C%15=C([H])C([H'
                '])=C([H])C(=C%15[H])C%15=C([H])C([H])=N->%18C([H])=C'
                '%15[H])<-N%15=C([H])C([H])=C(C([H])=C%15[H])C%15=C(['
                'H])C(=C([H])C([H])=C%15[H])C%15=C([H])C([H])=N(->[Pd'
                '+2]%18%27<-N%28=C([H])C([H])=C(C([H])=C%28[H])C%28=C'
                '([H])C([H])=C([H])C(=C%28[H])C%28=C([H])C([H])=N(->['
                'Pd+2]%29(<-N%30=C([H])C([H])=C(C([H])=C%30[H])C%30=C'
                '([H])C([H])=C([H])C(=C%30[H])C%30=C([H])C([H])=N(->['
                'Pd+2]%31%32<-N%33=C([H])C([H])=C(C([H])=C%33[H])C%33'
                '=C([H])C(=C([H])C([H])=C%33[H])C%33=C([H])C([H])=N(-'
                '>[Pd+2](<-N%34=C([H])C([H])=C(C([H])=C%34[H])C%34=C('
                '[H])C([H])=C([H])C(=C%34[H])C%34=C([H])C([H])=N(->[P'
                'd+2]%35(<-N%36=C([H])C([H])=C(C([H])=C%36[H])C%36=C('
                '[H])C([H])=C([H])C(=C%36[H])C%36=C([H])C([H])=N(->[P'
                'd+2](<-N%37=C([H])C([H])=C(C([H])=C%37[H])C%37=C([H]'
                ')C([H])=C([H])C(=C%37[H])C%37=C([H])C([H])=N(->[Pd+2'
                '](<-N%38=C([H])C([H])=C(C([H])=C%38[H])C%38=C([H])C('
                '[H])=C([H])C(=C%38[H])C%38=C([H])C([H])=N(->[Pd+2](<'
                '-N%39=C([H])C([H])=C(C([H])=C%39[H])C%39=C([H])C([H]'
                ')=C([H])C(=C%39[H])C%39=C([H])C([H])=N->%29C([H])=C%'
                '39[H])(<-N%29=C([H])C([H])=C(C([H])=C%29[H])C%29=C(['
                'H])C(=C([H])C([H])=C%29[H])C%29=C([H])C([H])=N->6C(['
                'H])=C%29[H])<-N6=C([H])C([H])=C(C([H])=C6[H])C6=C([H'
                '])C(=C([H])C([H])=C6[H])C6=C([H])C([H])=N->9C([H])=C'
                '6[H])C([H])=C%38[H])(<-N6=C([H])C([H])=C(C([H])=C6[H'
                '])C6=C([H])C([H])=C([H])C(=C6[H])C6=C([H])C([H])=N->'
                '%31C([H])=C6[H])<-N6=C([H])C([H])=C(C([H])=C6[H])C6='
                'C([H])C(=C([H])C([H])=C6[H])C6=C([H])C([H])=N->3C([H'
                '])=C6[H])C([H])=C%37[H])(<-N3=C([H])C([H])=C(C([H])='
                'C3[H])C3=C([H])C([H])=C([H])C(=C3[H])C3=C([H])C([H])='
                'N(->[Pd+2]6(<-N9=C([H])C([H])=C(C([H])=C9[H])C9=C([H]'
                ')C([H])=C([H])C(=C9[H])C9=C([H])C([H])=N(->[Pd+2]%29'
                '(<-N%31=C([H])C([H])=C(C([H])=C%31[H])C%31=C([H])C(['
                'H])=C([H])C(=C%31[H])C%31=C([H])C([H])=N(->[Pd+2](<-'
                'N%37=C([H])C([H])=C(C([H])=C%37[H])C%37=C([H])C([H])'
                '=C([H])C(=C%37[H])C%37=C([H])C([H])=N->%19C([H])=C%3'
                '7[H])(<-N%19=C([H])C([H])=C(C([H])=C%19[H])C%19=C([H'
                '])C(=C([H])C([H])=C%19[H])C%19=C([H])C([H])=N(->[Pd+'
                '2](<-N%37=C([H])C([H])=C(C([H])=C%37[H])C%37=C([H])C'
                '([H])=C([H])C(=C%37[H])C%37=C([H])C([H])=N->%12C([H]'
                ')=C%37[H])(<-N%12=C([H])C([H])=C(C([H])=C%12[H])C%12'
                '=C([H])C(=C([H])C([H])=C%12[H])C%12=C([H])C([H])=N(-'
                '>[Pd+2](<-N%37=C([H])C([H])=C(C([H])=C%37[H])C%37=C('
                '[H])C([H])=C([H])C(=C%37[H])C%37=C([H])C([H])=N->6C('
                '[H])=C%37[H])(<-N6=C([H])C([H])=C(C([H])=C6[H])C6=C(['
                'H])C([H])=C([H])C(=C6[H])C6=C([H])C([H])=N->%29C([H]'
                ')=C6[H])<-N6=C([H])C([H])=C2C([H])=C6[H])C([H])=C%12'
                '[H])<-N2=C([H])C([H])=C(C([H])=C2[H])C2=C([H])C(=C([H'
                '])C([H])=C2[H])C2=C([H])C([H])=N->7C([H])=C2[H])C([H]'
                ')=C%19[H])<-N2=C([H])C([H])=C(C([H])=C2[H])C2=C([H])C'
                '(=C([H])C([H])=C2[H])C2=C([H])C([H])=N->%13C([H])=C2['
                'H])C([H])=C%31[H])<-N2=C([H])C([H])=C(C([H])=C2[H])C2'
                '=C([H])C([H])=C([H])C(=C2[H])C2=C([H])C([H])=N->%21C('
                '[H])=C2[H])C([H])=C9[H])<-N2=C([H])C([H])=C(C([H])=C'
                '2[H])C2=C([H])C([H])=C([H])C(=C2[H])C2=C([H])C([H])='
                'N(->[Pd+2](<-N6=C([H])C([H])=C(C([H])=C6[H])C6=C([H]'
                ')C([H])=C([H])C(=C6[H])C6=C([H])C([H])=N->%22C([H])='
                'C6[H])(<-N6=C([H])C([H])=C(C([H])=C6[H])C6=C([H])C(=C'
                '([H])C([H])=C6[H])C6=C([H])C([H])=N->%35C([H])=C6[H])'
                '<-N6=C([H])C([H])=C(C([H])=C6[H])C6=C([H])C(=C([H])C('
                '[H])=C6[H])C6=C([H])C([H])=N->%24C([H])=C6[H])C([H])='
                'C2[H])C([H])=C3[H])<-N2=C([H])C([H])=C(C([H])=C2[H])C'
                '2=C([H])C(=C([H])C([H])=C2[H])C2=C([H])C([H])=N->4C(['
                'H])=C2[H])C([H])=C%36[H])<-N2=C([H])C([H])=C(C([H])=C'
                '2[H])C2=C([H])C([H])=C([H])C(=C2[H])C2=C([H])C([H])='
                'N->%32C([H])=C2[H])C([H])=C%34[H])(<-N2=C([H])C([H])'
                '=C(C([H])=C2[H])C2=C([H])C([H])=C([H])C(=C2[H])C2=C('
                '[H])C([H])=N->%25C([H])=C2[H])<-N2=C([H])C([H])=C(C'
                '([H])=C2[H])C2=C([H])C([H])=C([H])C(=C2[H])C2=C([H])'
                'C([H])=N->%18C([H])=C2[H])C([H])=C%33[H])C([H])=C%30'
                '[H])<-N2=C([H])C([H])=C(C([H])=C2[H])C2=C([H])C(=C(['
                'H])C([H])=C2[H])C2=C([H])C([H])=N(->[Pd+2](<-N3=C([H'
                '])C([H])=C(C([H])=C3[H])C3=C([H])C([H])=C([H])C(=C3['
                'H])C3=C([H])C([H])=N->%27C([H])=C3[H])(<-N3=C([H])C'
                '([H])=C(C([H])=C3[H])C3=C([H])C([H])=C([H])C(=C3[H])'
                'C3=C([H])C([H])=N->%10C([H])=C3[H])<-N3=C([H])C([H])'
                '=C(C([H])=C3[H])C3=C([H])C([H])=C([H])C(=C3[H])C3=C('
                '[H])C([H])=N->%16C([H])=C3[H])C([H])=C2[H])C([H])=C%'
                '28[H])C([H])=C%15[H])C([H])=C%26[H])C([H])=C%23[H])C'
                '([H])=C%20[H])C([H])=C%17[H])C([H])=C%14[H])C([H])=C'
                '%11[H])C([H])=C8[H])C([H])=C5[H])C([H])=C1[H]'
            ),
            name=name,
        ),
    ),
)
def metal_cage_m24l48(request) -> CaseData:
    return request.param(
        f'{request.fixturename}{request.param_index}',
    )
