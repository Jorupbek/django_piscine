import os
import sys
import re
import settings


def check_error(args):
    if len(args) != 2:
        sys.stderr.write("Неверное количество аргументов\n")
        exit(1)
    if not os.path.exists(args[1]):
        sys.stderr.write("Файла не существует\n")
        exit(1)

    file_name, file_extension = os.path.splitext(args[1])
    if file_extension != '.template':
        sys.stderr.write("Неверное расширение файла\n")
        exit(1)

    return file_name


def render():
    args = sys.argv
    file_name = check_error(args)

    with open(args[1], 'r') as f:
        data = f.read()

    data = re.sub(r'{(\w+)}', lambda x: getattr(settings, x.group(1), None), data)

    with open(f'{file_name}.html', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    render()
