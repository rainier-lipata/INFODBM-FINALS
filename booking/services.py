from django.db import connection, DatabaseError


def get_pending_requests(mentor_id):

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT *
            FROM viewPendingRequests
            WHERE MentorID = %s
        """, [mentor_id])

        columns = [column[0] for column in cursor.description]

        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


def create_booking(data):

    try:

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

            return {
                "success": True,
                "RequestID": row[0],
                "Message": row[1]
            }

    except DatabaseError as e:

        return {
            "success": False,
            "Message": str(e)
        }

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

def get_mentor_sessions(mentor_id):

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT *
            FROM viewMentorSessions
            WHERE MentorID = %s
        """, [mentor_id])


        columns = [
            column[0]
            for column in cursor.description
        ]


        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

def complete_session(session_id):

    try:

        with connection.cursor() as cursor:

            cursor.execute("""
                EXEC uspCompleteSession
                @session_id=%s
            """, [session_id])

            row = cursor.fetchone()

            return {
                "success": True,
                "Message": row[0]
            }

    except DatabaseError as e:

        return {
            "success": False,
            "Message": str(e)
        }


def get_student_sessions(student_id):

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT *
            FROM viewMentorSessions
            WHERE StudentID = %s
        """, [student_id])


        columns = [
            column[0]
            for column in cursor.description
        ]


        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]