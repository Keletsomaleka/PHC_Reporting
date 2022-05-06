from django.contrib import admin
from django.urls import path,include
from student_dash import views

urlpatterns = [
    path('stats/',views.dash, name='statistics'),
    path('',views.infoscreen, name='dashboard'),
    path('allstats/',views.staff_info, name='allstats'),
    path('signup/', views.signup, name='signup'),
    path('reports/',views.report, name='reports'),
    path('finance/',views.finance,name='finance'),
    path('nav/',views.nav,name='nav'),
    path('accounts/', include('django.contrib.auth.urls')),

]