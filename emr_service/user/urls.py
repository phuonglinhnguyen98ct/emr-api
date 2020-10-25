# Django imports
from django.conf.urls import url, include

# Application imports
from emr_service.user.views import (
    EmrServiceView,
    EmrServiceRemoveView,
)
#
urlpatterns = [
    url(r'^(?P<emr_id>[0-9A-Fa-f-]+)/$', EmrServiceView.as_view(), name='user-add-emr-service'),
    url(r'^(?P<emr_id>[0-9A-Fa-f-]+)/remove/(?P<emr_service_id>[0-9A-Fa-f-]+)/$', EmrServiceRemoveView.as_view(), name='user-remove-emr-service'),
]
