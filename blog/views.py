from django.shortcuts import render


def starting_page(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request)


def single_post(request):
    pass

