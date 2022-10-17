import sqlite3

# Test av dict


def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}


connection = sqlite3.connect(
    "C:/Users/hadis/source/repos/onion/onion.db", check_same_thread=False)
cursor = connection.cursor()

# Test av dict
connection.row_factory = dict_factory
for row in connection.execute("SELECT * from semesters"):
    print(row)


def read_semesters():
    res = []
    for row in connection.execute("SELECT * from semesters"):
        res.append(row)
    return res


def write_semester(semester, code, name, ects):
    try:
        cursor.execute("INSERT INTO courses VALUES(?,?,?,?)",
                       (code, name, semester, ects))
        connection.commit()
        return True
    except Exception as e:
        raise Exception(str(e))


def read_courses():
    res = []
    for row in connection.execute("SELECT * from courses"):
        res.append(row)
    return res
