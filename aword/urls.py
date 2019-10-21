# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('', views.home, name='homepage'),
#     path('create/profile',views.create_profile, name='create-profile'),
#     path('new/project',views.new_project, name='new-project'),
#     path('profile/',views.profile, name='profile'),
#     path('search/',views.search_results, name='search_results'),
#     #path('user/',views.user_profile,name='user-profile'),
#     path('signup/',views.signup, name='signup'),
#     path('api/profiles/', views.ProfileList.as_view()),
#     path('api/projects/', views.ProjectList.as_view()),
#     path('api/categories/', views.CategoriesList.as_view()),
#     path('api/countries/', views.CountriesList.as_view()),
#     path('api/technologies/', views.TechnologiesList.as_view()),
    

# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
