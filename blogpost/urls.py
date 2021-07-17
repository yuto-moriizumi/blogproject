from .views import BlogList, BlogDetail, BlogCreate
from django.urls import path

urlpatterns = [
    path("list/", BlogList.as_view(), name="list"),
    path("detail/<int:pk>", BlogDetail.as_view()),
    path("create/", BlogCreate.as_view()),
]
