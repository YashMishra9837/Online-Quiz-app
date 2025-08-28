from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path('index/', views.index_def, name='index_def'),
    path("index/<int:myid>/", views.index, name="index"),
    path("index/<int:myid>/", views.quiz, name="quiz"), 
    path('index/<int:myid>/data/', views.quiz_data_view, name='quiz-data'),
    path('index/<int:myid>/save/', views.save_quiz_view, name='quiz-save'),
    path("signup/", views.Signup, name="signup"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path('about_us/', views.about_us, name='about_us'),
    path('add_quiz/', views.add_quiz, name='add_quiz'),    
    path('add_question/', views.add_question, name='add_question'),  
    path('add_options/<int:myid>/', views.add_options, name='add_options'), 
    path('results/', views.results, name='results'),    
    path('delete_question/<int:myid>/', views.delete_question, name='delete_question'),  
    path('delete_result/<int:myid>/', views.delete_result, name='delete_result'), 
    path('forgotpass/', views.forgotpass, name='forgotpass'),
    path('resetpass/<uidb64>/<token>/', views.resetpass, name='resetpass'),
]