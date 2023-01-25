from django.http import HttpResponse
from django.shortcuts import render
from feedback.models import *


def index(request):
    try:
        print("Reached")
        if request.method == 'POST':
            print('POST')
            from_email = request.POST['from_email']
            subject = request.POST['subject']
            queryType = request.POST['queryType']
            content = request.POST['content']
            print(from_email, subject, queryType, content)
            feedback = Feedback(from_email=from_email, queryType=queryType, subject=subject, content=content)
            feedback.save()

            return HttpResponse('review')
    except:
        return render(request, "index.html", {})

    return render(request, "index.html", {})
