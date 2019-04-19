from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.


class Doc(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='docs')
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=40000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    authors_shared = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='docs_shared', blank=True)

    class Meta:
        verbose_name = 'doc'
        verbose_name_plural = 'docs'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('docs:detail', kwargs={'pk': self.pk})
