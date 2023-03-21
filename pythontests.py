import pytest
from Cat import Cat


@pytest.fixture()
def create_cat():
    catty = Cat('Barsik')
    return catty


def test_name_getter(create_cat):
    assert create_cat.get_name() == 'Barsik'


def test_name_setter(create_cat):
    create_cat.set_name('Murzik')
    assert create_cat.get_name() == 'Murzik'


@pytest.mark.parametrize("time, expected_mood, expected_energy", [(10, 60, 40), (15, 65, 35), (20, 70, 30)])
def test_player(create_cat, time, expected_mood, expected_energy):
    create_cat.play(time)
    assert create_cat.energy == expected_energy
    assert create_cat.mood == expected_mood
    with pytest.raises(ValueError):
        create_cat.play(300)
