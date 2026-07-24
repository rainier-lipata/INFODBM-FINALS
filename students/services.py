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