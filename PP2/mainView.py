from django.shortcuts import render

import csc.models
from csc.models import Animal, CSCUser

def to_main(request):
    if request.POST.get('type') == 'login':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        # set session
        try:
            user = CSCUser.objects.get(email=email)
        except csc.models.CSCUser.DoesNotExist:
            print(None)
            return render(request, 'CS/login.html')
        if user.password != password:
            return render(request, 'CS/login.html')
        request.session['uid'] = user.id

    animals = Animal.objects.all()
    user_id = request.session.get('uid')
    try:
        user = CSCUser.objects.get(id=user_id)
    except csc.models.CSCUser.DoesNotExist:
        user = None
    if len(animals) > 4:
        animals = animals[0: 4]
    return render(request, 'CS/index.html', {'animals': animals, 'USER': user})


def to_meeting(request):
    user_id = request.session.get('uid')
    try:
        user = CSCUser.objects.get(id=user_id)
    except csc.models.CSCUser.DoesNotExist:
        user = None

    if request.POST.get('type') == 'upload':
        if user is None:
            return render(request, 'CS/login.html')
        animal = Animal()
        animal.discoverer = user
        animal.animal_name = request.POST.get('aname')
        animal.picture = request.FILES.get('picture')
        animal.description = request.POST.get('description')
        animal.catgories = request.POST.get('cate')
        animal.location = request.POST.get('location')
        animal.save()

    animals = Animal.objects.all()

    return render(request, 'CS/meetings.html', {'animals': animals, 'USER': user})


def to_meeting_details(request, aid):
    animal = Animal.objects.get(id=aid)
    user_id = request.session.get('uid')
    try:
        user = CSCUser.objects.get(id=user_id)
    except csc.models.CSCUser.DoesNotExist:
        user = None
    return render(request, 'CS/meeting-details.html', {'animal': animal, 'USER': user})