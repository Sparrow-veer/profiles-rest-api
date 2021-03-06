from django.urls import path

from profiles_api import views

# imports required for router for ViewSet
from django.urls import include
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)

urlpatterns=[
path('hello-view/',views.HelloApiView.as_view()),
path('login/',views.UserLoginApiView.as_view()),
path('',include(router.urls)),
]
