from rest_framework import viewsets
from Cliente.models import Cliente
from Cliente.serializer import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer