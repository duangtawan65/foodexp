from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add-category/', views.add_category, name='add_category'),
    path('manage-food/', views.manage_food, name='manage_food'),
    path('add-food-item/', views.add_food_item, name='add_food_item'),
    path('delete-food-item/<int:pk>/', views.delete_food_item, name='delete_food_item'),

]
