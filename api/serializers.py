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
        model = models.AboutUs
        fields = "__all__"


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialNetwork
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = ["product", "image"]

class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    images = ImageSerializer()

    class Meta:
        model = models.Product
        fields = ["title", "category", "image", "text", "narx"]



