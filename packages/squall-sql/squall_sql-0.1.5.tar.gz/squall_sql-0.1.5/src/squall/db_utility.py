# db_utility.py

import sqlite3

from pathlib import Path


def get_table_names(db_path: Path) -> list[str]:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    return table_names


def get_data_from_table(db_path: Path, table_name: str) -> list[tuple]:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    sql = f"SELECT * FROM {table_name} LIMIT 1000;"
    cursor.execute(sql)

    # Get column names
    column_names = tuple([description[0] for description in cursor.description])

    data = cursor.fetchall()
    data.insert(0, column_names)
    return data


def get_schema(db_path: Path) -> dict[str, dict]:
    sql = "SELECT * FROM sqlite_master;"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    tables: dict[str, dict] = {}
    for item in result:
        _, table_name, _, _, schema = item

        if schema is None:
            continue

        if "CREATE TABLE" in schema:
            fields = parse_out_fields(schema)
            tables[table_name] = {}
            tables[table_name]["Schema"] = schema
            tables[table_name]["Columns"] = fields

    return tables


def parse_out_fields(schema: str) -> dict[str, dict[str, str]]:
    fields: dict[str, dict] = {}
    schema = schema.replace("\t", "")

    if "CREATE TABLE" in schema and "(" in schema:
        location = schema.find("(")
        lines = [schema[location:]]

    for line in lines:
        line = line.strip()

        if not line_is_table_field(line):
            continue

        field_schema = parse_field_schema(line)

        if line.endswith(",") and line.count(",") == 1:
            parse_fields(line, fields, field_schema)
        elif line.count(",") == 0:
            parse_fields(line, fields, field_schema)
        elif (
            (line.startswith("(") and line.count(",") >= 1)
            or line.endswith(")")
            and line.count(",") >= 1
        ):
            for sub_line in line.split(","):
                sub_line = sub_line.strip()
                if not line_is_table_field(sub_line):
                    continue
                if sub_line:
                    field_schema = parse_field_schema(sub_line)
                    parse_fields(sub_line, fields, field_schema)
        elif line.endswith(","):
            parse_fields(line, fields, field_schema)
        else:
            print(line)
            raise NotImplementedError

    return fields


def line_is_table_field(line: str) -> bool:
    if not line:
        return False

    if len(line) == 1:
        return False

    if line.startswith("FOREIGN KEY") or line.startswith("PRIMARY KEY"):
        return False

    if line.startswith("ON DELETE"):
        return False

    if line.startswith("CONSTRAINT "):
        return False

    return True


def parse_fields(
    line: str, fields: dict, field_schema: str
) -> dict[str, dict[str, str]]:
    # Clean line
    line = line.replace("[", "")
    line = line.replace("]", "")
    line = line.replace("(", "")
    line = line.replace(")", "")
    line = line.replace(",", "")
    # End of field
    try:
        field_name, field_type, *_ = line.split()
    except ValueError:
        field_name = line
        field_type = line

    field_name = field_name.strip()
    if field_name in fields:
        # do not update the fields a second time
        return fields
    fields[field_name] = {}
    fields[field_name]["Type"] = field_type
    fields[field_name]["Schema"] = field_schema
    return fields


def parse_field_schema(line: str) -> str:
    field_schema = line.strip()
    field_schema = field_schema.replace(",", "")
    if field_schema.startswith("("):
        field_schema = field_schema.replace("(", "")
    if ") WITHOUT" in line:
        field_schema = field_schema[: field_schema.find(") WITHOUT")]
    field_name, *parts = field_schema.split()
    field_name = field_name.replace("[", '"')
    field_name = field_name.replace("]", '"')
    field_name = field_name.replace("(", "")
    field_name = field_name.replace(")", "")
    field_name = field_name.replace('"', "")
    field_schema = line.strip()
    field_schema = f'"{field_name}" {" ".join(parts)}'
    field_schema = field_schema.replace(",", "")
    return field_schema


def get_primary_keys(db_path: Path, table_name: str) -> list[tuple[str]]:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = f'SELECT l.name FROM pragma_table_info("{table_name}") as l WHERE l.pk <> 0;'
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_column_types(db_path: Path, table_name: str) -> dict[str, str]:
    """
    Get all the column data types and return it as a dictionary
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = f"PRAGMA table_info({table_name});"
    cursor.execute(sql)
    result = cursor.fetchall()
    return {key: value for _, key, value, *_ in result}


def run_sql(db_path: Path, sql: str) -> list[tuple]:
    """
    Runs the user-provided SQL. This may be a select, update, drop
    or any other SQL command

    If there are results, they will be returned
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql)
    headers = [name[0] for name in cursor.description]
    result = cursor.fetchall()
    result.insert(0, tuple(headers))
    conn.commit()
    return result


def run_row_update(
    db_path: Path, sql: str, column_values: list, primary_key_value
) -> None:
    """
    Update a row in the database using the supplied SQL command(s)
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql, (*column_values, primary_key_value))
    conn.commit()
