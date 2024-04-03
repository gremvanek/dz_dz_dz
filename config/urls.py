from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from config.views import ContactView, PostCreateView, PostDetailView, PostUpdateView, \
    PostDeleteView, PostListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, \
    ProductListView, VersionListView, VersionDetailView, VersionCreateView, VersionUpdateView, VersionDeleteView

urlpatterns = [
                  path('post_list/', PostListView.as_view(), name='post_list'),
                  path('contacts/', ContactView.as_view(), name='contacts'),
                  path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
                  path('post_list/create/', PostCreateView.as_view(), name='create_view'),
                  path('<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
                  path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
                  path('', ProductListView.as_view(), name='product_list'),
                  path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
                  path('product/create/', ProductCreateView.as_view(), name='product_create'),
                  path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
                  path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
                  path('product/<int:product_id>/versions/', VersionListView.as_view(), name='product_versions_list'),
                  path('version/<int:pk>/', VersionDetailView.as_view(), name='version_detail'),
                  path('version/new/', VersionCreateView.as_view(), name='version_create'),
                  path('version/<int:pk>/edit/', VersionUpdateView.as_view(), name='version_update'),
                  path('version/<int:pk>/delete/', VersionDeleteView.as_view(), name='version_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
