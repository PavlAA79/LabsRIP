import unittest
#from icecream_cafe.IcecreamBuilder import Iceman
#from icecream_cafe.Facade import Facade
from IcecreamBuilder import Iceman
from Facade import Facade

test_iceman1 = Iceman("TestIceman1", None, None)
test_iceman2 = Iceman("TestIceman2", None, None)


class TestFacade(unittest.TestCase):
    def test_facade_create_iceman(self):
        facade = Facade(test_iceman1, test_iceman2)
        unknown_iceman1 = facade.iceman1
        unknown_iceman2 = facade.iceman2

        self.assertEqual(unknown_iceman1.name, test_iceman1.name)

        self.assertEqual(unknown_iceman2.name, test_iceman2.name)

if __name__ == '__main__':
    unittest.main()