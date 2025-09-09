from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
import debug_toolbar.toolbar
from rest_framework.authtoken.views import obtain_auth_token

def home(request):
    return JsonResponse({
        "message": "Bookstore API",
        "version": "1.0.0",
        "endpoints": {
            "products": "/bookstore/v1/product/",
            "categories": "/bookstore/v1/category/",
            "orders": "/bookstore/v1/order/",
            "admin": "/admin/",
            "api_token": "/api-token-auth/"
        },
        "documentation": "Use the browsable API interface for testing"
    })

urlpatterns = [
    path("", home, name="home"),
    path("__debug__", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
