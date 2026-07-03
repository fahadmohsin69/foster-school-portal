from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404

from .models import Student


@login_required(login_url="login")
def download_result(request):

    student = get_object_or_404(Student, user=request.user)

    if student.result_pdf:
        return redirect(student.result_pdf.url)

    raise Http404("Result has not been uploaded yet.")

@login_required(login_url="login")
def profile(request):

    student = get_object_or_404(
        Student,
        user=request.user
    )

    context = {
        "student": student,
    }

    return render(
        request,
        "students/profile.html",
        context
    )