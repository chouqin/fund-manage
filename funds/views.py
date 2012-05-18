# Create your views here.
#coding=utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from funds.models import Teacher
from funds.models import Department
from funds.models import ProjectType
from funds.models import Project
import json
from datetime import datetime
from django.utils.timezone import utc

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
        teacher_title = request.POST['title']
        if 'is_dean' in request.POST.keys():
            teacher_isdean = False
        else:
            teacher_isdean = True
        teacher_department = Department.objects.get(id=request.POST['department'])
        Teacher.objects.create(name=teacher_name , title=teacher_title , is_dean=teacher_isdean , department=teacher_department )
        return HttpResponseRedirect('/teacher')
    else:
        departments = Department.objects.all()
        return render_to_response('teacher_add.html', {'departments': departments})

def teacher_edit(request, teacher_id):
    if request.method == 'POST':
        teacher = get_object_or_404(Teacher, pk=teacher_id)
        teacher.name = request.POST['name']
        teacher.title = request.POST['title']
        if 'is_dean' in request.POST.keys():
            teacher.isdean = False
        else:
            teacher.isdean = True
        teacher.department = Department.objects.get(id=request.POST['department'])
        teacher.save()
        return HttpResponseRedirect('/teacher')
    else:
        departments = Department.objects.all()
        teacher = get_object_or_404(Teacher, pk=teacher_id)
        return render_to_response('teacher_edit.html', {'departments': departments, 'teacher': teacher})

def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    teacher.delete()
    return HttpResponseRedirect('/teacher')

def teacher_search(request, key):
    #print type(key.encode('utf8'))
    teachers = Teacher.objects.filter(name__startswith=key.encode('utf8'))
    #print teachers
    result = []
    for teacher in teachers:
        #label = teacher.name + ' ' + teacher.title
        label = teacher.name
        #print label
        result.append({'label': label, 'value': teacher.id})
    return HttpResponse(json.dumps(result), mimetype='application/json')

def project_index(request):
    projects = Project.objects.filter(ended_at__gte=datetime.utcnow().replace(tzinfo=utc)).order_by('created_at')
    projects.reverse()
    project_list = []
    for project in projects:
        teachers = project.teachers.all()
        project_item = {}
        project_item['name'] = project.name
        project_item['project_type'] = project.project_type.name
        project_item['teachers'] = teachers
        project_item['created_at'] = project.created_at.strftime('%Y-%m')
        project_item['ended_at'] = project.ended_at.strftime('%Y-%m')
        project_list.append(project_item)
    return render_to_response('project_index.html', {'projects': project_list})

def project_add(request):
    if request.method == 'POST':
        #save teacher and redirect to teacher_view
        teacherList = request.POST.getlist('teachers')
        projectName = request.POST['name']
        projectType = ProjectType.objects.get(id=request.POST['project_type'])
        startTime = request.POST['created_at']
        endTime = request.POST['ended_at']
        teacher_list=[]
        for teacher in teacherList:
            teacherInstance = Teacher.objects.get(id=teacher)
            teacher_list.append(teacherInstance)
        addProject = Project.objects.create(name=projectName , project_type = projectType, created_at = startTime,ended_at=endTime)
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
    if request.method == "POST":
        pass
    else:
        return render_to_response('project_add_device.html', {'project_id', project_id})

def project_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    #project = Project.objects.get(id=project_id)
    devices = project.device_set().all()
    businesses = project.business_set().all()
    teachers = project.teachers.all()
    return render_to_response('project_view.html', {'project': project, 'devices': devices, 'businesses': businesses, 'teachers': teachers})

def project_edit(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    #project = Project.objects.get(id=project_id)
    devices = project.device_set().all()
    businesses = project.business_set().all()
    teachers = project.teachers.all()
    return render_to_response('project_edit.html', {'project': project, 'devices': devices, 'businesses': businesses, 'teachers': teachers})


def project_delete(request):
    return render_to_response('index.html')

def project_search(request):
    return render_to_response('index.html')

def device_edit(request, device_id):
    pass


def device_delete(request, device_id):
    pass

def business_edit(request, business_id):
    pass


def business_delete(request, business_id):
    pass


def expense_view(request):
    return render_to_response('index.html')
def expense_add(request): return render_to_response('index.html')

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

