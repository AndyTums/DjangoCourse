from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, category, order, contact, user_contact

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('category/', category, name='category'),
    path('order/', order, name='category'),
    path('contact/', contact, name='category'),
    path('user_contact/', user_contact, name='user_contact'),

]
