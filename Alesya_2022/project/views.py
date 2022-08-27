from django.shortcuts import render #отдавать


def project(request):
    return render(request, 'project.html')

