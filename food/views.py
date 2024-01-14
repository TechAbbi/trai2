from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
# for rest api
from rest_framework import viewsets
from .serializers import ItemSerializer
# for class view
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
# orm
from django.db.models import Q,Max,Min,Avg,Count, Sum

# Create your views here.
def home(request):
    return HttpResponse("Welcome !")


def index(request):
    item_list = Item.objects.all()
    return render(request, "food/index.html", {"item_list": item_list})


class IndexListView(ListView):
    model = Item
    template_name = "food/index.html"
    # context_object_name = "item_list"


class IndexViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(DetailView):
    model = Item
    template_name = "food/details.html"


class ItemUpdateView(UpdateView):
    model = Item
    template_name = "food/update.html"
    fields = "__all__"
    success_url = reverse_lazy("food:index")


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "food/delete.html"
    success_url = reverse_lazy("food:index")
    a=b;


def less_tha_100(request):
    items_below_hundred = Item.objects.filter(Q(name__icontains="e") | Q(price__gt=100))

    return HttpResponse(items_below_hundred)
