from django.db import models
from django.shortcuts import reverse


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def get_detail_url(self):
        return reverse('teachers:teacher_detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:teacher_delete', args=[self.pk])
