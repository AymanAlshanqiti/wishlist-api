from django.shortcuts import render
from items.models import Item
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ItemListSerializer, ItemDetailSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrStaff

class ItemListView(ListAPIView):
	
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer

	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['name', 'description', 'image']

	permission_classes = [AllowAny,]


class ItemDetailView(RetrieveAPIView):

	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'

	permission_classes = [IsOwnerOrStaff,]

	

