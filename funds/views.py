#coding=utf-8
import time
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from funds.models import Teacher
from funds.models import Department
from funds.models import ProjectType
from funds.models import Project , Business
import json
from funds.models import Device
from funds.models import DeviceExpense, BusinessExpense
from datetime import datetime
from django.utils.timezone import utc
from django.contrib import auth
from django.contrib.auth.models import User
import re

def login_view(request):
    if request.method == 'POST':
        if not request.user.is_authenticated():
            user_name = request.POST.get('user_name','')
            pass_word = request.POST.get('password','')
            user = auth.authenticate(username=user_name,password=pass_word)
            if user is not None and user.is_active:
                auth.login(request,user)
                return render_to_response('index.html')
            else:
                error_message = "无效的用户或者密码错误"
                return render_to_response('login_view.html',{'error_message':error_message,})
        return HttpResponseRedirect('/home')
    else:
        if not request.user.is_authenticated():
            return render_to_response('login_view.html')
        else:
            return HttpResponseRedirect('/home')

@login_required
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')

@login_required
def accountInfo(request):
    if request.method == 'POST':
        return render_to_response('setPassword.html')
    else:
        return render_to_response('accountInfo.html',{'username':request.user.username,'email':request.user.email})



@login_required
def setPassword(request):
    if request.method == 'POST':
        oldPassword = request.POST.get('oldPassword','')
        newPassword = request.POST.get('newPassword','')
        error_message = None
        if oldPassword == newPassword:
            error_message = "新密码与旧密码相同"
            return render_to_response('setPassword.html',{'username':request.user.username,'error_message':error_message})
        elif newPassword == None :
            error_message = "密码不能为空"
            return render_to_response('setPassword.html',{'username':request.user.username,'error_message':error_message})
        elif len(newPassword) < 6:
            error_message = "密码长度必须大于6位"
            return render_to_response('setPassword.html',{'username':request.user.username,'error_message':error_message})
        else:
           user = User.objects.get(username__exact=request.user.username)
           user.set_password(newPassword)
           user.save()
        return render_to_response('accountInfo.html',{'username':request.user.username,'email':request.user.email})
    else:
        return render_to_response('setPassword.html',{'username':request.user.username,})

@login_required
def index(request):
    return render_to_response('index.html')

@login_required
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


@login_required
def teacher_add(request):
    if request.method == 'POST':
        teacher_name = request.POST['name']
        teacher_title = request.POST['title']
        if 'is_dean' in request.POST.keys():
            teacher_isdean = True
        else:
            teacher_isdean = False
        teacher_department = Department.objects.get(id=request.POST['department'])
        Teacher.objects.create(name=teacher_name , title=teacher_title , is_dean=teacher_isdean , department=teacher_department )
        return HttpResponseRedirect('/teacher')
    else:
        departments = Department.objects.all()
        return render_to_response('teacher_add.html', {'departments': departments})


@login_required
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


@login_required
def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    teacher.delete()
    return HttpResponseRedirect('/teacher')

@login_required
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



@login_required
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
        project_item['id'] = project.id
        project_list.append(project_item)
    return render_to_response('project_index.html', {'projects': project_list})



@login_required
def project_add(request):
    if request.method == 'POST':
        teacherList = request.POST.getlist('teachers')
        projectName = request.POST['name']
        projectType = ProjectType.objects.get(id=request.POST['project_type'])
        startTime = request.POST['created_at']
        endTime = request.POST['ended_at']
        print type(startTime)
        p = re.compile(r'\d{4}\-\d{1,2}-\d{1,2}')
        if not p.match(startTime):
            error_message = "请按年-月-日的格式正确输入起始日期"
            projectTypes = ProjectType.objects.all()
            return render_to_response('project_add.html', {'project_types': projectTypes, 'error_message': error_message})
        if not p.match(endTime):
            error_message = "请按年-月-日的格式正确输入终止日期"
            projectTypes = ProjectType.objects.all()
            return render_to_response('project_add.html', {'project_types': projectTypes, 'error_message': error_message})
        if startTime > endTime:
            error_message = "起始日期不能大于终止日期, 请重新输入"
            projectTypes = ProjectType.objects.all()
            return render_to_response('project_add.html', {'project_types': projectTypes, 'error_message': error_message})
        teacher_list=[]
        for teacher in teacherList:
            if teacher == '':
                teacherInstance = Teacher.objects.get(id=teacher)
                teacher_list.append(teacherInstance)
        addProject = Project.objects.create(name=projectName , project_type = projectType, created_at = startTime,ended_at=endTime)
        for teacher in teacher_list:
            addProject.teachers.add(teacher)
        addProject.save()
        submit_type = request.POST['submit_type']
        if submit_type == 'save':
            return HttpResponseRedirect('/project/' + str(addProject.id))
        else:
            if submit_type == 'add_device':
                return HttpResponseRedirect('/project/add/device/' + str(addProject.id))
            else:
                return HttpResponseRedirect('/project/add/business/' + str(addProject.id))
    else:
        projectTypes = ProjectType.objects.all()
        return render_to_response('project_add.html',{'project_types':projectTypes})


@login_required
def project_add_device(request, project_id):
    if request.method == "POST":
        name = request.POST['name']
        specification = request.POST['specification']
        maker = request.POST['maker']
        if 'is_import' in request.POST.keys():
            is_import = True
        else:
            is_import = False
        price = request.POST['price']
        amount = request.POST['amount']
        position = request.POST['position']
        remain_amount = amount
        usage = request.POST['usage']
        month_to_add = "-12-31 00:00"
        year = request.POST['year']
        year += month_to_add
        project = get_object_or_404(Project, pk=project_id)
        Device.objects.create(name=name,specification = specification ,maker = maker , is_import = is_import , price = price ,
                amount = amount ,position = position ,remain_amount = remain_amount , usage = usage , year = year,project = project)
        submit_type = request.POST['submit_type']
        if submit_type == 'save':
            return HttpResponseRedirect('/project/' + str(project_id))
        else:
            if submit_type == 'add_device':
                return HttpResponseRedirect('/project/add/device/' + str(project_id))
            else:
                return HttpResponseRedirect('/project/add/business/' + str(project_id))
    else:
        currentTime = time.localtime()
        years = range(-6,6)
        years = [ year + currentTime.tm_year for year in years ]
        return render_to_response('project_add_device.html', {'project_id': project_id ,'years':years})


@login_required
def project_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    devices = project.device_set.all()
    businesses = project.business_set.all()
    teachers = project.teachers.all()
    return render_to_response('project_view.html', {'project': project, 'devices': devices, 'businesses': businesses, 'teachers': teachers})


@login_required
def project_edit(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        teacherList = request.POST.getlist('teachers')
        projectName = request.POST['name']
        projectType = ProjectType.objects.get(id=request.POST['project_type'])
        startTime = request.POST['created_at']
        endTime = request.POST['ended_at']
        print type(startTime)
        p = re.compile(r'\d{4}\-\d{1,2}-\d{1,2}')
        if not p.match(startTime):
            error_message = "请按年-月-日的格式正确输入起始日期"
            devices = project.device_set.all()
            businesses = project.business_set.all()
            teachers = project.teachers.all()
            projectTypes = ProjectType.objects.all()
            return render_to_response('project_edit.html', {'project': project, 'devices': devices,
                'businesses': businesses, 'teachers': teachers, 'project_types': projectTypes, 'error_message': error_message})
        if not p.match(endTime):
            error_message = "请按年-月-日的格式正确输入终止日期"
            devices = project.device_set.all()
            businesses = project.business_set.all()
            teachers = project.teachers.all()
            projectTypes = ProjectType.objects.all()
            return render_to_response('project_edit.html', {'project': project, 'devices': devices,
                'businesses': businesses, 'teachers': teachers, 'project_types': projectTypes, 'error_message': error_message})
        if startTime > endTime:
            error_message = "起始日期不能大于终止日期, 请重新输入"
            devices = project.device_set.all()
            businesses = project.business_set.all()
            teachers = project.teachers.all()
            projectTypes = ProjectType.objects.all()
            return render_to_response('project_edit.html', {'project': project, 'devices': devices,
                'businesses': businesses, 'teachers': teachers, 'project_types': projectTypes, 'error_message': error_message})
        teacher_list=[]
        for teacher in teacherList:
            if teacher == '':
                teacherInstance = Teacher.objects.get(id=teacher)
                teacher_list.append(teacherInstance)
        addProject = Project.objects.create(name=projectName , project_type = projectType, created_at = startTime,ended_at=endTime)
        for teacher in teacher_list:
            addProject.teachers.add(teacher)
        addProject.save()
    else:
        #project = Project.objects.get(id=project_id)
        devices = project.device_set.all()
        businesses = project.business_set.all()
        teachers = project.teachers.all()
        projectTypes = ProjectType.objects.all()
        return render_to_response('project_edit.html', {'project': project, 'devices': devices,
            'businesses': businesses, 'teachers': teachers, 'project_types': projectTypes})

@login_required
def project_add_business(request , project_id):
    if request.method == 'POST':
        total = request.POST['total']
        year = request.POST['year']
        year += "-12-31 00:00"
        project = get_object_or_404(Project , pk=project_id)
        Business.objects.create(total = total , remain = total , project = project , year = year)
        submit_type = request.POST['submit_type']
        if submit_type == 'save':
            return HttpResponseRedirect('/project/'+str(project_id))
        else:
            if submit_type == 'add_device':
                return HttpResponseRedirect('/project/add/device/'+str(project_id))
            else:
                return HttpResponseRedirect('/project/add/business/'+str(project_id))
    else:
        currentTime = time.localtime()
        years = range(-6,6)
        years = [year + currentTime.tm_year for year in years]
        return render_to_response('project_add_business.html',{'years':years , 'project_id':project_id,})


@login_required
def project_delete(request,project_id):
    project = get_object_or_404(Project,pk=project_id)
    project.delete()
    return HttpResponseRedirect('/project')

@login_required
def project_search(request):
    return render_to_response('index.html')

@login_required
def device_edit(request, device_id):
    if request.method == 'POST':
        device = get_object_or_404(Device, pk=device_id)
        device.name = request.POST['name']
        device.specification = request.POST['specification']
        device.maker = request.POST['maker']
        if 'is_import' in request.POST.keys():
            device.is_import = True
        else:
            device.is_import = False
        device.price = request.POST['price']
        device.amount = request.POST['amount']
        device.position = request.POST['position']
        device.remain_amount = device.amount
        device.usage = request.POST['usage']
        month_to_add = "-12-31 00:00"
        year = request.POST['year']
        year += month_to_add
        device.year = year
        device.save()
        return HttpResponseRedirect('/project/' + str(device.project_id))
    else:
        device = get_object_or_404(Device, pk=device_id)
        currentTime = time.localtime()
        years = range(-6,6)
        years = [ year + currentTime.tm_year for year in years ]
        return render_to_response('device_edit.html', {'device': device,'years':years})


@login_required
def device_delete(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    project_id = device.project_id
    device.delete()
    return HttpResponseRedirect('/project/' + str(project_id))

@login_required
def business_edit(request, business_id):
    if request.method == 'POST':
        business = get_object_or_404(Business , pk=business_id)
        business.total = request.POST['total']
        business.remain = business.total
        month_to_add = "-12-31 00:00"
        year = request.POST['year']
        year += month_to_add
        business.year = year
        project_id = business.project_id
        business.save()
        return HttpResponseRedirect('/project/'+str(project_id))
    else:
        business = get_object_or_404(Business , pk = business_id)
        currentTime = time.localtime()
        years = range(-6,6)
        years = [year + currentTime.tm_year for year in years]
        return render_to_response('business_edit.html',{'business':business,'years':years,})

@login_required
def business_delete(request, business_id):
        business = get_object_or_404(Business,pk=business_id)
        project_id = business.project_id
        business.delete()
        return HttpResponseRedirect('/project/'+str(project_id))

@login_required
def teacher_select(request):
    departments = []
    departmentList = Department.objects.all()
    for dt in departmentList:
        teacherList = dt.teacher_set.all()
        department_teachers={}
        department_teachers['name']=dt.name
        department_teachers['teachers'] = teacherList
        departments.append(department_teachers)
    return render_to_response('teacher_select.html', {'departments': departments})

@login_required
def project_select(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    projects = teacher.project_set.all()
    return render_to_response('project_select.html', {'projects': projects, 'teacher': teacher})

@login_required
def funds_select(request, teacher_id, project_id):
    project = get_object_or_404(Project, pk=project_id)
    devices = project.device_set.all()
    businesses = project.business_set.all()
    teachers = project.teachers.all()
    return render_to_response('funds_select.html', {'project': project, 'devices': devices, 'businesses': businesses, 'teacher_id': teacher_id, 'teachers': teachers})


@login_required
def device_expense_add(request, device_id, teacher_id):
    device = get_object_or_404(Device, pk=device_id)
    if request.method == "POST":
        #teacher = get_object_or_404(Teacher, pk=teacher_id)
        amount = request.POST['amount']
        device_expense = DeviceExpense(device=device, amount=amount, created_at=datetime.now(), status=1, teacher_id=teacher_id)
        device_expense.save()
        device.remain_amount = device.remain_amount - float(amount)
        device.save()
        return HttpResponseRedirect('/record')
    else:
        amounts = device.remain_amount
        amount_array = range(amounts)
        amount_array = [ item + 1 for item in amount_array]
        return render_to_response('device_expense.html', {'device': device, 'teacher_id': teacher_id, 'amount_array': amount_array})

@login_required
def business_expense_add(request, business_id, teacher_id):
    business = get_object_or_404(Business, pk=business_id)
    if request.method == "POST":
        amount = request.POST['amount']
        business_expense = BusinessExpense(business=business, amount=amount, created_at=datetime.now(), status=1, teacher_id=teacher_id)
        business_expense.save()
        business.remain = business.remain - float(amount)
        business.save()
        return HttpResponseRedirect('/record')
    else:
        return render_to_response('business_expense.html', {'business': business, 'teacher_id': teacher_id})

@login_required
def expense_view(request):
    deviceExpenseList = DeviceExpense.objects.all()
    #deviceTeacherList = []
    #for deviceExpense in deviceExpenseList:
        #teacherName = deviceExpense.teacher.name
    businessExpenseList = BusinessExpense.objects.all()
    return render_to_response('expense_view.html',{'deviceExpenseList':deviceExpenseList,'businessExpenseList':businessExpenseList,})

@login_required
def expense_add(request):
    return render_to_response('index.html')

@login_required
def record_view_all(request):
    return render_to_response('index.html')

@login_required
def expense_view_department(request):
    return render_to_response('index.html')

@login_required
def expense_view_teacher(request):
    return render_to_response('index.html')

