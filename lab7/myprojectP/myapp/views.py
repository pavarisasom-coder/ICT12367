from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>ICT12367 SPU</h1>")

# Create your views here.
def about(request):
    return HttpResponse("<h1>เกี่ยวกับเรา</h1>")

def form(request):
    return render(request, 'form.html')

def contact(request):
    return HttpResponse("<h1>ติดต่อ</h1><p>รหัสนักศึกษา: ICT12367</p><p>ชื่อ: นายสมชาย ใจดี</p>")