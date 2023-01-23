""" /*
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */ """


def main():

    area(Triangle(10.0, 5.0))
    area(Rectangle(5.0, 7.0))
    area(Square(4.0))


class Triangle:
    def __init__(self, base, height):
      # self allows to attach parameter to the class
        self.base = base
        if height:
            self.height = height
        else:
            self.height = base

    def area(self):
        area = (self.base * self.height) / 2
        print(area)
        return area


class Rectangle:
    def __init__(self, length, width):
      # self allows to attach parameter to the class
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def area(self):
        area = self.length * self.width
        print(area)
        return area


class Square:
    def __init__(self, side):
      # self allows to attach parameter to the class
        self.side = side

    def area(self):
        area = self.side * self.side
        print(area)
        return area


def area(polygon):
    return polygon.area()


print(main())
