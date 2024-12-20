from django.db import models
from django.shortcuts import reverse


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    group_type = models.CharField(max_length=100)

    def get_detail_url(self):
        return reverse('groups:group_detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('groups:group_delete', args=[self.pk])

