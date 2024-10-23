from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, category, order, contact, user_contact, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('category/', category, name='category'),
    path('order/', order, name='category'),
    path('contact/', contact, name='category'),
    path('contact/', user_contact, name='user_contact'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
