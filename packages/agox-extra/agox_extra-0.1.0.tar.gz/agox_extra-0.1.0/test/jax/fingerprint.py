import pytest

from agox_extra.jax import JaxFingerprint

from ase import Atoms
from ase.build import molecule

@pytest.fixture(params=['CH3CHO', 'H2O', 'CH3COCl'])
def atoms_data(request) -> Atoms:

    formula = request.param
    atoms = molecule(formula)
    atoms.set_pbc([False, False, False])
    atoms.set_cell([10, 10, 10])
    atoms.center()

    return atoms

@pytest.fixture
def jax_fingerprint(atoms_data: Atoms) -> JaxFingerprint:
    return JaxFingerprint.from_atoms(atoms_data)

def test_fingerprint(jax_fingerprint: JaxFingerprint, atoms_data: Atoms):
    f = jax_fingerprint.get_features(atoms_data)
    n_pairs = len(jax_fingerprint.pairs)
    n_triplets = len(jax_fingerprint.triplets)
    assert f.shape[1] == jax_fingerprint.n_bins_radial * n_pairs + jax_fingerprint.n_bins_angular * n_triplets

def test_fingerprint_gradient(jax_fingerprint: JaxFingerprint, atoms_data: Atoms): 
    f = jax_fingerprint.get_feature_gradient(atoms_data)
    n_pairs = len(jax_fingerprint.pairs)
    n_triplets = len(jax_fingerprint.triplets)
    n_features = jax_fingerprint.n_bins_radial * n_pairs + jax_fingerprint.n_bins_angular * n_triplets
    assert f.shape == (1, len(atoms_data), 3, n_features)


