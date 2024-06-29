# views.py

from rest_framework import viewsets, permissions
from .models import AntiqueProduct, Bidding
from .serializers import AntiqueProductSerializer, BiddingSerializer, AntiqueProductListSerializer
from rest_framework.authentication import SessionAuthentication


class AntiqueProductViewSet(viewsets.ModelViewSet):
    queryset = AntiqueProduct.objects.all()
    serializer_class = AntiqueProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        if self.action in ['list', 'retrieve']:  
            return AntiqueProduct.objects.exclude(user=self.request.user)
        else:
            return AntiqueProduct.objects.filter(user=self.request.user)

class BiddingViewSet(viewsets.ModelViewSet):
    queryset = Bidding.objects.all()
    serializer_class = BiddingSerializer
    permission_classes = [permissions.IsAuthenticated]


class AntiqueProductListViewSet(viewsets.ModelViewSet):
    queryset = AntiqueProduct.objects.all()
    serializer_class = AntiqueProductListSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

    def get_queryset(self):
        return AntiqueProduct.objects.filter(user=self.request.user).prefetch_related('biddings')