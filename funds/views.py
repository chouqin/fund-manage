# Create your views here.
#coding=utf-8
#from django.http import HttpResponse
from django.shortcuts import render_to_response
#from funds.models import Teacher
from funds.models import Department
#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
from funds.models import Teacher
from funds.models import Department
from django.http import HttpResponseRedirect

def index(request):
    return render_to_response('index.html')

def teacher_view(request):
    departments = []
    departmentList = Department.objects.all()
    for dt in departmentList:
	teacherList = dt.teacher_set.all()
	department_teachers={}
	department_teachers['name']=dt.name
	department_teachers['teachers'] = teacherList
	departments.append(department_teachers)
    return render_to_response('teacher_view.html', {'departments': departments})

def teacher_add(request):
    if request.method == 'POST':
        pass
        #teacher_name = request.POST['name']
        #teacher_title = request.POST['title']
        #teacher_isdean = request.POST['is_dean']
        #teacher_department = request.POST['department']
        #Teacher.objects.creaet(name=teacher_name , title=teacher_title , is_dean=teacher_isdean,department=teacher_department)
	#return HttpResponseRedirect('/teacher/')
        #return HttpResponse(teacher)
    else:
        #departments = []
        departments = Department.objects.all()
        #dts = [{'name': dt.name, 'id': dt.id} for dt in departments]
        #print departments
        #return HttpResponse(departments)
        return render_to_response('teacher_add.html', {'departments': departments})

def teacher_edit(request, teacher_id):
    if request.method == 'POST':
        #save teacher and redirect to teacher_view
        pass
    else:
        #departments = []
        departments = Department.objects.all()
        dts = [{'name': dt.name, 'id': dt.id} for dt in departments]
        teacher = 0
        return render_to_response('teacher_edit.html', {'departments': dts, teacher: teacher})

def teacher_delete(request):
    return render_to_response('index.html')

def teacher_search(request):
    return render_to_response('index.html')

def project_view(request):
    return render_to_response('index.html')

def project_add(request):
    return render_to_response('project_add.html')

def project_edit(request):
    return render_to_response('index.html')

def project_delete(request):
    return render_to_response('index.html')

def project_search(request):
    return render_to_response('index.html')

def expense_view(request):
    return render_to_response('index.html')

def expense_add(request):
    return render_to_response('index.html')

def record_view_all(request):
    return render_to_response('index.html')

def expense_view_department(request):
    return render_to_response('index.html')

def expense_view_teacher(request):
    return render_to_response('index.html')
#def project_edit(request):
    #return render_to_response('index.html')

#def project_delete(request):
    #return render_to_response('index.html')

