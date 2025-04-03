from turtle import onclick
from django.shortcuts import render
#from jaime.authenticator import verificador
  

# Create your views here.
def menu(request):
    #if onclick:
        
    

    return render(request, 'LoginApp/menu.html')    

def logon(request):
    return render(request, 'LoginApp/success.html')