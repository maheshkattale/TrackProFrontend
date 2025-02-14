from django.contrib import admin
from django.urls import path, include, re_path
from . import views as v
# from django.conf.urls import url
urlpatterns = [
    path('investment-list', v.investmentlist, name='investment-list'),
    path('update-investment', v.updateinvestment, name='update-investment'),
    path('delete-investment/<int:id>', v.deleteinvestment, name='delete-investment'),
    path('section', v.sectionlist, name='section'),
    path('update-section', v.updatesection, name='update-section'),
    path('delete-section/<int:id>', v.deletesection, name='delete-section'),   
    path('configuration-list', v.configurationlist, name='configuration-list'),   
]