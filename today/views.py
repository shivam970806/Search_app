#from django.db.models.fields.related import ForeignKey
from .models import Emp, Benefit
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse, response
from django.db.models import Q
# Create your views here.

def add_employee(request):
    if request.method == 'POST':
        fn = request.POST.get('first_name')
        print(fn)
        ln = request.POST.get('last_name')
        print(ln)
        e = request.POST.get('InputEmail')
        print(e)
        des = request.POST.get('designation')
        print(des)
        bt = request.POST.get('benefit')
        print(bt)
        ba = request.POST.get('ben_amnt')
        print(ba)
        emp = Emp.objects.create(first_name=fn,last_name=ln,email=e,designation=des)
        Benefit.objects.create(benefit_type=bt,benefit_ammount=ba, Employee=emp)
        messages.info(request, 'Huurry! Your data saved successfully')
        return render(request, 'add_emp.html',{'msg':'employee!added'})
    else:
        return render(request, 'add_emp.html')

def emp_detail(request):
    if 'q' in request.GET:
        q=request.GET['q']
        e_dtls=Benefit.objects.filter(Q(benefit_type__icontains=q) | Q(benefit_ammount__icontains=q) | Q(Employee__first_name__icontains=q) | Q(Employee__last_name__icontains=q))

    else:
    #Employee foregin key h jo Benefit table me Emp tble ki all access kr raha h
        e_dtls = Benefit.objects.select_related('Employee').all()
    return render(request,'emp_detail.html',{'e_dtls':e_dtls})

