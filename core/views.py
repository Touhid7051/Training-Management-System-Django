from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView,DetailView, CreateView
from core.models import *
from core.forms import *
from .models import Session
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

def class_view_decorator(function_decorator):
    """Convert a function based decorator into a class based decorator usable
    on class based Views.

    Can't subclass the `View` as it breaks inheritance (super in particular),
    so we monkey-patch instead.
    """

    def simple_decorator(View):
        View.dispatch = method_decorator(function_decorator)(View.dispatch)
        return View

    return simple_decorator

# Create your views here.
def index(request):
    note = Resolution.objects.all
    return render(request, 'trainee/index.html', {'note':note})


@class_view_decorator(login_required)
class AddApplicant(CreateView):
    model = Applicant
  
    form_class = Add_Applicant

    template_name = 'trainee/add_applicant.html'
    success_url = '/success/'

# def AddApplicant(request):
#     if request.user.is_authenticated:
#         user = request.user
#         print(user)
#         form = Add_Applicant(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             applicant = form.save(commit=False)
#             applicant.user = user
#             applicant.save()
#             print(applicant)
#             return redirect("index")
#         else: 
#             return render(request , 'trainee/add_applicant.html' , context={'form' : form})


def dashboard(request):
    return render(request, 'core/dashboard.html')



# COURSE

class ManageCourse(ListView):
    model = Course
    template_name = 'core/manage_Course.html'
    context_object_name = 'manage_course_list'

class DetailedCourse(DetailView):
    model = Course
    template_name = 'blog/detail_view.html'
    context_object_name = 'course'
    
class AddCourse(CreateView):
    model = Course
    form_class = Add_Course
    template_name = 'core/add_course.html'
    success_url = '/'


class EditCourse(UpdateView):
    model = Course
    form_class = Add_Course
    pk_url_kwarg = 'pk'
    template_name = 'core/add_course.html'
    success_url = '/'


class DeleteCourse(DeleteView):
    model = Course
    pk_url_kwarg = 'pk'
    template_name = 'blog/delete_view.html'
    success_url = '/blog/manage_post_list'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
    


# Session
class ManageSession(ListView):
    model = Session
    template_name = 'core/manage_Session.html'
    context_object_name = 'Session'

class DetailedSession(DetailView):
    model = Course
    template_name = 'blog/detail_Session.html'
    context_object_name = 'Session'
    
class AddSession(CreateView):
    model = Session
    form_class = Add_Session
    template_name = 'core/add_Session.html'
    success_url = '/'


class EditSession(UpdateView):
    model = Session
    form_class = Add_Session
    pk_url_kwarg = 'pk'
    template_name = 'core/add_Session.html'
    success_url = '/'


class DeleteSession(DeleteView):
    model = Session
    pk_url_kwarg = 'pk'
    template_name = 'core/delete_Session.html'
    success_url = '/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


# applicants

class ManageApplicant(ListView):
    model = Applicant
    template_name = 'core/manage_Applicant.html'
    context_object_name = 'Applicant'

class Remark_Applicant(UpdateView):
    model = Applicant
    form_class = Remarks_Applicant
    pk_url_kwarg = 'pk'
    template_name = 'core/Remarks_Applicant.html'
    success_url = '/'
# resolution


class ManageResolution(ListView):
    model = Resolution
    template_name = 'core/manage_Resolution.html'
    context_object_name = 'Resolution'

class DetailedResolution(DetailView):
    model = Resolution
    template_name = 'core/detail_Resolution.html'
    context_object_name = 'Resolution'
    
class AddResolution(CreateView):
    model = Resolution
    form_class = Add_Resolution
    template_name = 'core/add_Resolution.html'
    success_url = '/'


class EditResolution(UpdateView):
    model = Resolution
    form_class = Add_Resolution
    pk_url_kwarg = 'pk'
    template_name = 'core/add_Resolution.html'
    success_url = '/'


class DeleteResolution(DeleteView):
    model = Resolution
    pk_url_kwarg = 'pk'
    template_name = 'core/delete_Resolution.html'
    success_url = '/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


# Financial aid


def sessions(request):
    sessions = Session.objects.all()

    return render(request, 'core/sessions.html', {'sessions': sessions})

def session(request, session_id):
    session = get_object_or_404(Session, pk=session_id)

    return render(request, 'core/session.html', {'session': session})

def session_short_list(request, session_id):
    #session = get_object_or_404(Session, pk=session_id,session.applicants.status )
    applicant = Applicant.objects.filter(session = session_id, status="Accepted")

    return render(request, 'core/session_short_list.html', {'applicant': applicant})

def session_waiting_list(request, session_id):
    #session = get_object_or_404(Session, pk=session_id,session.applicants.status )
    applicant = Applicant.objects.filter(status="Waiting")

    return render(request, 'core/session_short_list.html', {'applicant': applicant})
def done(request, session_id):
    #session = get_object_or_404(Session, pk=session_id,session.applicants.status )
    applicant = Applicant.objects.filter(status="Successfully Done")

    return render(request, 'core/session_short_list.html', {'applicant': applicant})

# reg

def registerPage(request):
    #if request.user.is_authenticated:
     #   return redirect('index')

    #else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                user=form.save()
                username =form.cleaned_data.get('username')



                messages.success(request, 'Account is created for ' +  username )
                return redirect('login')

        context = {'form' : form}
        return render(request, 'trainee/register.html' , context )


def loginPage(request):
    #if request.user.is_authenticated:
        #return redirect('index')

    #else:
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request ,username = username ,password = password)

        if user is not None:
            login(request , user)
            return redirect('AddApplicant')

        else:
            messages.info(request, 'Username or Password is incorrect')
    context ={}
    return render(request, 'trainee/login.html', context)



def load_Sub_district(request):
    district_id = request.GET.get('district')
    sub_district = Sub_district.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'trainee/dropdown_list_options.html', {'sub_district': sub_district})


class Applicant_Detailed(DetailView):
    model = Applicant
    template_name = 'core/Apllicant_detail.html'
    context_object_name = 'applicant'
    
def success(request):
    return render(request, 'trainee/success.html')