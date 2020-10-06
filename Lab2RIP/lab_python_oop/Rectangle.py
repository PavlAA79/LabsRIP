from lab_python_oop.Figure import Figure
from lab_python_oop.FigureColor import FigureColor


class Rectangle(Figure):
    """
       Класс "Прямоугольник"
    """
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    #Конструктор Rectangle
    def __init__(self, color_param, width_param, height_param):

        self.fc = FigureColor()
        self.fc.colorproperty = color_param 
        self.width = width_param
        self.height = height_param

    #Переопределение метода вычисления площади
    def square(self):

        return self.width*self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.fc.colorproperty,
            self.width,
            self.height,
            self.square()
        )