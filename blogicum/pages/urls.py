from django.urls import path  # type: ignore[import-untyped]

from . import views

app_name: str = 'pages'

urlpatterns: list[path] = [
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('rules/', views.RulesPageView.as_view(), name='rules'),
]
