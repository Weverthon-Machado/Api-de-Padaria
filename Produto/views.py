from rest_framework import viewsets
from Produto.models import Produto
from Produto.serializer import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer