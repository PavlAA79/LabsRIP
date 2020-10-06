from abc import ABC, abstractmethod


class Figure(ABC):
    """
       Класс "Геометрическая фигура"
    """
    #Абстрактный метод вычисления площади
    @abstractmethod
    def square(self):
        pass