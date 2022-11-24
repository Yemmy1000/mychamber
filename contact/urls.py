from django.urls import path, re_path
# from django.conf.urls import url
from . import views
from .views import PersonContactListJson

urlpatterns = [
    path('', views.personContactPage, name="person-contact" ),
    path('company-contact/', views.companyContactPage, name="company-contact" ), 
    path('create-person/', views.CreatePersonContact, name="create-person"),
    path('view-person/<str:fk>', views.viewPersonContact, name="view-person"),   
    path('update-person/<str:fk>', views.updatePersonContact, name="update-person"),        
    path('create-company/<str:fk>', views.createCompanyContact, name="create-company"), 
    path('person-contact/', PersonContactListJson.as_view(), name='person_contact_json'),
    path('person-contact-popup/', views.personContactPopup, name="person-popup"),
    path('delete-person-contact/', views.deletePersonContact, name="delete-person-contact"),
]
