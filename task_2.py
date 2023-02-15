import os
from dataclasses import dataclass
import mysql.connector
from prettytable import PrettyTable
from dotenv import load_dotenv

load_dotenv(".env")


@dataclass
class CodeKey:
    code: str
    code_format: str
    dec_key: str or None = None

    def __post_init__(self):
        value_field_code_format = getattr(self, "code_format")
        codekey = ''

        value_field_code = getattr(self, "code")
        if value_field_code_format == 'W26':
            facility_part = str(int(value_field_code[2:4], 16)).zfill(3)
            after_common_part = str(int(value_field_code[4:8], 16)).zfill(5)
            codekey = f"{facility_part},{after_common_part}"
        elif value_field_code_format == 'W34':
            codekey = int(value_field_code[2:10], 16)
        elif value_field_code_format in ('W42', 'W36'):
            codekey = int(value_field_code[2:12], 16)
        elif value_field_code_format in ('W58', 'W58DEC'):
            codekey = int(value_field_code[2:16], 16)
        setattr(self, "dec_key", str(codekey))


def get_codekeys_from_db() -> list[CodeKey]:
    codekeys = []
    with mysql.connector.connect(
            host=os.getenv('HOST'),
            port=os.getenv('WIN_PORT'),
            user=os.getenv('DATABASE_USERNAME'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DATABASE')
    ) as connect:
        with connect.cursor() as cursor:
            cursor.execute("""
                SELECT HEX(CODEKEY), CODEKEY_DISP_FORMAT
                FROM PERSONAL
                WHERE CODEKEY IS NOT NULL""")
            rows = cursor.fetchall()
            for row in rows:
                codekeys.append(CodeKey(
                    code_format=row[1],
                    code=row[0]
                ))
    return codekeys


def create_table(data: list[CodeKey]) -> PrettyTable:
    table = PrettyTable()
    table.field_names = ("CODEKEY", "DEC_CODEKEY", "CODE_FORMAT")
    for key in data:
        table.add_row([key.code, key.dec_key, key.code_format])
    return table


def write_results(data: str) -> None:
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(data)


def main():
    data_from_db = get_codekeys_from_db()
    table = create_table(data_from_db)
    str_table = table.get_string()
    write_results(str_table)


if __name__ == '__main__':
    main()
