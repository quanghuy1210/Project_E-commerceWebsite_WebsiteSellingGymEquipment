from django.shortcuts import render

# Create your views here.
def getgioithieuView(request):
    return render(request, 'gioithieu/gioithieu.html') 