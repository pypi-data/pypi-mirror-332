import sqlite3
from pathlib import Path

from unidecode import unidecode

NAME_DB = Path(__file__).parent / "names.db"

NAME_REPLACERS = ['DE', 'DEL', 'EL', 'LA', 'LAS']


def select_surname(conn, name: str):
    sql = """SELECT apellido from apellidos WHERE apellido=?"""
    cur = conn.cursor()
    res = cur.execute(sql, [unidecode(name).upper()])
    return res.fetchone() is not None


def select_name(conn, name: str):
    processed_name = unidecode(name).upper()
    for rep in NAME_REPLACERS:
        processed_name = processed_name.replace(f' {rep} ', ' ')
    sql = """SELECT nombre from nombres WHERE nombre=?"""
    cur = conn.cursor()
    res = cur.execute(sql, [processed_name])
    return res.fetchone() is not None


def _search(conn, block, selector):
    fullchain = ''
    last_index = 0
    for i in range(len(block)):
        custom_chunk = ' '.join(block[:i + 1])
        if selector(conn, custom_chunk):
            fullchain = custom_chunk
            last_index = i + 1
    return (fullchain, last_index) if last_index else None


def split_name(name_str):
    conn = sqlite3.connect(NAME_DB)
    name_l = name_str.split(' ')
    name, surname1, surname2 = None, None, None
    first_element = 0

    # Name calculation
    name_result = _search(conn, name_l[first_element:], select_name)
    if name_result:
        name, last_index = name_result
        first_element += last_index

    # Surname calculation
    surname_result = _search(conn, name_l[first_element:], select_surname)
    if surname_result:
        surname1, last_index = surname_result
        first_element += last_index

    # The rest is considered the second surname
    surname2 = ' '.join(name_l[first_element:])

    # Move to surname1 if surname1 is not populated
    if not surname1:
        surname1 = surname2
        surname2 = None

    # For surnames that can be confused as compound names, if we haven't got
    # the second surname but we have a compound name, check it.
    if not surname2 and len(name.split(' ')) > 1:
        last_name = name.split(' ')[-1]
        if select_surname(conn, last_name):
            name = ' '.join(name.split(' ')[:-1])
            surname2 = surname1
            surname1 = last_name

    return [name or None, surname1 or None, surname2 or None] # or None to be consistent


if __name__ == '__main__':
    import sys

    name = ' '.join(sys.argv[1:])
    print(split_name(name))
