from . import views
from django.urls import path

urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    path('', views.index, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('blogs/', views.posts, name='blogs'),

   
]