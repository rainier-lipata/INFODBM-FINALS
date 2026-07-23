from django.shortcuts import render, redirect
from .db import get_connection


# Create your views here.
def login_view(request):
    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "EXEC uspLoginUser @Email=?, @PasswordHash=?",
            (email, password)
        )

        user = cursor.fetchone()

        print("Email:", email)
        print("Password:", password)
        print("User:", user)

        conn.close()

        if user:
            print("Login Successful")

            request.session["UserID"] = user.UserID
            request.session["FirstName"] = user.FirstName
            request.session["LastName"] = user.LastName
            request.session["Role"] = user.Role

            if user.Role == "Student":
                return redirect("student_dashboard")

            elif user.Role == "Mentor":
                return redirect("mentor_dashboard")

        print("Login Failed")

    return render(request, 'users/login.html')

def student_dashboard(request):
    return render(request, "users/student_dashboard.html")


def mentor_dashboard(request):
    return render(request, "users/mentor_dashboard.html")