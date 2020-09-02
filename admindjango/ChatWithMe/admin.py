from django.contrib import admin
from .models import Chat
from .forms import ChatModelForm


# Register your models here.
# admin.site.register(Chat)

class ChatModelAdmin(admin.ModelAdmin):
    form = ChatModelForm


admin.site.register(Chat, ChatModelAdmin)
