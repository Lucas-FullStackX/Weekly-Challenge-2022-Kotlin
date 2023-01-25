""" /*
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */ """

import re


def main():
    countWords(
        "Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev).")


def countWords(text: str):
    dic = {}
    words = re.sub(r"[^a-zA-Z0-9]", " ", text).lower()
    for word in words.split(" "):
        if word == "":
            continue
        if word in dic:
            dic[word] += dic[word] + 1
        else:
            dic[word] = 1
    for key, value in dic.items():
        print(f"{key} se ha repetido {value} {'vez' if value == 1 else 'veces'}")


print(main())
