from django.shortcuts import render
from csc.models import Animal, CSCUser
# Create your views here.

def to_login(request):
    return render(request, 'CS/login.html')

def logout(request):
    request.session['uid'] = None
    animals = Animal.objects.all()
    if len(animals) > 4:
        animals = animals[0: 4]
    return render(request, 'CS/index.html', {'animals': animals, 'USER': None})


