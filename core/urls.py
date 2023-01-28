from django.urls import path

from core import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addcontact', views.addcontact, name='addcontact'),
    path('contactprofile/<int:pk>', views.contactprofile, name='contactprofile'),
    path('edit_contact/<int:pk>', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:pk>', views.delete_contact, name='delete_contact'),

]
