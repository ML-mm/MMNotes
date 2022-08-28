from django.db import models
from author.models import Author
from django.urls import reverse_lazy


# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='notes-pics', default='unknown.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Notes'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse_lazy('notes:home')

    def __str__(self):
        return self.title
