from django.db import connection


def create_student(data):

    with connection.cursor() as cursor:

        cursor.execute("""
            EXEC uspInsertUser
                @Email=%s,
                @PasswordHash=%s,
                @FirstName=%s,
                @LastName=%s,
                @Role=%s,
                @Course=%s,
                @YearLevel=%s
        """, [
            data["Email"],
            data["PasswordHash"],
            data["FirstName"],
            data["LastName"],
            "Student",
            data["Course"],
            data["YearLevel"]
        ])


def create_mentor(data):

    with connection.cursor() as cursor:

        cursor.execute("""
            EXEC uspInsertUser
                @Email=%s,
                @PasswordHash=%s,
                @FirstName=%s,
                @LastName=%s,
                @Role=%s,
                @Bio=%s,
                @SkillLevel=%s,
                @YearsExperience=%s
        """, [
            data["Email"],
            data["PasswordHash"],
            data["FirstName"],
            data["LastName"],
            "Mentor",
            data["Bio"],
            data["SkillLevel"],
            data["YearsExperience"]
        ])


def update_user(data):

    with connection.cursor() as cursor:

        cursor.execute("""
            EXEC uspUpdateUser
                @UserID=%s,
                @Email=%s,
                @FirstName=%s,
                @LastName=%s
        """, [
            data["UserID"],
            data["Email"],
            data["FirstName"],
            data["LastName"]
        ])


def login_user(email, password):

    with connection.cursor() as cursor:

        cursor.execute("""
            EXEC uspLoginUser
                @Email=%s,
                @PasswordHash=%s
        """, [
            email,
            password
        ])

        row = cursor.fetchone()

    return row