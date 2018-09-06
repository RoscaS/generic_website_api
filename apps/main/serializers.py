from rest_framework import serializers
from apps.gallery.serializers import ImageSerializer
from .models import PresentationSection, HeroSection, EventsSection, \
    ContactSection, SiteOptions, Message, ReviewSection, PromoSection, \
    ArticlesSection, AuthTest, SiteInformations, SiteContact


class AuthTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthTest
        fields = ('id', 'title', 'text')


class SiteOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteOptions
        # fields = '__all__'
        exclude = ('id',)


class SiteInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteInformations
        fields = '__all__'


class SiteContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteContact
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    date = serializers.ReadOnlyField()

    class Meta:
        model = Message
        fields = ('id', 'name', 'email', 'message', 'date')


class PromoSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        model = PromoSection
        # fields = ('id', 'title', 'text', 'image')
        exclude = ('id',)


class PresentationSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        model = PresentationSection
        # fields = ('id', 'title', 'sub_title', 'text1', 'text2', 'image')
        exclude = ('id',)


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        # fields = '__all__'
        exclude = ('id',)


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsSection
        # fields = ('id', 'title', 'sub_title')
        exclude = ('id', 'header')


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlesSection
        # fields = ('id', 'title', 'sub_title')
        exclude = ('id', 'header')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSection
        # fields = ('id', 'title', 'sub_title', 'sub_title2', 'sub_title3')
        exclude = ('id', 'header')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSection
        fields = ('name', 'title', 'sub_title', 'g_api', 'g_place_id',
                  'g_review_all_url', 'g_review_new_url', 'reviews')

