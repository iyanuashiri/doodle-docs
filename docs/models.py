from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Doc(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=40000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'doc'
        verbose_name_plural = 'docs'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('docs:detail', kwargs={'pk': self.pk})
