from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("",views.landing, name="landing"),
    path("question/",views.top_questions, name="top_question"),
    path("question/<int:pk>/",views.question, name="question"),
    path("ask_question/",views.ask_question, name="ask_question"),
    path('question/<int:answer_id>/add_comment/', views.add_comment, name='add_comment'),
    path('question/<int:question_id>/add_answer/', views.add_answer, name='add_answer'),
    path('ask_question/submit/', views.submit_question, name='ask_question_submit'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout')

]