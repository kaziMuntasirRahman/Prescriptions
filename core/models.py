from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
import re


def check_email(email):
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  if not(re.fullmatch(regex, email)):
      raise ValueError('Your eamil is not valid')

class UserManager(BaseUserManager):
  def _create_user(self, name, nid,dob,gender, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    check_email(email)
    user = self.model(
        email=email,
        name = name,
        nid = nid,
        gender = gender,
        dob = dob,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, name,nid ,dob ,email,gender, password, **extra_fields):
    return self._create_user(name,nid,dob ,gender, email, password, False, False, **extra_fields)

  def create_superuser(self, name,nid,dob,gender,email, password, **extra_fields):
    user=self._create_user(name,nid,dob,gender, email, password, True, True, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    nid = models.CharField(max_length=25,unique=True)
    gender = models.CharField(max_length=20,null=True)
    is_staff = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    dob = models.DateField(auto_now=False, auto_now_add=False,null=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ["name","nid"]

    objects = UserManager()

class Prescription(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  prescribed_by = models.CharField(max_length=200)
  image = models.ImageField( upload_to="./image/prescription")
  uploaded_at = models.DateTimeField(auto_now_add=True) 

# Create your models here.
