from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('detailsform/',views.detailsform,name='detailsform'),
    path('logout/',views.logout,name='logout'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX
]