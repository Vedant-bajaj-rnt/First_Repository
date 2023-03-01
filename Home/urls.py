from django.urls import path,include
from Home import views

urlpatterns = [
    path("",views.login),
    path('home',views.home,name='home'),
    path('logout',views.logout),
    path('registeration',views.registeration),
    path('login',views.login),
    path('show',views.show),
    path('send',views.send),
    path('delete',views.delete),
    path('edit',views.edit),
    path('RecordEdited',views.RecordEdited)

]