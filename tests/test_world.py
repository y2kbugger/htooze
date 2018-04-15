import pytest
from htooze import world

def test_planet_exists():
    p = world.Planet()
    assert isinstance(p, world.Planet)

def test_planet_size_is_obeyed():
    p = world.Planet((25, 25))
    assert p.size == (25, 25)

# note: add tests to check that x or y can't be 0 (teach raises)

def test_life_can_exist():
    mycell = world.Cell()
    assert isinstance(mycell, world.Cell)

def test_planet_starts_without_life():
    p = world.Planet()
    assert len(p.life) == 0

def test_life_can_live_on_planet():
    p = world.Planet()
    mycell = world.Cell()
    p.addcell(mycell)

    assert len(p.life) == 1
    for coords, cell in p.life.items():
        assert cell is mycell
        assert isinstance(coords, tuple)
        assert int(coords[0]) == coords[0]

@pytest.mark.skip(reason="Save this for later")
def test_life_can_choose_motion():
    mycell = world.Cell()
    move = mycell.choose_move()
    assert int(move.axis) == move.axis
    assert 0 <= move.axis < 2
    assert int(move.distance) == move.distance
