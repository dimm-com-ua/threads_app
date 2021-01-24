from django.db import models

from threads_common.models.common_models.user_space import Author


class Thread(models.Model):
    name = models.CharField(max_length=170)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    slug = models.CharField(max_length=64, default='')

    class Meta:
        db_table = 'th_thread'

    def __str__(self):
        return f"{self.name}"


class ThreadItem(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.content}"

    class Meta:
        db_table = 'th_thread_item'
        ordering = ['created_at']
