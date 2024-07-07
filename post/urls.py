
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
   # path("add/", views.add_post, name="add_post"),
   path("add/", views.AddpostCreatView.as_view(), name="add_post"),
   # path("edit/<int:id>", views.edit_post, name="edit_post"),
   path("edit/<int:id>", views.EditPostview.as_view(), name="edit_post"),
   # path("delete/<int:id>", views.delete_post, name="delete_post")
   path("delete/<int:id>", views.DeletePostview.as_view(), name="delete_post"),
   path("details/<int:id>", views.DetailspostView.as_view(), name="details_post")
]
