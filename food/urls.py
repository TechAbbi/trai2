from django.urls import path
from . import views
app_name = "food"
urlpatterns = [
    path('', views.home, name="home"),
    # path("index/", views.index, name="index"),
    path("index/", views.IndexListView.as_view(), name="index"),
    path("details/<int:pk>/", views.ItemDetailView.as_view(), name="details"),
    path("update/<int:pk>/", views.ItemUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.ItemDeleteView.as_view(), name="delete"),
    path("belowhundred/", views.less_tha_100)
]
