from django.contrib import admin
from django.urls import path, include
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),

    # API - Client Master 
    path('createclient',v.createclient, name = 'createclient'),

    path('Addclient',v.Addclient, name = 'Addclient'),
    path('getclientdata',v.getclientdata, name = 'getclientdata'),
    path('Updateclient',v.Updateclient, name = 'Updateclient'),
    path('Deleteclient',v.Deleteclient, name = 'Deleteclient'),

    path('Addclientsidemanager',v.Addclientsidemanager, name = 'Addclientsidemanager'),
    path('updateclientsidemanager',v.updateclientsidemanager, name = 'updateclientsidemanager'),
    path('DeleteManager',v.DeleteManager, name = 'DeleteManager'),

    path('Add_createclient',v.Add_createclient, name = 'Add_createclient'),
    path('update_createclient',v.update_createclient, name = 'update_createclient'),
    path('delete_createclient',v.delete_createclient, name = 'delete_createclient'),

    path('Event',v.Event, name = 'Event'),
    # path('getEvent',v.getEvent, name = 'getEvent'),
    # path('UpdateEvent',v.UpdateEvent, name = 'UpdateEvent'),
    path('deleteevent/<int:id>',v.deleteevent, name = 'deleteevent'),
    path('Addclient_project',v.Addclient_project, name = 'Addclient_project'),
    path('Updateclientproject',v.Updateclientproject, name = 'Updateclientproject'),
    path('deleteclientproject',v.deleteclientproject, name = 'deleteclientproject'),




]