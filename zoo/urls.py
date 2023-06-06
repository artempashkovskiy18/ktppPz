from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('prices/', views.prices),
    path('rules/', views.rules),
    path('history/', views.history),
    path('excursion/', views.excursion, name="excursionReg"),
    path('news/', views.news),
    path('getAllExcursions/', views.getAllExcursions),
    path('excursion/<int:id>/', views.getExcursion, name="excursion"),
    path('login/', LoginView.as_view(), name="login")
]
