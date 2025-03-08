
import matplotlib

matplotlib.use("Agg")

import os
from pathlib import Path

import numpy as np
import pytest
from agox import AGOX
from agox.databases import Database
from agox.environments import Environment
from agox.evaluators import LocalOptimizationEvaluator
from ase import Atoms

from agox_extra.symmetry import SymmetryGenerator


@pytest.fixture(scope="module")
def symmetry_rss(tmp_path_factory) -> Database:

    test_path = tmp_path_factory.mktemp("test-run/")
    current_path = Path.cwd()
    os.chdir(test_path)


    # Manually set seed and database-index
    seed = 42
    database_index = 0

    ##############################################################################
    # Calculator
    ##############################################################################

    from ase.calculators.emt import EMT

    calc = EMT()

    ##############################################################################
    # System & general settings:
    ##############################################################################

    template = Atoms("", cell=np.eye(3) * 24)
    confinement_corner = np.array([3, 3, 3])
    confinement_cell = np.eye(3) * (24 - 6)
    environment = Environment(
        template=template,
        symbols="C24",
        confinement_cell=confinement_cell,
        confinement_corner=confinement_corner,
    )

    # Database
    db_path = "db{}.db".format(database_index)  # From input argument!
    database = Database(filename=db_path, order=3)

    ##############################################################################
    # Search Settings:
    ##############################################################################

    random_generator = SymmetryGenerator(
        **environment.get_confinement(), sym_type="cluster", environment=environment, order=1
    )

    # Wont relax fully with steps:5 - more realistic setting would be 100+.
    evaluator = LocalOptimizationEvaluator(
        calc,
        gets={"get_key": "candidates"},
        optimizer_run_kwargs={"fmax": 0.05, "steps": 2},
        store_trajectory=False,
        order=2,
        constraints=environment.get_constraints(),
    )

    ##############################################################################
    # Let get the show running!
    ##############################################################################

    agox = AGOX(random_generator, database, evaluator, seed=seed)

    agox.run(N_iterations=10)
    os.chdir(current_path)
    return database

def test_has_candidates(symmetry_rss: Database) -> None:
    print(symmetry_rss)
    assert len(symmetry_rss.get_all_candidates()) != 0

