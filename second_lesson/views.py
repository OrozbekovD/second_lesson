from django.shortcuts import render


def index(request):
    name = 'Orozbekov Dosoy'
    return render(request, 'index.html', locals())


def index2(request):
    name = 'Mikel Arteta'
    return render(request, 'index2.html', locals())


def index3(request):
    name = 'Leo Messi'
    return render(request, 'index3.html', locals())


def index4(request):
    name = 'Marco Roys'
    return render(request, 'index4.html', locals())


def index5(request):
    name = 'Frodo Beggins'
    return render(request, 'index5.html', locals())
