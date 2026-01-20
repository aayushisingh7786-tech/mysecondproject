from django.db import models

# This class creates a table named 'core_student' in the database
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=50)
    # auto_now_add=True sets the date automatically when created
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
