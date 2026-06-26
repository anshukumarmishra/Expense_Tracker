from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("expense/",views.expense,name="expense"),
    path("expense/<int:id>",views.delete_expense,name="delete"),
    path("edit/<int:id>",views.edit_expense,name="edit"),
    path("report/",views.report,name="report"),
    path("register/",views.register_user,name="register"),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout")
]