import pytest
from   permutation import Permutation

@pytest.mark.parametrize('a,b,p', [
    (1, 1, Permutation()),
    (1, 2, Permutation(2,1)),
    (2, 1, Permutation(2,1)),
    (4, 7, Permutation(1,2,3,7,5,6,4)),
    (7, 4, Permutation(1,2,3,7,5,6,4)),
    (7, 7, Permutation()),
])
def test_transposition(a,b,p):
    assert Permutation.transposition(a,b) == p

@pytest.mark.parametrize('cyc,p', [
    ((), Permutation()),
    ((1,), Permutation()),
    ((1,2), Permutation(2,1)),
    ((2,1), Permutation(2,1)),
    ((1,2,3,4), Permutation(2,3,4,1)),
])
def test_cycle(cyc, p):
    assert Permutation.cycle(*cyc) == p

@pytest.mark.parametrize('cycles,p', [
    ((), Permutation()),
    (((),), Permutation()),
    (((1,2),(2,1)), Permutation()),
    (((1,2,3),), Permutation(2,3,1)),
    (((1,2,3),()), Permutation(2,3,1)),
    (((1,2,3),(3,)), Permutation(2,3,1)),
    (((1,2,3),(4,)), Permutation(2,3,1)),
    (((1,2,3),(2,1)), Permutation(3,2,1)),
    (((2,1),(1,2,3)), Permutation(1,3,2)),
    (((1,2),(3,4,5)), Permutation(2,1,4,5,3)),
    (((3,4,5),(1,2)), Permutation(2,1,4,5,3)),
])
def test_from_cycles(cycles, p):
    assert Permutation.from_cycles(*cycles) == p

@pytest.mark.parametrize('s,p', [
    ('1',              Permutation()),
    ('()',             Permutation()),
    ('(5)',            Permutation()),
    (' ( 5 ) ',        Permutation()),
    ('(1 2) (2 1)',    Permutation()),
    ('(1 2 3)',        Permutation(2,3,1)),
    (' (1  2  3) \n ', Permutation(2,3,1)),
    ('\t\n(1\r2\r3)',  Permutation(2,3,1)),
    ('(1 2 3) ()',     Permutation(2,3,1)),
    ('(1 2 3) (3 )',   Permutation(2,3,1)),
    ('(1\n2 3) (4 )',  Permutation(2,3,1)),
    ('(1 2 3) (2 1)',  Permutation(3,2,1)),
    ('(2 1) (1 2 3)',  Permutation(1,3,2)),
    ('(1 2) (3 4 5)',  Permutation(2,1,4,5,3)),
    ('(3 4 5) (1 2)',  Permutation(2,1,4,5,3)),
    ('(3,4,5) (1,2)',  Permutation(2,1,4,5,3)),
    ('(3,4,5),(1,2)',  Permutation(2,1,4,5,3)),
    ('(3 4 5),(1 2)',  Permutation(2,1,4,5,3)),
])
def test_parse(s,p):
    assert Permutation.parse(s) == p

@pytest.mark.parametrize('a,b', [
    (1,0),
    (0,1),
    (0,0),
    (-1, 5),
    (5, -1),
    (-1, -1),
])
def test_bad_transposition(a,b):
    with pytest.raises(ValueError):
        Permutation.transposition(a,b)

@pytest.mark.parametrize('cyc', [
    [-1],
    [1, 2, -1],
    [-1, -2, -3],
    [1, 2, 1],
    [1, 1],
])
def test_bad_cycle(cyc):
    with pytest.raises(ValueError):
        Permutation.cycle(*cyc)

@pytest.mark.parametrize('cycles', [
    [(-1,)],
    [(1, 2, -1,)],
    [(-1, -2, -3,)],
    [(1, 2, 1,)],
    [(1, 1,)],
    [(-1, 2), (-1, 2)],
])
def test_bad_from_cycles(cycles):
    with pytest.raises(ValueError):
        Permutation.from_cycles(*cycles)

@pytest.mark.parametrize('s', [
    '',
    '1,',
    '(-1)',
    '1 2',
    '(one two)',
    '1 (1 2 3)',
    '(1 2 3',
    '[1 2 3]',
    '1,2,3',
    '(1 2 -1)',
    '(-1 -2 -3)',
    '(1 2, 1)',
    '(1 1)',
    '(-1 2) (-1 2)',
    '((3 4 5) (1 2))',
    '(3 4 5, 4 2)',
    '(3 4 5 4 2)',
    pytest.param('(,)', marks=pytest.mark.xfail),
    ',(1 2 3)',
    '(1 2 3),',
])
def test_bad_parse(s):
    with pytest.raises(ValueError):
        Permutation.parse(s)

@pytest.mark.parametrize('img', [
    [2],
    [2, 3],
    [1, 2, 1],
    [0, 1, 2],
    [-1, 2, 3],
    [-1],
    [1, 2, -1],
    [-1, -2, -3],
    [1, 1],
])
def test_bad_init(img):
    with pytest.raises(ValueError):
        Permutation(*img)
