from django.urls import path, re_path
# from django.conf.urls import url
from . import views
from .views import FactDocumentClaimantCat, FactDocumentDefendantCat
# app_name = 'systemsettings'

urlpatterns = [
    path('', views.SettingsPage, name="system-settings-home" ),
    path('criminal-matter/', views.CriminalMatterEntry, name="criminal-matters-entry" ),
    path('civil-matter/', views.CivilMatterEntry, name="civil-matters-entry" ),
    path('autoload-data/', views.AutoLoaddata, name="autoload-data" ),   
    path('sample-modal-popup/', views.SampleModalPopup, name="sample-modal-popup" ),
    path('activity-logs/', views.ActivityLogView, name="activity_logs" ),
    path('<file_no>', views.Matter_Detail, name="matter_detail" ),
    # path('document-claimant-category/', views.FactDocumentClaimantCat, name="document-claimant-category"),
    path('document-claimant-category/', FactDocumentClaimantCat.as_view(), name="document-claimant-category"),
    path('document-defendant-category/', FactDocumentDefendantCat.as_view(), name="document-defendant-category"),

    

   
    # path('civil-matter/edit-sample/', views.EditSample, name="edit-civil-sample" ),   
]
