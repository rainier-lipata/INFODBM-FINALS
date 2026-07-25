from django.db import connection, DatabaseError


def get_pending_requests(request_id):

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT *
            FROM viewPendingRequests
        """)

        columns = [column[0] for column in cursor.description]

        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


def create_booking(data):

    with connection.cursor() as cursor:

        cursor.execute("""
            EXEC uspCreateBookingRequest
                @student_id=%s,
                @mentor_id=%s,
                @availability_id=%s,
                @topic_id=%s,
                @message=%s
        """, [

            data["StudentID"],
            data["MentorID"],
            data["AvailabilityID"],
            data["TopicID"],
            data["Message"]

        ])

        row = cursor.fetchone()

    return row

def approve_booking(request_id):
    try:

        with connection.cursor() as cursor:

            cursor.execute("""
                   EXEC uspApproveBookingRequest
                       @request_id=%s
               """, [request_id])

            row = cursor.fetchone()

            return {
                "success": True,
                "SessionID": row[0],
                "Message": row[1]
            }

    except DatabaseError as e:

        return {
            "success": False,
            "Message": str(e)
        }