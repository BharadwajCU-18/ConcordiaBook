from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Textbook

def textbooks(request, course_code):
    # Query the database for textbooks with the given course code and that are available.
    textbooks = Textbook.objects.filter(course_code=course_code, is_available=True)
    # If no textbooks are found, render the page with no textbooks.
    if not textbooks:
        context = {
            'course_code': course_code,
            'textbooks': None,
        }
        return render(request, 'textbookresults.html', context)
    #else render the page with the available textbooks.
    context = {
        'course_code': course_code,
        'textbooks': textbooks,
    }
    return render(request, 'textbookresults.html', context)

