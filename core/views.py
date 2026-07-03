from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import Student


@login_required(login_url="login")
def dashboard(request):

    student = Student.objects.get(user=request.user)

    context = {
        "student": student
    }

    return render(
        request,
        "dashboard.html",
        context
    )


