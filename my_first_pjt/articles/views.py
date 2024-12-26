from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")



def hello(request):
    name = "재석"
    tags = ["python", "django", "html", "css"]
    books = ["해변의 카프카", "코스모스", "백설공주", "어린왕자", "그리스인 조르바"]

    context = {
        "name": name,
        "tags": tags,
        "books": books,
    }
    return render(request, "hello.html", context)

def data_throw(request):
    return render(request, "data_throw.html")

def data_catch(request):
    message = request.GET.get("message")
    context = {"message" : message}
    return render(request, "data_catch.html", context)

