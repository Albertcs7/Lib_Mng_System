from django.shortcuts import render,redirect

def home(request):
    return render(request,"home.html")

def add(request):
    if request.method == 'POST':
        book_name = request.POST.get('bname')
        book_auth = request.POST.get('aname')
        shelf = request.POST.get('shelf')
        book_cat = request.POST.get('cat')
        
        a = [book_name, book_auth, shelf, book_cat]

        return render(request, "view.html", {"details": a})
    return render(request, "add.html")


def edit(request):
    return render(request,"edit.html")

def view(request):
    return render(request,"view.html")