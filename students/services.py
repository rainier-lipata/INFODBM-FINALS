from django.db import connection


def search_mentors(topic):

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT *
            FROM viewTopicsMentor
            WHERE TopicName LIKE %s
        """, [f"%{topic}%"])

        columns = [column[0] for column in cursor.description]

        rows = cursor.fetchall()

    return [
        dict(zip(columns, row))
        for row in rows
    ]

def get_student_sessions(student_id):

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT *
            FROM StudentSessions
            WHERE StudentID=%s
        """, [student_id])

        columns = [col[0] for col in cursor.description]

        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]