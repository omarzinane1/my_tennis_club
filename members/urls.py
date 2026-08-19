from django.urls import path

from members import admin
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>',views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
    path('admin/', admin.site.urls),
]