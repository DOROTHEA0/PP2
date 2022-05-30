from django.shortcuts import render
# Create your views here.
#from csc.models import Animal, CSCUser

def to_login(request):
    return render(request, 'CS/login.html')


