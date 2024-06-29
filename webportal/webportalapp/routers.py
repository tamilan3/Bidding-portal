from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AntiqueProductViewSet,BiddingViewSet,AntiqueProductListViewSet

router = DefaultRouter()
router.register(r'antiqueproducts', AntiqueProductViewSet, basename='antiqueproduct')
router.register(r'biddings', BiddingViewSet, basename='bidding')
router.register(r'antiqueproductslist',AntiqueProductListViewSet,basename='antiqueproductlist')



