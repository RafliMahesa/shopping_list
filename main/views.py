from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Muhammad Rafli Mahesa',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
