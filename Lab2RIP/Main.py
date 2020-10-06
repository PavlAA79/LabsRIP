import colorama
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
from colorama import Fore, Style
colorama.init()


def main():
    print(Fore.GREEN + 'Павловская А.А. ИУ5-51Б')
    print(Style.RESET_ALL)
    figure1 = Rectangle("синего", 15, 15)
    figure2 = Circle("зеленого", 15)
    figure3 = Square("красного", 15)
    print(figure1)
    print(figure2)
    print(figure3)

if __name__ == "__main__":
    main()

