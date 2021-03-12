from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Susi Sonnenschein',
        'title': 'Der erste Post',
        'content': 'Der Inhalt vom ersten Post',
        'date_posted': '21.03.2021'
    },
    {
        'author': 'Josef Jedermann',
        'title': 'Noch ein Post',
        'content': 'Inhalt der im zweiten Post steht',
        'date_posted': '21.03.2021'
    },
]

def home(request):
    context = {
        'title': 'Startseite',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'Infos',
    }
    return render(request, 'blog/about.html')