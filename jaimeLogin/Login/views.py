from django.shortcuts import render
  

# Create your views here.
def menu(request):
    return render(request, 'LoginApp/menu.html')    

def logon(request):
    return render(request, 'LoginApp/success.html')