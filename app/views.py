from django.http import HttpResponseRedirect
from django.shortcuts import render
from app.forms import EmployeeForm
from app.models import Employee


def create_employee_post(request):
    form = EmployeeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/list")
    return render(request, 'create_employee.html', context={'form': form})


def employee_list(request):
    list_emp = Employee.objects.all()
    return render(request, 'employee_list.html', context={'query_set': list_emp})


def employee_detailed(request,id):
    object_data = Employee.objects.get(id=id)
    return render(request, 'employee_details.html', context={'object': object_data})

# orm
# To get specific object
# print(Employee.objects.get(id=1))

# To get filtered query set
# Employee.objects.filter(salary__gt=100) #__lt,#__gte #__lte
# Employee.objects.filter(name__contains= "thirumala")
# Employee.objects.filter(age)

# to Get all elements
# Employee.objects.all()

# order by ASC
# Employee.objects.all().order_by('salary)
# Employee.objects.all().order_by('-salary')
# second-highest salary
# Employee.objects.all().order_by('-salary')[2]

# To update Specific object
# data = Employee.objects.get(id=2)
# data.salary = 20000
# data.save()

# To delete Sp object
'''
    data = Employee.objects.get(id=2).delete()
    or
    data = Employee.objects.get(id=2)
    data.delete()
'''

# Create object
# object = Employee.objects.create(name='thirumala',salary=1000,address='reddy vari palli',age=20)
# object.save()

# count
# Employee.objects.all().count()

# and or Q
# employees= Employee.objects.filter(ename__startswith='J',esal__lt=15000)
