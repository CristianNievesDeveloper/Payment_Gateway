from django.shortcuts import render

# Create your views here.
def account_login(request):
    return render(request, "account/login.html")

def account_logout(request):
    return render(request, "account/logout.html")




