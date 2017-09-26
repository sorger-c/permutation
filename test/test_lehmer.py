import pytest
from   permutation import Permutation

PERMUTATIONS = [
    (Permutation(1,2,3), 0, 0),
    (Permutation(1,2,3), 1, 0),
    (Permutation(1,2,3), 2, 0),
    (Permutation(2,1,3), 2, 1),
    (Permutation(1,2,3), 3, 0),
    (Permutation(1,3,2), 3, 1),
    (Permutation(2,1,3), 3, 2),
    (Permutation(2,3,1), 3, 3),
    (Permutation(3,1,2), 3, 4),
    (Permutation(3,2,1), 3, 5),
    (Permutation(1,2,3), 4, 0),
    (Permutation(1,3,2), 4, 2),
    (Permutation(2,1,3), 4, 6),
    (Permutation(2,3,1), 4, 8),
    (Permutation(3,1,2), 4, 12),
    (Permutation(3,2,1), 4, 14),
    (Permutation(5,1,7,3,2,4,6), 7, 2982),
]

@pytest.mark.parametrize('p,degree,lehmer', PERMUTATIONS)
def test_lehmer(p, degree, lehmer):
    assert p.lehmer(degree) == lehmer

@pytest.mark.parametrize('p', [p for p, _, _ in PERMUTATIONS])
def test_bad_lehmer(p):
    with pytest.raises(ValueError):
        p.lehmer(p.degree-1)

@pytest.mark.parametrize('p,degree,lehmer', PERMUTATIONS)
def test_from_lehmer(p, degree, lehmer):
    assert Permutation.from_lehmer(lehmer, degree) == p

@pytest.mark.parametrize('lehmer,degree', [
    (1, 0),
    (1, 1),
    (6, 3),
    (7, 3),
    (24, 3),
    (24, 4),
    (25, 3),
    (25, 4),
    (-1, 0),
    (-1, 3),
    (5040, 5),
])
def test_bad_from_lehmer(lehmer, degree):
    with pytest.raises(ValueError):
        Permutation.from_lehmer(lehmer, degree)
