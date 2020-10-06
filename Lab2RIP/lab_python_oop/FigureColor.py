
class FigureColor:
    """
       Класс "Цвет фигуры"
    """
    def __init__(self):
        self._color = None
    #Свойство для описания цвета фигуры
    @property
    def colorproperty(self):
        return self._color
    #Set color
    @colorproperty.setter
    def colorproperty(self, value):
        self._color = value