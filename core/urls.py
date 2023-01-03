from django.urls import path
from .views import PrescriptionView,SignupView,HomepageView,Logout,LoginView,PatientProfileView,OtherPatientProfileView,UploadPrescription
urlpatterns = [
  path('',HomepageView.as_view(),name="home"),
  path('account/logout',Logout,name="logout"),
  path('account/login',LoginView.as_view(),name="login"),
  path('account/signup',SignupView.as_view(),name="signup"),
  path('account/profile',PatientProfileView.as_view(),name="profile"),
  path('patient/profile/<int:pk>',OtherPatientProfileView.as_view(),name="patient"),
  path('prescription/upload',UploadPrescription.as_view(),name="upload_prescription"),
  path('prescription/<int:pk>',PrescriptionView.as_view(),name="prescription")
]