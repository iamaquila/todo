from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Category, User
from .forms import PersonalInfoForm, CategoryForm, CustomUserCreationForm
from .models import PersonalInfo
from


def index(request):