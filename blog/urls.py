from django.urls import path
from .views import index, detail, list, contact, about, login_view, logout_view, Register

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('list/', list, name='list'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', Register.as_view(), name='register'),
]
