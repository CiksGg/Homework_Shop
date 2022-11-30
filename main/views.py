from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

User = get_user_model()

# Create your views here.
@api_view(['GET'])
def post_list(request):
    queryset = Product.objects.all().order_by('id')
    serializer = ProductSerializer(queryset, many=True)
    return Response (serializer.data, status=200)