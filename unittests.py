import unittest

from Cat import Cat


class TestCat(unittest.TestCase):
    def test_get_name(self):
        barsik = Cat('Barsik')
        self.assertEqual(barsik.get_name(), 'Barsik')

    def test_set_name(self):
        catty = Cat('Murka')
        catty.set_name('Snezhok')
        self.assertEqual(catty.get_name(), 'Snezhok')

    def test_play(self):
        meow = Cat('Meow')
        meow.play(15)
        self.assertEqual(meow.mood, 65)
        self.assertEqual(meow.energy, 35)
        with self.assertRaises(ValueError):
            meow.play(150)


if __name__ == '__main__':
    unittest.main()