from rest_framework import serializers
from .models import AddModel


class AddSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddModel
        fields = ("first_number", "second_number",)


class TotalSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddModel
        fields = ("total",)
