from rest_framework import viewsets
from Fornecedor.models import Fornecedor
from Fornecedor.serializer import FornecedorSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer