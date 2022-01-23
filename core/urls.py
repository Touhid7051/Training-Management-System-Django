from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *




urlpatterns = [
    # Trainee
    path('', views.index, name='index'),
    path('AddApplicant/', AddApplicant.as_view(), name='AddApplicant'),
    path('ajax/load_Sub_district/', views.load_Sub_district, name='ajax_load_Sub_district'),


    path('register/', views.registerPage , name='register'),
    path('login/', views.loginPage , name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),




    # course
    path('dashboard/', views.dashboard, name='dashboard'),
    path('AddCourse/', AddCourse.as_view(), name="AddCourse"),
    path('ManageCourse/', ManageCourse.as_view(), name="ManageCourse"),
    path('EditCourse/<int:pk>', EditCourse.as_view(), name="EditCourse"),
    path('DeleteCourse/<int:pk>', DeleteCourse.as_view(), name="DeleteCourse"),

    # session
    path('AddSession/', AddSession.as_view(), name="AddSession"),
    path('ManageSession/', ManageSession.as_view(), name="ManageSession"),
    path('EditSession/<int:pk>', EditSession.as_view(), name="EditSession"),
    path('DeleteSession/<int:pk>', DeleteSession.as_view(), name="DeleteSession"),
    # 
    path('sessions/', views.sessions, name='sessions'),
    path('<int:session_id>/', views.session, name='session'),


    # applicants
    path('ManageApplicant/', ManageApplicant.as_view(), name="ManageApplicant"),
    path('Applicant_Detailed/<int:pk>', Applicant_Detailed.as_view(), name="Applicant_Detailed"),
    path('Remark_Applicant/<int:pk>', Remark_Applicant.as_view(), name="Remark_Applicant"),

    # resolution
    path('AddResolution/', AddResolution.as_view(), name="AddResolution"),
    path('ManageResolution/', ManageResolution.as_view(), name="ManageResolution"),
    path('EditResolution/<int:pk>', EditResolution.as_view(), name="EditResolution"),
    path('DeleteResolution/<int:pk>', DeleteResolution.as_view(), name="DeleteResolution"),

    # Financial aid
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)