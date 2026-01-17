from rest_framework import viewsets
from rest_framework.response import Response
from pokedex.models import Pokemon
from .serializers import PokemonSerializer
from pokedex.models import Trainer
from .serializers import TrainerSerializer
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    required_scopes = ['write']
    
    authentication_classes = [OAuth2Authentication]
    required_scopes = ["write"]
    
    def get_permissions(self):
        if self.request.method in ["POST","PUT","PATCH","DELETE"]:
            return [TokenHasScope(), IsAuthenticated()]
        return [AllowAny()]


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    authentication_classes = [OAuth2Authentication]
    required_scopes = ["write"]

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [TokenHasScope(), IsAuthenticated()]
        return [AllowAny()]