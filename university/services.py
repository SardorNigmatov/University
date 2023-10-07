from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from university_faculty""")
        faculties = dictfetchall(cursor)
        return faculties


def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from university_kafedra""")
        kafedra = dictfetchall(cursor)
        return kafedra


def get_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT university_group.id, university_group.name, university_faculty.name as faculty
         from university_group left join university_faculty on university_group.faculty_id = university_faculty.id
         """)
        groups = dictfetchall(cursor)
        return groups


def get_subject():
        with closing(connection.cursor()) as cursor:
            cursor.execute("""SELECT * from university_subject """)
            subjects = dictfetchall(cursor)
            return subjects

def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT university_teacher.id, university_teacher.first_name, university_teacher.last_name,
        university_teacher.age, university_kafedra.name as kafedra_name, university_subject.name as subject_name from 
        university_teacher left join university_kafedra on university_teacher.kafedra_id = university_kafedra.id
        left join university_subject on university_teacher.subject_id = university_subject.id""")
        teachers = dictfetchall(cursor)
        return teachers


def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT university_student.id, university_student.first_name, university_student.last_name, 
        university_student.age, 
        university_group.name as group_name, university_student.image as image  from university_student
        left join university_group on university_student.group_id = university_group.id""")
        student = dictfetchall(cursor)
        return student


