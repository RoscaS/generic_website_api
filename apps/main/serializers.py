from rest_framework import serializers
from .models import Presentation
from apps.gallery.serializers import ImageSerializer

class PresentationSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)
    # image = serializers.ReadOnlyField(source='image.image.url')
    # image = serializers.HyperlinkedRelatedField(view_name='image-detail', read_only=True)


    class Meta:
        model = Presentation
        fields = ('title', 'sub_title', 'text1', 'text2', 'image')

