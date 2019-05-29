from django.shortcuts import render


posts = [
    {
        'author': 'Ahmed Hosam',
        'title': 'First Title',
        'content': 'First Content',
        'date_posted': '2002-10-14'
    },
    {
        'author': 'Mohammed Hosam',
        'title': 'Second Title',
        'content': 'Second Content',
        'date_posted': '2009-12-05'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})