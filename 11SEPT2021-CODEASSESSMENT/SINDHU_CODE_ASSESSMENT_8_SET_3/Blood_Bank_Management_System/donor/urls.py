from django.urls import path,include
from donor import views

urlpatterns = [
#  Views
   path('reg/',views.add_donor_view,name='add_donor_view'),
   path('viewalldonor/',views.viewall_donor_view,name='viewall_donor_view'),
   path('viewupdate/',views.update_donor_view,name='update_donor_view'),
   path('signin_check/',views.signin_view_check,name='signin_view_check'),
   path('signin/',views.signin_view,name='signin_view'),
   path('welcome/',views.welcome_view,name='welcome_view'),

#    API's 
    path('add/',views.donor_create,name='donor_create'),
    path('viewall/',views.donor_list,name='donor_list'),
    path('viewdonor/<id>',views.donor_details,name='donor_details'),
    path('update_action_api/',views.update_data_read,name='update_data_read'),
    path('updatesearch/',views.updateapi,name='updateapi'),
]