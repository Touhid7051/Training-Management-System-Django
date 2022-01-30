from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class Add_Applicant(ModelForm):
    
    class Meta:
        model = Applicant
        fields =[
            "course", "session", "name_ban", "name_eng", 
        "fathers_name_bangla", "fathers_name", 
        "mothers_name_bangla", "mothers_name", 
        "marital_status", "present_address", 
        "village", "district",
        "sub_district", "ps",
        "post_office", "date_of_birth",
        "religion", "nid_BC",
        "education", "phone", 
        "picture"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_district'].queryset = Sub_district.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['sub_district'].queryset = Sub_district.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sub_district'].queryset = self.instance.district.sub_district_set.order_by('name')

class Remarks_Applicant(ModelForm):
    
    class Meta:
        model = Applicant
        fields =["status", "roll_no", ]


    
class Add_Course(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class Add_Session(ModelForm):
    class Meta:
        model = Session
        fields = '__all__'


class Add_Resolution(ModelForm):
    class Meta:
        model = Resolution
        fields = '__all__'

class Add_Financial_aid(ModelForm):
    class Meta:
        model = Financial_aid
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username' , 'email' , 'password1' , 'password2']