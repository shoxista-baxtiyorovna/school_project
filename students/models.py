from django.db import models
from django.shortcuts import reverse


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()

    def get_detail_url(self):
        return reverse('students:student_detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:student_delete', args=[self.pk])