from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=170, verbose_name='Автор')
    slug = models.CharField(max_length=64, default='')

    class Meta:
        db_table = 'th_author'

    def __str__(self):
        return f"{self.name}"
