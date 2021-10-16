from django.urls import path, include
from rest_framework.routers import DefaultRouter

from usersApp import views

router = DefaultRouter()
# router.register('user-wish-list', views.UserWishListViewSet)
# router.register('search-query', views.SearchQueryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test/', views.TestView.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('normal-user/', views.NormalUserView.as_view()),
]