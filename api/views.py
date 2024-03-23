from rest_framework.response import Response
from . import models
from rest_framework.views import APIView
from . import serializers, models

from rest_framework import generics

# Create your views here.


class home(APIView):

    def get(self, request):

        description = models.Description.objects.last()
        descriptionserializer = serializers.DescriptionSerializer(
            description, many=False
        )

        social = models.SocialNetwork.objects.last()
        socialserializer = serializers.SocialsSerializer(social, many=False)

        category = models.Category.objects.all()
        categoryserializer = serializers.CategorySerializer(category, many=True)

        product = models.Product.objects.all()
        productserializer = serializers.ProductSerializer(product, many=True)


        data = {
            'description': descriptionserializer.data,
            'socials': socialserializer.data,
            'category': categoryserializer.data,
            'products': productserializer.data

        }    
        return Response(data=data, status=200)

class BranchList(generics.ListAPIView):
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer

class AboutUs(generics.ListAPIView):
    queryset = models.AboutUs.objects.all()
    serializer_class = serializers.AboutUsSerializer


