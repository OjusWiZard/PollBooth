from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultView.as_view(), name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('login/', views.loginPage, name='loginPage'),
    path('login/in/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('register/', views.register, name='register'),
]
