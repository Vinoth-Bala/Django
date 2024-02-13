from rest_framework import serializers
from .models import students,Department

class stu_serializer(serializers.ModelSerializer):

    class Meta:
        model=students
        fields = '__all__'


class dept_serializer(serializers.ModelSerializer):

    class Meta:
        model=Department
        fields = '__all__'