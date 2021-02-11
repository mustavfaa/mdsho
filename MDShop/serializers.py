# backend/notes/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from .models import smartphone,Category

from rest_framework import serializers
from django.contrib.auth.models import User


from django.contrib.auth.models import User
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

               
class MDShopListSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = smartphone
        fields = '__all__'

    category = serializers.SlugRelatedField(slug_field="name", read_only=True)   


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
   

    class Meta:
        model = Customer
        fields = '__all__'






class MDShopSerializer(serializers.ModelSerializer):
    


    class Meta:
        model = smartphone
        fields = ("id", "img1", "img2", "img3", "img4", "img5", "img6","title","price","slug")


class MDShopCustomerSerializer(serializers.ModelSerializer):
    


    class Meta:
        model = smartphone
        fields = '__all__'


    

class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'



class CustomerLikeSerializer(serializers.ModelSerializer):
    likeNEW=MDShopSerializer( read_only=True)
    class Meta:
        model = CustomerLike
        fields = ("id", "likeNEW", "likeCustomer","created_at")

class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerLike
        fields = '__all__'





class MDShopDetailSerializer(serializers.ModelSerializer):
	

    class Meta:
        model = Category
        fields = '__all__'
class CustomerAddressSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = CustomerAddress
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    img1 = serializers.SerializerMethodField('get_image_url')
    img2 = serializers.SerializerMethodField('get_image_url')
    img3 = serializers.SerializerMethodField('get_image_url')
    img4 = serializers.SerializerMethodField('get_image_url')
    img5 = serializers.SerializerMethodField('get_image_url')
    img6 = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = smartphone
        fields = ("id", "img1", "img2", "img3", "img4", "img5", "img6","title","price","slug")
    def get_image_url(self, obj):
        return obj.image.url
    
    
class OrderCreateSerializer(serializers.ModelSerializer):
    smartphone=ShopSerializer(many=True)
    class Meta:
        model = order
        fields = '__all__'

    def create(self, validated_data):
        
        smartphone = validated_data.pop('smartphone')
        question = order.objects.create(**validated_data)
        question.smartphone.set(smartphone)
        return question

    

