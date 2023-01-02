
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name','nid','dob','gender','email')
