from django.urls import path
from .views import textbooks

urlpatterns = [
    path('textbooks/<str:course_code>/', textbooks, name='textbooks'), # Added URL pattern for textbooks view.
]