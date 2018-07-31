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
        fields = ('name', 'email', 'message', 'date')


class PromoSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        model = PromoSection
        fields = ('title', 'text', 'image')


class PresentationSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        model = PresentationSection
        fields = ('title', 'sub_title', 'text1', 'text2', 'image')


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GallerySection
        fields = ('title', 'sub_title')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSection
        fields = ('title', 'sub_title', 'sub_title2', 'sub_title3')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSection
        fields = ('title', 'sub_title', 'g_api', 'g_place_id',
                  'g_review_all_url', 'g_review_new_url', 'reviews')

