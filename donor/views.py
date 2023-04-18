from django.shortcuts import HttpResponse
from donor.models import Wilaya,Daiira,BloodType,Donor
from rest_framework.decorators import api_view
from donor.Serializers import WilayaSerializer,BloodTypeSerializer,DonorSerializer,DaiiraSerializer,DonorSerializerPOST
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status




@api_view(['GET'])
def get_wilayate(request):
    wilaya = Wilaya.objects.all()
    serializeData = WilayaSerializer(wilaya, many=True)
    return Response(serializeData.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_daiira(request, wilayaNum):
    daiira = Daiira.objects.filter(wilaya_n=wilayaNum)
    serializeData = DaiiraSerializer(daiira, many=True)
    return Response(serializeData.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_blood_types(request):
    blood = BloodType.objects.all()
    serializeData = BloodTypeSerializer(blood, many=True)
    return Response(serializeData.data, status=status.HTTP_200_OK)

@api_view(['POST','GET'])
def donor(request):
    if request.method == 'POST':
        serializer = DonorSerializerPOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, tatus=status.HTTP_200_OK)
        raise ValidationError('wrong data')
    
    elif request.method == 'GET':
        donor = Donor.objects.all()
        serializeData = DonorSerializer(donor, many=True)
        if not serializeData.data:
            return Response({'message': 'No data available.'}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializeData.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def search_donor(request,bloodtype,wilaya,daiira):
    
    if Wilaya.objects.get(number=wilaya).name != Daiira.objects.get(number=daiira).name:
        donor = Donor.objects.filter(blood=bloodtype,wilaya=wilaya,daiira=daiira)
    else:
        donor = Donor.objects.filter(blood=bloodtype,wilaya=wilaya)


    serializeData = DonorSerializer(donor, many=True)
    if not serializeData.data:
        return Response({'message': 'No data available.'}, status=status.HTTP_204_NO_CONTENT)
    
    return Response(serializeData.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def search_donor_using_bloodType_and_wilaya(request,bloodtype,wilaya):
    
    donor = Donor.objects.filter(blood=bloodtype,wilaya=wilaya)
    serializeData = DonorSerializer(donor, many=True)

    if not serializeData.data:
        return Response({'message': 'No data available.'}, status=status.HTTP_204_NO_CONTENT)
    
    return Response(serializeData.data,status=status.HTTP_200_OK)
    