# Create your views here.
#coding=utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from funds.models import Teacher
from funds.models import Department
from funds.models import ProjectType
from funds.models import Project

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
        #save teacher and redirect to teacher_view
        pass
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
        #print type(teacher.name)
        label = teacher.name + ' ' + teacher.title
        #label = teacher.name.encode('utf8') + ' ' + teacher.title.encode('utf8')
        #label = teacher.name
        print label
        result.append({'label': label, 'value': teacher.id})
    #return json.dumps(result)
    #return result
    #print result
    return HttpResponse(json.dumps(result), mimetype='application/json')
    #return HttpResponse(result, mimetype='application/json')

def project_view(request):
    return render_to_response('index.html')

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
            teacherInstance = Teacher.objects.all().get(name=teacher)
            teacher_list.append(teacherInstance)
        addProject = Project.objects.create(name=projectName , project_type = projectType, created_at = startTime,ended_at=endTime)
        for teacher in teacher_list:
            addProject.teachers.add(teacher)
        return HttpResponseRedirect('/project')
    else:
        projectTypes = ProjectType.objects.all()
        return render_to_response('project_add.html',{'project_types':projectTypes})

def project_edit(request):
    return render_to_response('index.html')

def project_delete(request):
    return render_to_response('index.html')

def project_search(request):
    return render_to_response('index.html')

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

