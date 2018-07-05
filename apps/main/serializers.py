from rest_framework import serializers
from .models import PresentationSection, HeroSection, GallerySection, \
    ContactSection, MainOptions, Message, ReviewSection
from apps.gallery.serializers import ImageSerializer


class MainOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainOptions
        fields = ('project_name', 'name', 'name_add', 'description', 'oppening', 'adress', 'city',
            'post_code', 'phone', 'mail', 'facebook', 'tripadvisor',
            'google', 'twitter', 'instagram', 'linkedin', 'snapchat')


class MessageSerializer(serializers.ModelSerializer):
    date = serializers.ReadOnlyField()

    class Meta:
        model = Message
        fields = ('name', 'email', 'message', 'date')


class PresentationSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        model = PresentationSection
        fields = ('title', 'sub_title', 'text1', 'text2', 'image')


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = (
            'icon1', 'icon2', 'icon3', 'title1', 'title2', 'title3', 'text1',
            'text2', 'text3',)


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
