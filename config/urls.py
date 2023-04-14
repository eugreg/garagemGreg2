from django.contrib import admin
from django.urls import  include, path  

from rest_framework.routers import DefaultRouter

from garagem.views import MarcaViewSet, AcessorioViewSet , VeiculoViewSet , CategoriaViewSet, CorViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"acessorio", AcessorioViewSet)
router.register(r"veiculo", VeiculoViewSet)
router.register(r"categoria", CategoriaViewSet)
router.register(r"cor", CorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
