from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/<str:date>/', views.bookings, name='bookings_by_date'),
]
