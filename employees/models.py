from django.db import models


class Employee(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    COURSE_CHOICES = [
        ('MCA', 'MCA'),
        ('BCA', 'BCA'),
        ('BSC', 'BSC'),
        ('BE', 'BE'),
        ('BTECH', 'B.Tech'),
    ]

    DESIGNATION_CHOICES = [
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
        ('Tester', 'Tester'),
        ('Intern', 'Intern'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)

    def __str__(self):
        return self.name
