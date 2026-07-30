from django.shortcuts import render

def login_page(request):

    return render(
        request,
        "MentorMatchFrontend/login.html"
    )

def student_dashboard(request):
    return render(
        request,
        "MentorMatchFrontend/student-dashboard.html"
    )

def mentor_dashboard(request):
    return render(
        request,
        "MentorMatchFrontend/mentor-dashboard.html"
    )

