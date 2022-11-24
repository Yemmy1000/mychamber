

from django.urls import path
from . import views
from .views import MatterUpdate, ClientCategory, CaseAttorney, ClientCoparties, ClientAdverseParties, CaseAssociateNames, \
    CaseBrief, CaseAssignee, CaseFactDocument, CaseNatureOfClaim, EditCaseBrief, CaseAssigneeEdit

urlpatterns = [
    # path('', views.eventPage, name="event" ), 
    path('<file_no>', MatterUpdate.as_view(), name="matter-update"),
    path('client-category/<file_no>', ClientCategory.as_view(), name="client-category"),
    path('case-attorney/<file_no>', CaseAttorney.as_view(), name="case-attorney"), 
    path('client-coparties/<file_no>', ClientCoparties.as_view(), name="client-coparties"),
    path('client-adverse-parties/<file_no>', ClientAdverseParties.as_view(), name="client-adverse-parties"),
    path('case-associate-names/<file_no>', CaseAssociateNames.as_view(), name="case-associate-names"),
    path('case-fact-documents/<file_no>', CaseFactDocument.as_view(), name="case-fact-documents"),
    path('nature-of-claim/<file_no>', CaseNatureOfClaim.as_view(), name="nature-of-claim"),  

    path('case-brief/<file_no>', CaseBrief.as_view(), name="case-brief"), 
    path('case-brief-edit/<pk>', EditCaseBrief.as_view(), name="case-brief-edit"),
    path('case-assignee/<file_no>', CaseAssignee.as_view(), name="case-assignee"), 
    path('case-assignee-edit/<pk>', CaseAssigneeEdit.as_view(), name="case-assignee-edit"), 
    # path('update-basic-information/<file_no>', UpdateBasicInformation.as_view(), name="update-basic-information"),   
    # path('update-basic-info/<file_no>', views.UpdateBasicInfo, name="update-basic-info"),   
  


]
