from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'employee/dashboard.html')

def work(request):
    return render(request, 'employee/work.html')

def request(request):
    return render(request, 'employee/request.html')

def notice(request):
    return render(request, 'employee/notice.html')

def attendance(request):
    return render(request, 'employee/attendance.html')

