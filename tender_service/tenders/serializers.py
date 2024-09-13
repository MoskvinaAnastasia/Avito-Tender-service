from rest_framework import serializers

from .models import Bid, Organization, Review, Tender


class OrganizationSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Organization."""

    class Meta:
        model = Organization
        fields = '__all__'


class TenderSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Tender."""

    class Meta:
        model = Tender
        fields = '__all__'


class BidSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Offer."""

    class Meta:
        model = Bid
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Review."""

    class Meta:
        model = Review
        fields = '__all__'
