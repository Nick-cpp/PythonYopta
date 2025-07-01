import os
import re
import random

TRANSLATION_TABLE = {
    "нихуясебе": "elif",
    "ебать": ":",
    "насрисюда": "input",
    "пиздец": "if",
    "нах": "else",
    "бля": "for",
    "в": "in",
    "ебашить": "while",
    "сделать": "def",
    "верни": "return",
    "хуярить": "print",
    "охуенно": "True",
    "непиздеж": "True",
    "пиздеж": "False",
    "и": "and",
    "или": "or",
    "не": "not",
    "сукакласс": "class",
    "похуй": "continue",
    "нахуйвсе": "break",
    "попробуй": "try",
    "поймайпиздец": "except",
    "как": "as",
    "выкиньнах": "raise",
    "глобальныйпиздец": "global",
    "вьебать": "import",
    "из": "from",
    "лямбдахуямбда": "lambda",
    "хуйня": "None",
    "с": "with",
    "подтверди_сука": "assert",
    "выпилитьнахуй": "del",
    "высри": "yield",
    "всегдабля": "finally",
    "длина": "len",
    "жопа": "range",
    "число": "int",
    "строка": "str",
    "список": "list",
    "словарь": "dict",
    "множество": "set",
    "файл": "open",
    "плюсравно": "+=",
    "минусравно": "-=",
    "умножитьравно": "*=",
    "делитьравно": "/=",
    "равно": "==",
    "неравно": "!=",
    "большеравно": ">=",
    "меньшеравно": "<=",
    "это": "=",
    "плюс": "+",
    "минус": "-",
    "умножить": "*",
    "делить": "/",
    "процент": "%",
    "встепени": "**",
    "больше": ">",
    "меньше": "<"
}

def translate_line(line):
    string_matches = re.findall(r'"([^"]*)"', line)
    for i, match in enumerate(string_matches):
        token = f"STRING_TOKEN_{i}_"
        line = line.replace(f'"{match}"', token)

    for mat_word, python_word in TRANSLATION_TABLE.items():
        line = re.sub(r'\b' + re.escape(mat_word) + r'\b', python_word, line)

    for i, match in enumerate(string_matches):
        token = f"STRING_TOKEN_{i}_"
        line = line.replace(token, f'"{match}"')

    return line

def execute_mat_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            mat_code = f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: Файл {filepath} не найден.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла {filepath}: {e}")
        return

    python_code = ""
    for line in mat_code:
        python_code += translate_line(line)

    try:
        exec(python_code)
    except Exception as e:
        print(f"Ошибка при выполнении кода из файла {filepath}: {e}")


def main():
    mat_files = [f for f in os.listdir('.') if f.endswith('.мат')]

    if not mat_files:
        print("В текущей директории не найдено .мат файлов.")
        return

    print("Список .мат файлов:")
    for i, filename in enumerate(mat_files):
        print(f"{i + 1}. {filename}")

    while True:
        try:
            choice = int(input("Введите номер файла для выполнения: "))
            if 1 <= choice <= len(mat_files):
                break
            else:
                print("Неверный номер файла.")
        except ValueError:
            print("Пожалуйста, введите число.")

    selected_file = mat_files[choice - 1]
    print(f"Выполняется файл: {selected_file}")
    execute_mat_file(selected_file)


if __name__ == "__main__":
    main()