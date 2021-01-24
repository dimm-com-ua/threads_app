from django.contrib import admin

from threads_common.models.common_models.user_space import Author
from threads_common.models.threads.thread import Thread, ThreadItem

admin.site.register(Author)
admin.site.register(Thread)
admin.site.register(ThreadItem)