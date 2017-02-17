from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    # Создаем словарь, чтобы передать шаблону в качестве содержимого.
    # Заметьте, что ключ boldmessage называется так же как и переменная {{ boldmessage }} в шаблоне!
    context_dict = {'boldmessage': "«I'm crazy. This is crazy. I'm crazy»"}

    # Возвращает ответ, полученный с помощью шаблона, который посылается клиенту.
    # Для упрощения нашей работы мы используем следующую функцию.
    # Заметьте, что первый параметр - это шаблон, который мы хотим использовать.

    return render(request, 'rango/index.html', context_dict)

def about(request):
    return render(request, 'rango/about.html')
    #return HttpResponse('<a href="/rango/">Index</a> <hr> Rango says here is the about page.')
