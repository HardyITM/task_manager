from tabnanny import verbose
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'