from django.urls import path
from .views import HomePageView, AboutPageView, CantactPageView, WorkPageView
0
urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='homepage'),

    path('contact/', CantactPageView.as_view(), name='cantact'),

    path('work/', WorkPageView.as_view(), name='staj'),
]

