from rest_framework import serializers
from mywebApp2.models import StudentDetails ,StudentDetails1

class SdSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields =( 'id',
        'Name' ,
        'age',
        'key' ,
        'gender'
        )

class SdSerializer1(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails1
        fields =( 'id',
        'product_name' ,
        'product_key'
        )
