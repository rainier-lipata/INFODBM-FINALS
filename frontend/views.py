from django.shortcuts import render

def login_page(request):

    return render(
        request,
        "MentorMatchFrontend/login.html"
    )
# Create your views here.
