from htooze import world

def test_planet_exists():
    p = world.Planet()
    assert isinstance(p, world.Planet)

