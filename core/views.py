from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View,TemplateView, DetailView, CreateView
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth import get_user_model
from .forms import SignUpForm, PrescriptionForm
from .models import User, Prescription
# Home page view
class HomepageView(LoginRequiredMixin,View):
  login_url = "/account/login"
  redirect_field_name = "next"
  template_name = "index.html"
  def get(self,request,*args, **kwargs):
    if request.user.is_doctor:
      context = {}
      context["patients"] = User.objects.all().filter(is_doctor=False).order_by("name")
      return render(request,self.template_name,context)
    else:
      return redirect(reverse("profile"))

# Signup View
class SignupView(UserPassesTestMixin,View):
  # only non authenticated user is allowed to visit this page
  def test_func(self):
    return not self.request.user.is_authenticated

  template_name = 'sign_up_page.html'

  def get(self,request,*args, **kwargs):
    form = SignUpForm()
    return render(request,self.template_name,{"form":form})

  def post(self,request,*args, **kwargs):
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data.get('email')
      password = form.cleaned_data.get('password1')
      user = authenticate(request, email=email, password=password)
      if user is not None:
          login(request, user)
          return redirect(reverse("home"))
      else:
        return render(request,self.template_name,{"form":form})
    else:
      return render(request,self.template_name,{"form":form})
# LoginView
class LoginView(UserPassesTestMixin,View):
  # only non authenticated user is allowed to visit this page
  def test_func(self):
    return not self.request.user.is_authenticated
  template_name = 'sign_in_page.html'

  def get(self,request,*args, **kwargs):
    print("Get method called")
    form = AuthenticationForm()
    return render(request,self.template_name,{"form":form})

  def post(self,request,*args, **kwargs):
    print("Post method called")
    email = request.POST.get('username')
    raw_password = request.POST.get('password')
    user = authenticate(request, email=email, password=raw_password)
    if user is not None:
        login(request, user)
        return redirect(reverse("home"))
    else:
      return render(request,self.template_name,{"error":"Your email and password does not match or you don't have an account"})
  
# Logout View
def Logout(request):
  if request.user.is_authenticated:
    logout(request)
  return redirect(reverse("home"))


# Patient Profile
class PatientProfileView(LoginRequiredMixin,TemplateView):
  login_url = "/account/login"
  redirect_field_name = "next"
  template_name = "Patient_Profile.html"
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["is_my_profile"] = True
      context["prescriptions"] = Prescription.objects.all().filter(user=self.request.user).order_by("-uploaded_at")
      return context

class OtherPatientProfileView(LoginRequiredMixin,DetailView):
  login_url = "/account/login"
  redirect_field_name = "next"
  template_name = "Patient_Profile.html"
  model = User
  context_object_name = "user"
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["prescriptions"] = Prescription.objects.filter(user=kwargs.get("object")).order_by("-uploaded_at")
      return context

class UploadPrescription(LoginRequiredMixin,View):
  login_url = "/account/login"
  redirect_field_name = "next"
  template_name = "prescription_form.html"

  def get(self,request,*args, **kwargs):
    form = PrescriptionForm()
    return render(request,self.template_name,{"form":form})

  def post(self,request,*args, **kwargs):
    Prescription.objects.create(user=request.user,title=request.POST.get("title"),prescribed_by=request.POST.get("prescribed_by"),image=request.FILES.get("image"))
    return redirect(reverse("profile"))
# Single prescription view
class PrescriptionView(LoginRequiredMixin,DetailView):
  login_url = "/account/login"
  redirect_field_name = "next"
  template_name = "prescription.html"
  model = Prescription
  context_object_name = "prescription"