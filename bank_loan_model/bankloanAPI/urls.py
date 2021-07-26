from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('MyAPI', views.ApprovalView)
urlpatterns = [
    path('form/', views.cxcontact, name='cxform'),
    path('api/', include(router.urls)),
    # path('status/', views.approvereject),
]
