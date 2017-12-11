from htooze import world

def test_planet_exists():
    p = world.Planet()
    assert isinstance(p, world.Planet)

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
