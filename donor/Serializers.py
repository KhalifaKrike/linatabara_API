from rest_framework import serializers
from donor.models import BloodType,Daiira,Donor,Wilaya

class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = '__all__'


class DaiiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daiira
        fields = '__all__'

class DonorSerializer(serializers.ModelSerializer):
    blood = serializers.CharField(source='blood.type')
    wilaya = serializers.CharField(source='wilaya.name')
    daiira = serializers.CharField(source='daiira.name')
    class Meta:
        model = Donor
        fields = '__all__'
class DonorSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'

class WilayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields = '__all__'

