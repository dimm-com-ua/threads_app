from django.shortcuts import render

from threads_common.models.common_models.user_space import Author
from threads_common.models.threads.thread import Thread


def frontend(request):
    threads = Thread.objects.all()
    authors = Author.objects.all()

    data = {
        'threads': threads,
        'authors': authors
    }

    return render(request, 'threads_ui/template.html', data)
