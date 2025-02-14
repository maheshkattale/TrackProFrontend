"""
URL configuration for TrackProFrontend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('Users.urls', 'users'),namespace='users')),
    path('company/',include(('Company.urls', 'company'),namespace='company')),
    path('role/',include(('role.urls', 'role'),namespace='role')),
    path('project/',include(('project.urls', 'project'),namespace='project')),
    path('devicechangerequest/',include(('devicechangerequest.urls', 'devicechangerequest'),namespace='devicechangerequest')),
    path('leave/',include(('leave.urls', 'leave'),namespace='leave')),
    path('task/',include(('task.urls', 'task'),namespace='task')),
    path('checktrackpro/',include(('checktrackpro.urls', 'checktrackpro'),namespace='checktrackpro')),
    path('investment-type/',include(('InvestmentType.urls', 'InvestmentType'),namespace='InvestmentType')),
    path('ClientMaster/',include(('ClientMaster.urls', 'ClientMaster'),namespace='ClientMaster')),
    path('shift/',include(('shift.urls', 'shift'),namespace='shift')),
    path('packet/',include(('packet.urls', 'packet'),namespace='packet')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
