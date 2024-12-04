from proyects.models import Proyecto
from rest_framework import viewsets, permissions
from .serializers import ProyectoSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Proyecto.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ProyectoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()