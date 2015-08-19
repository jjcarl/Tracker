from rest_framework import serializers
from main.models import Area, Point
from django.contrib.auth.models import User


class PointSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)

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
    areas = serializers.PrimaryKeyRelatedField(
        queryset=Area.objects.all(), many=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'email', 'first_name', 'last_name', 'areas',)
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
            )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.save()

        return instance
