"""
Tests functions which use MacroModel.

These tests are only run when the --macromodel_path pytest option is
used. MacroModel is 3rd party software, it does not come with ``stk``.

"""

import pytest
import sys
import os
from os.path import join
import numpy as np
import stk

macromodel = pytest.mark.skipif(
    all('macromodel' not in x for x in sys.argv),
    reason="Only run when explicitly asked.")


outdir = 'macromodel_tests_output'
if not os.path.exists(outdir):
    os.mkdir(outdir)


@macromodel
def test_macromodel_opt(tmp_cc3, macromodel_path):
    tmp_cc3.write(join(outdir, 'mm_opt_before.mol'), conformer=0)

    stk.macromodel_opt(
        tmp_cc3,
        macromodel_path,
        {'md': True, 'gradient': 1, 'restricted': 'both'},
        {'gradient': 1, 'sim_time': 20, 'eq_time': 2, 'confs': 2},
        output_dir='opt_odir',
        conformer=0)

    tmp_cc3.write(join(outdir, 'mm_opt_after.mol'), conformer=0)


@macromodel
def test_macromodel_cage_opt(tmp_cc3, macromodel_path):
    tmp_cc3.write(join(outdir, 'mm_cage_opt_before.mol'), conformer=0)

    stk.macromodel_cage_opt(
        tmp_cc3,
        macromodel_path,
        {'md': True, 'gradient': 1, 'restricted': False},
        {'gradient': 1, 'sim_time': 20, 'eq_time': 2, 'confs': 2},
        output_dir='cage_opt_odir',
        conformer=0)

    tmp_cc3.write(join(outdir, 'mm_cage_opt_after.mol'), conformer=0)


@macromodel
def test_macromodel_eng(amine2, macromodel_path):
    a = amine2.energy.macromodel(forcefield=16,
                                 macromodel_path=macromodel_path,
                                 output_dir='energy_calc')
    assert np.allclose(a=a,
                       b=49.0655,
                       atol=1e-2)
