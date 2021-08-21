from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.patient_view,name='patient_view'),
    path('add/',views.patient_create,name='patient_create'),
    path('viewall/',views.patient_list,name='patient_list'),
    path('view/<id>',views.patient_details,name='patient_details'),
    path('<p_code>',views.patient,name='patient'),
    
   
]