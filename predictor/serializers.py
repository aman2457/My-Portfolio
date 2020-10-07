from rest_framework import serializers
from . models import price_predictor

class price_predictorSerializers(serializers.ModelSerializer):
    class Meta:
        model = price_predictor
        fields = ('location','square_fit','bath','bhk')
