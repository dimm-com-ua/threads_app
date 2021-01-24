from django.contrib import admin

from threads_common.models.common_models.user_space import Author, Thread

admin.site.register(Author)
admin.site.register(Thread)