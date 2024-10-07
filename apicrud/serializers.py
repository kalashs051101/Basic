from rest_framework import serializers
from apicrud.models import *
from django.contrib.auth.models import User


class student_serializer(serializers.ModelSerializer):
    class Meta:
        model=api_student
        fields='__all__'


    def validate(self,data):
        if data['name']:
            for i in data['name']:
                if i.isdigit():
                    raise serializers.ValidationError({'error':'error occured'})

        if data['age']<18:
            raise serializers.ValidationError({'error':'error occured'})
        return data

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['username','password']

    def create(self,validated_data):  #it use for password hashing because password is not saved but now saved
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user