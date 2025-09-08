from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        "namaToko" : "Football Shop",
        "nama" : "Vanessa",
        "kelas" : "PBP B"
        }

    return render(request, "main.html", context)