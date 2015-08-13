from rest_framework import serializers
from main.models import Area, Point
from django.contrib.auth.models import User


class PointSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()

    class Meta:
        model = Point
        fields = ('order', 'lat', 'lng', 'id',)


class AreaSerializer(serializers.ModelSerializer):
    points = PointSerializer(many=True)

    class Meta:
        model = Area
        fields = ('name', 'description',
                  'points', 'user', 'date_created', 'id', 'lat', 'lng')

    def create(self, validated_data):
        points_data = validated_data.pop('points')
        area = Area.objects.create(**validated_data)

        for point_data in points_data:
            Point.objects.create(area=area, **point_data)

        return area

    def update(self, instance, validated_data):
        points_data = validated_data.pop('points')
        points = instance.points.all()

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lng = validated_data.get('lng', instance.lng)
        instance.save()

        for point_data in points_data:
            point = instance.points.get(id=point_data['id'])
            point.order = point_data.get('order', point.order)
            point.lat = point_data.get('lat', point.lat)
            point.lng = point_data.get('lng', point.lng)
            point.save()

        return instance


class UserSerializer(serializers.ModelSerializer):
    areas = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all(),
                                               many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'areas',)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.save()

        return instance
