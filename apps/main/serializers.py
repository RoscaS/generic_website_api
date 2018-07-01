from rest_framework import serializers
from .models import Presentation, Hero
from apps.gallery.serializers import ImageSerializer


class PresentationSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        model = Presentation
        fields = ('title', 'sub_title', 'text1', 'text2', 'image')


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = (
        'icon1', 'icon2', 'icon3', 'title1', 'title2', 'title3', 'text1',
        'text2', 'text3',)
