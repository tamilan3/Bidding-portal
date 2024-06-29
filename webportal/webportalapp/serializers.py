# serializers.py

from rest_framework import serializers
from .models import AntiqueProduct, Bidding

class AntiqueProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntiqueProduct
        fields = ['id', 'title', 'image', 'description', 'starting_price', 'user','bidding_closed']

class BiddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidding
        fields = ['id', 'product', 'bidder', 'bidding_price', 'bid_time']

    def validate_bidding_price(self, value):
        product = self.instance.product if self.instance else self.initial_data.get('product')
        last_bidding = Bidding.objects.filter(product=product).order_by('-id').first()
        product = AntiqueProduct.objects.get(id=product)
        if last_bidding:
            highest_price = max(product.starting_price, last_bidding.bidding_price)
        else:
            highest_price = product.starting_price

        if value <= highest_price:
            raise serializers.ValidationError('Bidding price must be greater than the starting price or last bidding price.')

        return value
    
    def validate(self, data):
        product_id = data.get('product')
        try:
            product = AntiqueProduct.objects.get(id=product_id.id)
        except AntiqueProduct.DoesNotExist:
            raise serializers.ValidationError("AntiqueProduct does not exist.")

        if product.bidding_closed:
            raise serializers.ValidationError("Bidding for this product is closed.")

        return data


class AntiqueProductListSerializer(serializers.ModelSerializer):
    biddings = BiddingSerializer(many=True, read_only=True)

    class Meta:
        model = AntiqueProduct
        fields = ['id', 'title', 'image', 'description', 'starting_price', 'biddings']

    
