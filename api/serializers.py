from rest_framework import serializers
from . import models


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Description
        fields = ["title", "context", "image"]


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        fields = "__all__"


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About_Us
        fields = "__all__"


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialNetwork
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["title", "image"]


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer()

    class Meta:
        model = models.Product
        fields = ["title", "category", "image", "text", "narx"]


class ImageSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = models.Image
        fields = ["product", "image"]
