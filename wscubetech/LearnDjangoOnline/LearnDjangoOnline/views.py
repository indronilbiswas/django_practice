from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import djangoform
from service.models import Service
from news.models import News
from enquiryform.models import Enquiry

def index(request):
    news_data = News.objects.all()
    data = {'news': news_data}
    return render(request, "index.html", data)

def newsdetails(request, slug):
    newsdetails = News.objects.get(new_slug=slug)
    data = {'newsdetails': newsdetails}
    return render(request, 'newsdetails.html', data)

def about(request):
    return render(request, "aboutus.html")

def services(request):
    #service_data = Service.objects.all().order_by('service_title')[:3]
    service_data = Service.objects.all()
    if request.method == "GET":
        st = request.GET.get('servicename')
        if st != None:
            service_data = Service.objects.filter(service_title__icontains=st)
    data = {'service': service_data}
    return render(request, "services.html", data)

def contact(request):
    return render(request, "contact.html")

def enquiry(request):
    m = ''
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('msg')
        fd = Enquiry(name=name, email=email, phone=phone, message=message)
        fd.save()
        m = 'Record Inserted Successfully!!'
    return render(request, "contact.html", {'m': m})

def table(request):
    enquiry_details = Enquiry.objects.all()
    data = {'enquiry_details': enquiry_details}
    return render(request, 'table.html', data)

def addition_get(request):
    result = 0
    data = {}
    if request.method == 'GET':
        try:
            n1 = int(request.GET.get('num1'))
            n2 = int(request.GET.get('num2'))
            result = n1+n2
            data = {'number1':n1, 'number2':n2, 'result':result}
        except:
            pass
    return render(request, "addition_get.html", data)

def addition_post(request):
    result = 0
    data = {}
    if request.method == "POST":
        try:
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            result = n1+n2
            data = {'number1':n1, 'number2':n2, 'result':result}
        except:
            pass
    return render(request, "addition_post.html", data)

def display_name(request):
    data = {}
    if request.method == "POST":
        try:
            fn = request.POST.get('fn')
            ln = request.POST.get('ln')
            fullname = fn + " " + ln
            data = {'firstname':fn, 'lastname':ln, 'fullname':fullname}
            url = "/welcome/?fullname={}".format(fullname)
            return HttpResponseRedirect(url)
        except:
            pass
    return render(request, 'display_name.html')

def welcome(request):
    if request.method == "GET":
        output = request.GET.get('fullname')
    return render(request, "welcome.html", {'output':output})

def welcome_action(request):
        try:
            if request.method == "POST":
                fn = request.POST.get('fn')
                ln = request.POST.get('ln')
                data = fn + " " + ln
                return HttpResponse(data)
        except:
            pass

def django_form(request):
    var = djangoform()
    data = {'form': var}
    try:
        if request.method == "POST":
            fn = request.POST.get("fn")
            ln = request.POST.get("ln")
            fullname = fn + " " + ln
            data = {'form': var, 'fullname': fullname}
    except:
        pass
    return render(request, "djangoform.html", data)

def calculator(request):
    c = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            opr = request.POST.get('opr')
            n2 = eval(request.POST.get('num2'))
            if opr == '+':
                c = n1 + n2
            elif opr == '-':
                c = n1 - n2
            elif opr == '-':
                c = n1 * n2
            elif opr == '/':
                c = n1 / n2
    except:
        c = "Invalid Value.."
    print(c)
    return render(request, 'calculator.html', {'c': c})

def evenodd(request):
    res = ''
    try:
        if request.method == "POST":
            if request.POST.get('num') == "":
                return render(request, 'evenodd.html', {'error': True})
            n = eval(request.POST.get('num'))
            if n % 2 == 0:
                res = 'Even Number'
            else:
                res = 'Odd Number'
    except:
        pass
    return render(request, 'evenodd.html', {'r': res})

def marksheet(request):
    data = {}
    try:
        if request.method == "POST":
            s1 = eval(request.POST.get("mat"))
            s2 = eval(request.POST.get("phy"))
            s3 = eval(request.POST.get("chem"))
            s4 = eval(request.POST.get("eng"))
            s5 = eval(request.POST.get("comp"))
            t = s1 + s2 + s3 + s4 + s5
            p = t*100/500
            if p >= 60:
                d = 'First Division'
            elif p>=45 and p<60:
                d = 'Second Division'
            elif p>=30 and p<45:
                d = 'Third Division'
            else:
                d = 'Fail'
            data = {'total': t, 'per': p, 'div': d}
    except:
        pass
    return render(request, 'marksheet.html', data)

def blog(request):
    return HttpResponse("<b>Hello this is my blog.</b>")

def course(request, cid):
    return HttpResponse(cid)

