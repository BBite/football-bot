from typing import Dict, List, Tuple

import sqlite3

# conn = sqlite3.connect(os.path.join("db", r"C:\mpr\football_bot\utils\db_api\db\football.db"))
conn = sqlite3.connect(r"C:\mpr\football_bot\utils\db_api\db\football.db")
cursor = conn.cursor()


def insert(table: str, column_values: Dict):
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
    cursor.executemany(
        f"INSERT OR REPLACE INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


def is_in_table(table: str, column_values: Dict) -> bool:
    cursor.executescript(
        f'''
        SELECT COUNT(id)
        FROM {table}
        WHERE team_1 = "Шальке" and team_2 = "Фрайбург" and liga = "b" and lang = "uk"
        '''
    )
    return bool(cursor.fetchall())


def insert_matches(table: str, column_values: Dict):
    if not is_in_table(table, column_values):
        cursor.execute('SELECT MAX(id) FROM matches')
        max_id = cursor.fetchone()[0]
        if not max_id:
            max_id = 0
        column_values['id'] = max_id + 1
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * (len(column_values.keys())))
    cursor.executemany(
        f"INSERT OR REPLACE INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


def update(table: str, id: int, column_values: Dict):
    update_values = list()
    for column, value in column_values.items():
        update_values.append(f'{column} = "{value}"')
    update_values = ', '.join(update_values)
    cursor.execute(
        f"UPDATE {table} "
        f"SET {update_values} "
        f"WHERE id = {id}")
    conn.commit()


def get_lang(id: int) -> str:
    cursor.execute(f"SELECT * FROM users WHERE id = {id}")
    user = cursor.fetchone()
    return user[3]


def remade_matches():
    cursor.executescript('''
    DROP TABLE matches;
   create table matches
(
    id          integer UNIQUE NOT NULL,
    time        timestamp,
    team_1      varchar(100)   NOT NULL,
    team_2      varchar(100)   NOT NULL,
    liga        varchar(5)     NOT NULL,
    lang        varchar(2)     NOT NULL,
    is_canceled boolean,
    primary key (team_1, team_2, lang)
)
    ''')


def fetchall(table: str, columns: List[str]) -> List[Dict]:
    columns_joined = ", ".join(columns)
    cursor.execute(f"SELECT {columns_joined} FROM {table}")
    rows = cursor.fetchall()
    result = list()
    for row in rows:
        dict_row = dict()
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


def get_cursor():
    return cursor


def _init_db():
    """Инициализирует БД"""
    with open(r"C:\mpr\football_bot\utils\db_api\createdb.sql", "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()


def check_db_exists():
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='users'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


check_db_exists()
