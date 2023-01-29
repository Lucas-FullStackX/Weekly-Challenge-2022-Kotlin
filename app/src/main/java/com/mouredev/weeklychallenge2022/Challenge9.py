""" /*
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
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
    naturalText = "Chocapic. Es una marca de cereales?"
    morseText = decoder(naturalText)
    print(morseText)
    print(decoder(morseText))


def decoder(input: str):
    decoded_input = ""
    NATURAL_DIC = {"A": ".—", "N": "—.", "0": "—————",
                   "B": "—...", "Ñ": "——.——", "1": ".————",
                   "C": "—.—.", "O": "———", "2": "..———",
                   "CH": "————", "P": ".——.", "3": "...——",
                   "D": "—..", "Q": "——.—", "4": "....—",
                   "E": ".", "R": ".—.", "5": ".....",
                   "F": "..—.", "S": "...", "6": "—....",
                   "G": "——.", "T": "—", "7": "——...",
                   "H": "....", "U": "..—", "8": "———..",
                   "I": "..", "V": "...—", "9": "————.",
                   "J": ".———", "W": ".——", ".": ".—.—.—",
                   "K": "—.—", "X": "—..—", ",": "——..——",
                   "L": ".—..", "Y": "—.——", "?": "..——..",
                   "M": "——", "Z": "——..", "\"": ".—..—.", "/": "—..—."}

    morseDict = {}
    for key, value in NATURAL_DIC.items():
        morseDict[value] = key
    if re.search(r"[a-zA-Z0-9]", input):
        index = 0
        ch = False
        for character in input.upper():
            if not ch and character != " ":
                print(NATURAL_DIC[character])
                nextIndex = index + 1
                if character == "C" and nextIndex < len(input) and input.upper()[nextIndex] == "H":
                    decoded_input += NATURAL_DIC["CH"]
                    ch = True
                else:
                    decoded_input += NATURAL_DIC[character]
                decoded_input += " "
            else:
                if not ch:
                    decoded_input += " "
                ch = False
            index += 1
    elif "." in input or "-" in input:
        for word in input.split("  "):
            for symbols in word.split(" "):
                if symbols != "":
                    decoded_input += morseDict[symbols]
        decoded_input += " "
    return decoded_input


print(main())
