# Create your views here.
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')

def teacher_view(request):
    #departments array
    departments = []
    return render_to_response('teacher_view.html', {'departments': departments})

def teacher_add(request):
    if request.method == 'POST':
        #save teacher and redirect to teacher_view
        pass
    else:
        departments = []
        return render_to_response('teacher_add.html', {'departments': departments})

def teacher_edit(request, teacher_id):
    if request.method == 'POST':
        #save teacher and redirect to teacher_view
        pass
    else:
        departments = []
        teacher = 0
        return render_to_response('teacher_edit.html', {'departments': departments, teacher: teacher})

def teacher_delete(request):
    return render_to_response('index.html')

def teacher_search(request):
    return render_to_response('index.html')

def project_view(request):
    return render_to_response('index.html')

def project_add(request):
    if request.method == 'POST':
        pass
    else:
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

