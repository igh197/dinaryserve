from django.urls import path

from download import views

urlpatterns = [
    path('getfile/', views.getfile),

]
