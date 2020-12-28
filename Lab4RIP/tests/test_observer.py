from unittest import main
from unittest import TestCase
from unittest.mock import patch
#from icecream_cafe.IcecreamBuilder import Iceman, Type1IcecreamBuilder
#from icecream_cafe.Observer import StartIcecreamObserver,FinishIcecreamObserver
from IcecreamBuilder import Iceman, Type1IcecreamBuilder
from Observer import StartIcecreamObserver,FinishIcecreamObserver

class TestObserver(TestCase):
    @patch('Observer.StartIcecreamObserver')
    def test_start_icecream_observer(self, MockObserver):
        observer = MockObserver
        iceman = Iceman("Iceman", observer, None)
        builder1 = Type1IcecreamBuilder()
        iceman.builder = builder1
        observer.update.assert_called_once()

    @patch('Observer.FinishIcecreamObserver')
    def test_finish_icecream_observer(self, MockObserver):
        observer = MockObserver
        iceman = Iceman("Iceman", None, observer)
        builder1 = Type1IcecreamBuilder()
        iceman.builder = builder1
        iceman.build_complex_icecream()
        observer.update.assert_called_once()

if __name__ == '__main__':
    main()