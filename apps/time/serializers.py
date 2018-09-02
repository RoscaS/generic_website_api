from rest_framework import serializers
from .models import Day, Slot


class SlotSerializer(serializers.ModelSerializer):
    day = serializers.SlugRelatedField(slug_field='slug', queryset=Day.objects.all())

    class Meta:
        model = Slot
        fields = '__all__'


class DaySerializer(serializers.ModelSerializer):
    slots = SlotSerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = '__all__'
