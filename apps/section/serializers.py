from rest_framework import serializers

from .models import Section, Gallery

class SectionSerializer(serializers.ModelSerializer):
    gallery = serializers.SlugRelatedField(slug_field='slug', read_only=True, required=False)

    def create(self, validated_data):
        gallery = Gallery.objects.create(
            slug=validated_data['name'].capitalize(),
            name=validated_data['name'].capitalize(),
            description='',
            limit=1
        )
        validated_data['gallery'] = gallery
        gallery.set_placeholder()
        return super().create(validated_data)

    class Meta:
        model = Section
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        fields = '__all__'


# class GenericSectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GenericSection
#         fields = '__all__'


