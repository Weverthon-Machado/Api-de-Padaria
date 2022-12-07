from rest_framework import viewsets
from Colaborador.models import Colaborador
from Colaborador.serializer import ColaboradorSerializer

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer