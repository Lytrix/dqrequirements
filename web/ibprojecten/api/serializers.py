from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

from rest_framework import serializers
from ibprojecten.api.models import (Product,
                                    ProductType,
                                    Requirement,
                                    Scope,
                                    ScopeType,
                                    Criteria,
                                    CriteriaType,
                                    Dimension,
                                    SubDimension,
                                    SubDimensionType,
                                    DataElement,
                                    )


class CriteriaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent the Hoofdtype model """
    class Meta:
        model = Criteria
        fields = '__all__'


class CriteriaTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Hoofdtype model """
    class Meta:
        model = CriteriaType
        fields = '__all__'


class DimensionSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent the Hoofdtype model """
    class Meta:
        model = Dimension
        fields = '__all__'


class SubDimensionSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent the Hoofdtype model """
    class Meta:
        model = SubDimension
        fields = '__all__'


class SubDimensionTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Werkordertype model """
    class Meta:
        model = SubDimensionType
        fields = '__all__'


class DataElementSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = DataElement
        fields = '__all__'


class ScopeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = Scope
        fields = '__all__'


class ScopeTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = ScopeType
        fields = '__all__'


class ScopeTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = ScopeType
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = Product
        fields = '__all__'

# class SubDimensionSerializer(GeoFeatureModelSerializer):
#     """ Serializer to represent the Werkorder model """
    
#     class Meta:
#         model = Werkorder
#         fields = ['werkorderType',
#                   'startdatum',
#                   'einddatum',
#                   'Timetellnummer',
#                   'Boekingscombinatie']

class RequirementSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Organisation model """
    class Meta:
        model = Requirement
        fields = '__all__'
        depth = 3


#class EmployeeField(serializers.StringRelatedField):
#    def to_representation(self, value):
#        return ('{} {}'.format(value.Voornaam, value.Achternaam),value.Email)
    #def get_huurder(self, obj):
    #    vo = obj.Ambtelijkopdrachtgever
    #   request = self.context.get('request')
    #   return EmployeeDetailSerializer(vo, many=False, context={'request':request}).data

# class WerkorderField(serializers.StringRelatedField):
#     def to_representation(self, value):
#         return ('{}'.format(value.WerkorderType))
