from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from . import views
urlpatterns = [
    path('', views.home, name='login'),
    path('home/',views.landing_page, name='home'),
    path('entry/', views.entry, name='entry'),
    path('exit/', views.exit, name='exit'),
    path('todayreport/',views.export_users_csv_today,name='todayreport'),
    path('overallreport/',views.export_users_csv_overall,name='overallreport'),
    path('stillinsidereport/',views.export_users_csv_inside,name='stillinsidereport'),
    path('customreport/',views.export_users_csv_date,name='customreport'),
    path('logout/', views.logout, name='logout'),
]