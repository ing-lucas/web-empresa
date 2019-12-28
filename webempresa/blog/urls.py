from django.urls import path
from . import views 

urlpatterns = [
    path('', views.blog, name = 'blog'),
    # Capturara lo que se encuentra entre category // y se lo pasara a la vista
    path('category/<int:category_id>/', views.category, name="category")
]