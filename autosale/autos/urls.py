from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mark", views.mark, name="mark"),
    path("model", views.model, name="model"),
    path("price", views.price, name="price"),
    path("category", views.category, name="category"),
    path("sort_by_year", views.sort_by_year, name="sort_by_year"),
    path("reset", views.index, name="reset"),
]