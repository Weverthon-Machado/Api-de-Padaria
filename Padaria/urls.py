from django.contrib import admin
from django.urls import path, include
from Produto.views import ProdutoViewSet
from Cliente.views import ClienteViewSet
from Colaborador.views import ColaboradorViewSet
from Fornecedor.views import FornecedorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register (r'produto', ProdutoViewSet) 
router.register (r'cliente', ClienteViewSet)
router.register (r'colaborador', ColaboradorViewSet) 
router.register (r'fornecedor', FornecedorViewSet) 
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls))

]
