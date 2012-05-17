# Create your views here.
#coding=utf-8
import time
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from funds.models import Teacher
from funds.models import Department
from funds.models import ProjectType
from funds.models import Project
import json
from datetime import datetime

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
        teacher_name = request.POST['name']
        teacjjher_title = request.POST['title']
        if 'is_dean' in request.POST.keys():
            teacher_isdean = True
        else:
#<<<<<<< HEAD
             #teacher_isdean = True
        #teacher_department = Department.objects.get(id=request.POST['department'])
        #Teacher.objects.create(name=teacher_name , title=teacher_title ,is_dean=teacher_isdean , department=teacher_department )
#=======
            teacher_isdean = False
        teacher_department = Department.objects.get(id=request.POST['department'])
        Teacher.objects.create(name=teacher_name , title=teacher_title , is_dean=teacher_isdean , department=teacher_department )
#>>>>>>> 330c5a0d2cb1911d6966f56d77de18a446388b77
        return HttpResponseRedirect('/teacher')
    else:
        departments = Department.objects.all()
        return render_to_response('teacher_add.html', {'departments': departments})

def teacher_edit(request, teacher_id):
    if request.method == 'POST':
        teacherName = request.POST['name']
        teacherTitle = request.POST['title']
        if 'is_dean' in request.POST:
            teacherIsDean = True
        else:
            teacherIsDean = False
        teacherDepartment = Department.objects.get(id=request.POST['department'])
        Teacher.objects.filter(id=teacher_id).update(name = teacherName , title = teacherTitle ,is_dean = teacherIsDean ,
        department = teacherDepartment)
        return HttpResponseRedirect('/teacher')
    else:
        departments = []
        departments = Department.objects.all()
        teacher = Teacher.objects.get(id=teacher_id)
        return render_to_response('teacher_edit.html', {'departments': departments, 'teacher': teacher})

def teacher_delete(request):
    return render_to_response('index.html')

def teacher_search(request, key):
    print type(key.encode('utf8'))
    teachers = Teacher.objects.filter(name__startswith=key.encode('utf8'))
    print teachers
    result = []
    for teacher in teachers:
        label = teacher.name + ' ' + teacher.title
        print label
        result.append({'label': label, 'value': teacher.id})
    return HttpResponse(json.dumps(result), mimetype='application/json')

#<<<<<<< HEAD
def project_view(request):
    projectList = Project.objects.order_by("created_at")
    projects = []
    for projectInList in projectList:
        project = {}
        project['project'] = projectInList
        project['teachers'] = projectInList.teachers.all()
        projects.append(project)
    return render_to_response('project_view_for_test.html',{'projects':projects})
   # return HttpResponse(projectList[0].ended_at)
#=======
def project_index(request):
    projects = Project.objects.filter(ended_at__gte=datetime.now()).order_by('create_at')
    projects.reverse()
    return render_to_response('project_index.html', {'projects': projects})
#>>>>>>> dbb09a6f48a3c66585860cb8f7cf8a9bd11544bc

def project_add(request):
    if request.method == 'POST':
#<<<<<<< HEAD
#=======
        ##save teacher and redirect to teacher_view
#>>>>>>> 330c5a0d2cb1911d6966f56d77de18a446388b77
        teacherList = request.POST.getlist('teachers')
        projectName = request.POST['name']
        projectType = ProjectType.objects.get(id=request.POST['project_type'])
        startTime = request.POST['created_at']
        endTime = request.POST['ended_at']
        teacher_list=[]
        for teacher in teacherList:
            teacherInstance = Teacher.objects.get(id=teacher)
            teacher_list.append(teacherInstance)
#<<<<<<< HEAD
            #addProject = Project.objects.create(name=projectName , project_type = projectType, created_at = startTime,ended_at=endTime)
#=======
        addProject = Project.objects.create(name=projectName , project_type = projectType, created_at = startTime,ended_at=endTime)
#>>>>>>> 330c5a0d2cb1911d6966f56d77de18a446388b77
        for teacher in teacher_list:
            addProject.teachers.add(teacher)
        addProject.save()
        submit_type = request.POST['submit_type']
        if submit_type == 'save':
            return HttpResponseRedirect('/project')
        else:
            if submit_type == 'add_device':
                return HttpResponseRedirect('/project/add/device/' + str(addProject.id))
            else:
                return HttpResponseRedirect('/project/add/business/' + str(addProject.id))
    else:
        projectTypes = ProjectType.objects.all()
        return render_to_response('project_add.html',{'project_types':projectTypes})

def project_add_device(request, project_id):
	if request.method == 'POST':
		device_name = request.POST['name']
		device_specification = request.POST['specification']
		device_maker = request.POST['maker']
		if 'is_import' in request.POST.keys():
			device_isImport = True
		else:
			device_isImport = False
		device_price = request.POST['price']
		device_amount = request.POST['amount']
		device_remain_amount = device_amount
		device_position = request.POST['position']
		device_usage = request.POST['usage']
		device_year = request.POST['year']
		device_project = Project.objects.get(id = project_id)
		Device.objects.create( name = device_name, specification = device_specification, maker = device_maker, is_import = device_isImport, price = device_price, amount = device.amount, remain_amount = device_remain_amount, position = device_position, usage = device_usage, year = device_year, project = device_project)
		return render_to_response('project_add_device.html')
	else:
		currentTime = time.localtime()
        years = range(-4,6)
        years = [ year + currentTime.tm_year for year in years ]
        return render_to_response('project_add_device.html',{'years':years,})

def project_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    #project = Project.objects.get(id=project_id)
    devices = project.device_set().all()
    businesses = project.business_set().all()
    return render_to_response('project_view.html', {'project': project, 'devices': devices, 'business': businesses})

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

