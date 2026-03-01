from rest_framework import serializers
from .models import Dragon

class DragonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dragon
        fields = ["id", "name", "species", "owner", "diet", "habitat", "abilities", "size"]