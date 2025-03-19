from django.shortcuts import render

# Create your views here.
def IndexView(request):
    return render(request,'index.html')

def loginIndex(request):
    return render(request,'loginSucess.html')