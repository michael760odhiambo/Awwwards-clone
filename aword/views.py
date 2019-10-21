from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Categories,Technologies,Countries,Project,Profile
from .forms import ProjectForm,ProfileForm,UserCreationForm, SignUpForm
import datetime as dt
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer,TechnologiesSerializer,ColorsSerializer,CountriesSerializer,CategoriesSerializer



def home(request):
    date = dt.date.today()
    winners = Project.objects.all()
    nominees = Project.objects.all()
    directories = Project.objects.all()
    resources = Project.objects.all()

    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

        current_user = request.user
        profile = Profile.objects.get(username=current_user)

    except ObjectDoesNotExist:
        return redirect('create-profile') 

    return render(request, 'all-pages/index.html',{"winners":winners,"profile":profile,"date":date,"nominees":nominees,"directories":directories,"resources":resources})

def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()

            return redirect('homepage')
    else:
        form=ProfileForm()

    return render(request, 'all-pages/create_profile.html', {'form':form})

def new_project(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.username = current_user
            project.pic = project.pic
            project.country = project.country
            project.save()

    else:
        form = ProjectForm()

    return render(request, 'all-pages/new_project.html', {'form':form})                        


def profile(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    projects = Project.objects.filter(user=current_user)

    return render(request, 'all-pages/profile.html', {'profile':profile,'projects':projects})

# # def user_profile(request,username):
# #     user = User.objects.get(current_user=username)
# #     profile = Profile.objects.get(username=user)
# #     project = Project.objects.get(username=user)

# #     return render(request, 'all-pages/user-profile.html', {'profile':profile, 'project':project}) 


def search_results(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        searched_projects = Project.search_project(search_term)
        message = f'{search_term}'

        print(searched_projects)

        return render(request, 'all-pages/search.html', {"message":message,"projects":searched_projects,"profile":profile})        

    else:
        message="You haven't searched for any term"
        return render(request,'all-pages/search.html',{"message":message})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})        
# # Create your views here.


# class ProfileList(APIView):
#     def get(self, request, format=None):
#         all_profiles = Profile.objects.all()
#         serializers = ProfileSerializer(all_profiles, many=True)
#         return Response(serializers.data)

# class ProjectList(APIView):
#     def get(self, request, format=None):
#         all_projects = Project.objects.all()
#         serializers = ProjectSerializer(all_projects, many=True)
#         return Response(serializers.data)

# class CategoriesList(APIView):
#     def get(self, request, format=None):
#         all_categories = categories.objects.all()
#         serializers = categoriesSerializer(all_categories, many=True)
#         return Response(serializers.data)

# class TechnologiesList(APIView):
#     def get(self, request, format=None):
#         all_technologies = technologies.objects.all()
#         serializers = technologiesSerializer(all_technologies, many=True)
#         return Response(serializers.data)



# class CountriesList(APIView):
#     def get(self, request, format=None):
#         all_countries = countries.objects.all()
#         serializers = countriesSerializer(all_countries, many=True)
#         return Response(serializers.data)