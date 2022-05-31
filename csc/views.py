from django.shortcuts import render
from csc.models import Animal, CSCUser
# Create your views here.


def to_login(request):
    if request.POST.get('type') == 'register':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        occupation = request.POST.get('occupation')
        try:
            CSCUser.objects.get(email=email)
            return render(request, 'CS/register.html', {'err_msg': '*email is already registered'})
        except CSCUser.DoesNotExist:
            user = CSCUser(email=email, password=password, full_name=name, occupation=occupation)
            user.save()
    return render(request, 'CS/login.html')


def logout(request):
    request.session['uid'] = None
    animals = Animal.objects.all()
    if len(animals) > 4:
        animals = animals[0: 4]
    return render(request, 'CS/index.html', {'animals': animals, 'USER': None})


def to_register(request):
    return render(request, 'CS/register.html')


def to_upload(request):
    user_id = request.session.get('uid')
    try:
        user = CSCUser.objects.get(id=user_id)
    except CSCUser.DoesNotExist:
        user = None
    return render(request, 'CS/upload.html', {'USER': user})


