from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import datetime, time


# Create your views here.
# def index(request):
#     return render(request, 'index.html')

# def main(request: HttpRequest) -> HttpResponse:
#     return HttpResponse("Hey! It's your main view!!")

class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s



def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True,
        'now': datetime.now(),
        'value': datetime.now().time(),  # 👈 Add this line
    })


def first(request):
    return render(request, 'first.html')

def add(request):
    return render(request, 'add.html')

def another(request: HttpRequest) -> HttpResponse:
    return HttpResponse("It's another page!!")

def main_article(request: HttpRequest) -> HttpResponse:
    return HttpResponse('There will be a list with articles')


def uniq_article(request: HttpRequest) -> HttpResponse:
    return HttpResponse('This is a unique answer for a unique value')


def article(request: HttpRequest, article_id: int, name: str = '') -> HttpResponse:
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
            name) if name else "This is unnamed article"))

def regex(request: HttpRequest, text: str) -> HttpResponse:
    return HttpResponse(f"It's regexp with text: {text}")