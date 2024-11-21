from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import OrderListView, ContactView, user_contact, ProductDetailView, \
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category'),
    path('order/', OrderListView.as_view(), name='order'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/user_contact/', user_contact, name='user_contact'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
