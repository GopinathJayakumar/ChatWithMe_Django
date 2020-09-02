from django.urls import path
from .views import Chat_Detail_View, Chat_List_View, Chat_Create_View, Chat_Update_View, Chat_Delete_View

urlpatterns = [
    path('create/', Chat_Create_View.as_view(), name='create_view'),        #create/
    path('<abc>/', Chat_Detail_View.as_view(), name='details_view'),        #1/
    path('<abc>/update/', Chat_Update_View.as_view(), name='update_view'), #1/update
    path('<abc>/delete/', Chat_Delete_View.as_view(), name='delete_view'),  # 1/update
    path('', Chat_List_View.as_view(), name='list_view'),                   #/
]
