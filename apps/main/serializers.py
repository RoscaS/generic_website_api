from rest_framework import serializers
from .models import PresentationSection, HeroSection, GallerySection, \
    ContactSection, MainOptions, Message, ReviewSection, PromoSection
from apps.gallery.serializers import ImageSerializer


class MainOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainOptions
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    date = serializers.ReadOnlyField()

    class Meta:
        model = Message
        fields = '__all__'


class PromoSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        model = PromoSection
        fields = '__all__'


class PresentationSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        model = PresentationSection
        fields = '__all__'


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GallerySection
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSection
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSection
        fields = '__all__'
