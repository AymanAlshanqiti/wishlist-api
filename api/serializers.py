from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']



class UserFavoriteItemSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = FavoriteItem
        fields = ['user']
		


class ItemListSerializer(serializers.ModelSerializer):

	detail = serializers.HyperlinkedIdentityField(
	view_name = 'api-item-detail',
	lookup_field = 'id',
	lookup_url_kwarg = 'item_id'
	)

	favorited = serializers.SerializerMethodField()

	added_by = UserSerializer()

	def get_favorited(self, obj):
		return obj.favs.count()

	class Meta:
		model = Item
		fields = ['id', 'image', 'name', 'description', 'detail', 'added_by', 'favorited']


class ItemDetailSerializer(serializers.ModelSerializer):

	favs = UserFavoriteItemSerializer(many=True)
	class Meta:
		model = Item
		fields = ['id', 'image', 'name', 'description', 'added_by', 'favs']


