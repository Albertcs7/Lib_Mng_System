from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def add(request):
    if request.method == 'POST':
        book_name = request.POST.get('bname')
        book_auth = request.POST.get('aname')
        shelf = request.POST.get('sno')
        book_cat = request.POST.get('cat')
        a = { "name":book_name, "auth":book_auth, "shel":shelf, "cat":book_cat }
        return render(request, "view.html", {"details": a})
    return render(request, "add.html")


def edit(request):
    return render(request,"edit.html")

def view(request):
    return render(request,"view.html")