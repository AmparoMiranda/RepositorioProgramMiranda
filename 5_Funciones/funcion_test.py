import pytest
from funcion import*
@pytest.mark.parametrize("a,res")[
    (100,1),
    (12,3),
    (14,5)
]
def test_add_diggit(a,res):
    assert test_add_diggit(a) == res