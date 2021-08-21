from django.urls import path,include
from . import views
urlpatterns = [
    path('register',views.doctor_view,name='doctor_view'),
    path('login',views.doctor_view,name='doctor_view'),
    path('add/',views.doctor_create,name='doctor_create'),
    path('viewall/',views.doctor_list,name='doctor_list'),
    path('view/<id>',views.doctor_details,name='doctor_details'),
    path('<d_code>',views.doctor,name='doctor'),
    
]