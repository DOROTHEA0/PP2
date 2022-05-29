from django.shortcuts import render

def to_main(request):
    return render(request, 'CS/index.html')

def to_meeting(request):
    return render(request, 'CS/meeting.html')

def to_meeting_details(request):
    return render(request, 'CS/meeting-details.html')