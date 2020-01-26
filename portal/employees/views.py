from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Employee
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import pprint

# Create your views here.
def index(request):
    queryset_list = Employee.objects.all()
    if (request.POST):

        if request.POST['name']:
            if queryset_list.filter(name=request.POST['name']).exists():
                    messages.error(request, 'Name already exists')
                    return redirect('/')
        else:
            messages.error(request, 'Name is mandatory')
            return redirect('/')

        if request.POST['pan']:
            if queryset_list.filter(pan=request.POST['pan']).exists():
                    messages.error(request, 'PAN Number already exists')
                    return redirect('')
        else:
            messages.error(request, 'PAN Number is mandatory')
            return redirect('/')

        if not request.POST['age']:
            messages.error(request, 'Age is mandatory')
            return redirect('/')

        if 'gender' not in request.POST:
            messages.error(request, 'Gender is mandatory')
            return redirect('/')

        if not request.POST['email']:
            messages.error(request, 'Email ID is mandatory')
            return redirect('/')

        if 'city' not in request.POST:
            messages.error(request, 'City is mandatory')
            return redirect('/')

        insert_data = {
            'name' : request.POST['name'],
            'pan' : request.POST['pan'],
            'age' : request.POST['age'],
            'gender' : request.POST['gender'],
            'email' : request.POST['email'],
            'city' : request.POST['city'],
        }
        
        try:
            new_emp = Employee(**insert_data)
            new_emp.save()
            print ("Employee Inserted")
        except :
            print ('ERROR: Employee not insert')
            pprint.pprint(insert_data)
            pass

    else:
        # Delete Employee
        if 'delete_employee' in request.GET:
            if request.GET['delete_employee']:
                Employee.objects.get(id=request.GET['delete_employee']).delete()

        # Name
        if 'name' in request.GET:
            name = request.GET['name']
            if name:
                queryset_list = queryset_list.filter(name__icontains=name)

        # PAN
        if 'pan' in request.GET:
            pan = request.GET['pan']
            if pan:
                queryset_list = queryset_list.filter(pan__icontains=pan)

        # Age
        if 'age' in request.GET:
            age = request.GET['age']
            if age:
                queryset_list = queryset_list.filter(age=age)

        # Gender
        if 'gender' in request.GET:
            gender = request.GET['gender']
            if gender:
                queryset_list = queryset_list.filter(gender__icontains=gender)
        
        # Email
        if 'email' in request.GET:
            email = request.GET['email']
            if email:
                queryset_list = queryset_list.filter(email__icontains=email)

        # City
        if 'city' in request.GET:
            city = request.GET['city']
            if city:
                queryset_list = queryset_list.filter(city__icontains=city)


        # Get Employee
        if 'get_employee' in request.GET:
            if request.GET['get_employee']:
                request.GET = Employee.objects.all().filter(id=request.GET['get_employee']).values()[0]

    gender_choices = {
        'M' : 'Male',
        'F' : 'Female'
    }
    city_choices = {
        'DL' : 'Delhi',
        'FB' : 'Faridabad',
        'GN' : 'Gurgaon',
        'ND' : 'Noida',
        'GZ' : 'Ghaziabad'
    }
    
    context = []
    for emp in queryset_list.values():
        emp['gender'] = gender_choices[emp['gender']]
        emp['city'] = city_choices[emp['city']]
        context.append(emp)

    # Pagination
    paginator = Paginator(context,10)
    page = request.GET.get('page')
    context = paginator.get_page(page)
    
    data = {
        'employees' : context,
        'gender_choices' : gender_choices,
        'city_choices' : city_choices,
        'values' : request.GET
    }
    return render(request, 'index.html', data)