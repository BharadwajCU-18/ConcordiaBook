from django.db import models

class Textbook(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    edition = models.CharField(max_length=255, blank=True, null=True) 
    author = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    condition = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.title} ({self.course_code})" # Return the title and course code of the textbook.