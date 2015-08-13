from rest_framework import serializers
from main.models import Area, Point
from django.contrib.auth.models import User


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('order', 'lat', 'lng', 'id',)


class AreaSerializer(serializers.ModelSerializer):
    points = PointSerializer(many=True)

    class Meta:
        model = Area
        fields = ('name', 'description',
                  'points', 'user', 'date_created', 'id',)

    def create(self, validated_data):
        points_data = validated_data.pop('points')
        area = Area.objects.create(**validated_data)

        for point_data in points_data:
            Point.objects.create(area=area, **point_data)

        return area

    def update(self, instance, validated_data):
        points_data = validated_data.pop('points')
        points = instance.points

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.user = validated_data.get('user', instance.user)
        instance.date_created = validated_data.get('date_created',
                                                   instance.date_created)
        instance.save()

        points.lat = validated_data.get('lat', points.username)
        points.lng = validated_data.get('lng', points.lng)
        points.order = validated_data.get('order', points.order)
        points.area = validated_data.get('area', points.area)
        points.save()


class UserSerializer(serializers.ModelSerializer):
    areas = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all(),
                                               many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'areas',)
