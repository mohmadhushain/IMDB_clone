from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):

  review_user  = serializers.StringRelatedField(read_only=True)

  class Meta:
    model = Review
    # fields = '__all__'
    exclude = ('watchlist',)



class WatchListSerializer(serializers.ModelSerializer):
  # review = ReviewSerializer(many=True,read_only=True)
  # len_name = serializers.SerializerMethodField()
  platform = serializers.CharField(source='platform.name')
  class Meta:
    model = WatchList
    fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):

  watchlist = WatchListSerializer(many=True, read_only=True)
  # len_name = serializers.SerializerMethodField()

  class Meta:
    model = StreamPlatform
    fields = '__all__'
  
  







  # def get_len_name(self,object):
  #   return len(object.name)


  # def validate(self, data):
  #   if data['name'] == data['description']:
  #     raise serializers.ValidationError("Nmae and Description should be different")
  #   else:
  #     return data


  
  # def validate_name(self,value):
  #   if len(value) < 2:
  #     raise serializers.ValidationError("name is too short")
  #   else:
  #     return value

  

# def name_length(value):
#   if len(value) < 2:
#       raise serializers.ValidationError("name is too short")

# class MovieSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   name  = serializers.CharField(validators=[name_length], max_length=100)
#   description = serializers.CharField( max_length=200)
#   active  = serializers.BooleanField(default=True)

#   def create(self, validated_data):
#     return Movie.objects.create(**validated_data)
  
#   def update(self, instance, validated_data):
#     instance.name = validated_data.get('name',instance.name)
#     instance.description = validated_data.get('description',instance.description)
#     instance.active = validated_data.get('active',instance.active)
#     instance.save()
#     return instance
  

#   def validate(self, data):
#    if data['name'] == data['description']:
#      raise serializers.ValidationError("Nmae and Description should be different")
#    else:
#      return data


  # def validate_name(self,value):

  #   if len(value) < 2:
  #     raise serializers.ValidationError("name is too short")
  #   else:
  #     return value
    
