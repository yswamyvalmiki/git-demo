from django.shortcuts import render

# Create your views here.
def static_view(request):
    return render(request,'testapp/home.html')