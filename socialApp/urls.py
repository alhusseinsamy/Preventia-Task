from django.urls import path, include
from rest_framework.routers import DefaultRouter

from socialApp import views

router = DefaultRouter()
router.register('post', views.PostViewSet)
router.register('comment', views.CommentViewSet)
router.register('like', views.LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]