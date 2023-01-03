
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User,Prescription
from django.forms import ModelForm, Form
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name','nid','dob','gender','email')

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = ('title','prescribed_by','user','image')

