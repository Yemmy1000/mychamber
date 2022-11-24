from django.urls import path
from . import views
from .views import MatterListJson, MatterInfoView, UpdateMatterInfoView
from contact.views import AllPersonContactList

urlpatterns = [
    path('', views.MatterPage, name="matter" ),
    path('matter-info/', MatterInfoView.as_view(), name='matter-info'),
    path('create-matter-Info/', views.CreateMatterInfo, name="create-matter"),
    path('create-matter-attorney/<file_no>', views.createMatterAttorney, name="create-matter-attorney"),
    path('create-matter-other-party/<file_no>', views.createMatterOtherParty, name="create-matter-other-party"),
    path('create-matter-adverse-party/<file_no>', views.CreateMatterAdverseParty, name="create-matter-adverse-party"),
    path('create-matter-other-filename/<file_no>', views.CreateMatterOtherFileName, name="create-matter-other-filename"),
    path('create-matter-document/<file_no>', views.createMatterDocument, name="create-matter-document"),
    path('create-matter-nature-civil/<file_no>', views.createMatterNatureCivil, name="create-matter-nature-civil"),
    path('create-matter-nature-criminal/<file_no>', views.createMatterNatureCriminal, name="create-matter-nature-criminal"),
    path('person-contact-list/', AllPersonContactList, name="person-list"),
    path('create-matter-description/<file_no>', views.createMatterDescription, name="create-matter-description"),
    path('matter-list/', MatterListJson.as_view(), name='matter_json'),
    path('view-matter/<str:file_no>', views.viewMatter, name="view-matter"),
    
    path('data-autoload/', views.DataAutoloader, name="data-autoload"),
    # path('update-matter-info/<file_no>', views.UpdateMatterInfo, name="update-matter-info"),
    path('update-matter-info/<pk>', UpdateMatterInfoView.as_view(), name="update-matter-info"),
    path('update-matter-attorney/<file_no>', views.UpdateMatterAttorney, name="update-matter-attorney"),
    path('update-matter-other-party/<file_no>', views.UpdateMatterOtherParty, name="update-matter-other-party"),
    path('update-matter-adverse-party/<file_no>', views.UpdateMatterAdverseParty, name="update-matter-adverse-party"),
    path('update-matter-other-filename/<file_no>', views.UpdateMatterOtherFileName, name="update-matter-other-filename"),
    path('update-matter-document/<file_no>', views.UpdateMatterDocument, name="update-matter-document"),
    path('update-matter-nature-civil/<file_no>', views.UpdateMatterNatureCivil, name="update-matter-nature-civil"),
    path('update-matter-nature-criminal/<file_no>', views.UpdateMatterNatureCriminal, name="update-matter-nature-criminal"),
    path('update-matter-description/<file_no>', views.UpdateMatterDescription, name="update-matter-description"),
    path('delete-matter-data/', views.DeleteMatterData, name="delete-matter-data"),
    path('delete-matter-records/', views.DeleteMatterRecords, name="delete-matter-records"),

    # path('<file_no>', MatterUpdate.as_view(), name="matter-update"),
]
