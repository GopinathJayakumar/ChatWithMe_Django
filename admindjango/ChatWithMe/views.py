from django.shortcuts import render
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Chat
from .forms import ChatModelForm
from django.urls import reverse_lazy


# create - POST
class Chat_Create_View(CreateView):
    form_class = ChatModelForm
    template_name = 'create_view.html'
    success_url = "/"


# update
class Chat_Update_View(UpdateView):
    queryset = Chat.objects.all()
    form_class = ChatModelForm
    template_name = 'update_view.html'
    success_url = "/"

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get('abc')
        return Chat.objects.get(id=pk)


# Retrive(Read) - GET
# Create your views here.
class Chat_Detail_View(DetailView):
    template_name = 'details_view.html'
    queryset = Chat.objects.all()

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get('abc')
        return Chat.objects.get(id=pk)


class Chat_List_View(ListView):
    template_name = 'list_view.html'
    queryset = Chat.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(Chat_List_View, self).get_context_data(*args, **kwargs)
        return context


class Chat_Delete_View(DeleteView):
    model = Chat
    template_name = 'delete_view.html'
    success_url = reverse_lazy("list_view")

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get('abc')
        return Chat.objects.get(id=pk)

