from django.db import connection


def get_mentor_schedule(mentor_id):

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT *
            FROM viewMentorSessions
            WHERE MentorID=%s
        """, [mentor_id])

        columns = [col[0] for col in cursor.description]

        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

def get_mentor_dashboard(mentor_id):

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT
                COUNT(*) AS TotalSessions,
                SUM(CASE WHEN Status='Scheduled' THEN 1 ELSE 0 END) AS ScheduledSessions,
                SUM(CASE WHEN Status='Completed' THEN 1 ELSE 0 END) AS CompletedSessions
            FROM Sessions
            WHERE MentorID=%s
        """, [mentor_id])

        row = cursor.fetchone()

        return {
            "TotalSessions": row[0],
            "ScheduledSessions": row[1] or 0,
            "CompletedSessions": row[2] or 0
        }

def get_mentor_availability(mentor_id):

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT
                AvailabilityID,
                AvailableDate,
                StartTime,
                EndTime,
                IsBooked
            FROM Availability
            WHERE MentorID=%s
            ORDER BY AvailableDate, StartTime
        """, [mentor_id])

        columns = [column[0] for column in cursor.description]

        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

def update_availability(availability_id, data):

    with connection.cursor() as cursor:

        cursor.execute("""
            EXEC usp_UpdateAvailability
                @AvailabilityID=%s,
                @AvailableDate=%s,
                @StartTime=%s,
                @EndTime=%s
        """, [
            availability_id,
            data["AvailableDate"],
            data["StartTime"],
            data["EndTime"]
        ])

def assign_mentor_topic(data):

    with connection.cursor() as cursor:

        cursor.execute("""
            EXEC uspAssignMentorTopic
                @mentor_id=%s,
                @topic_id=%s
        """, [
            data["MentorID"],
            data["TopicID"]
        ])

        row = cursor.fetchone()

        if row:
            return row[0]

        return "Topic assigned successfully!"