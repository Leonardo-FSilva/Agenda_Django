from django.urls import path
from contact import views


app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/<int:contact_id>/detail/update/', views.update, name='update'),
    path('contact/<int:contact_id>/detail/delete/', views.delete, name='delete'),
    path('contact/create/', views.create, name='create'),

    path('user/create/', views.register, name='register'),
]

