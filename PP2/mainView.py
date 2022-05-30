from django.shortcuts import render
from csc.views import to_login
from csc.models import Animal, CSCUser

def to_main(request):
    if request.POST.get('type') == 'login':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        # set session
        #user = CSCUser(email='bendog@email', password='123', full_name='ben', occupation='dog')
        #user.save()
        users = CSCUser.objects.all()
        print(users)
        return render(request, 'CS/index.html')
    return render(request, 'CS/index.html')
    #animals = Animal.objects.getAll()


def to_meeting(request):
    animals = Animal.objects.all()
    return render(request, 'CS/meetings.html', {'animals': animals})

def to_meeting_details(request):
    return render(request, 'CS/meeting-details.html')