from django.urls import path, include
from quotes_api.views import QuotesView
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'quotes', QuotesView)

urlpatterns = [
    path('', include(router.urls)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)