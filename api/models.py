from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _


class Description(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField()
    image = models.ImageField(upload_to="DescriptionImages/")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _("Description")
        verbose_name_plural = _("Descriptions")


class Branch(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    ish_vaqti = models.CharField(max_length=100)
    number = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Branch")
        verbose_name_plural = _("Branchs")

class About_Us(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="AboutUsImage/")
    text = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("AboutUs")


class SocialNetwork(models.Model):
    telegram = models.CharField(max_length = 100, blank=True, null=True)
    instagram = models.CharField(max_length = 100, blank=True, null=True)
    facebook = models.CharField(max_length = 100, blank=True, null=True)
    twitter = models.CharField(max_length = 100, blank=True, null=True)



    class Meta:
        verbose_name = _("Social")
        verbose_name_plural = _("Socials")



#PRODUCTS        

class Category(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="categoryImages/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image/")
    text = models.TextField()
    narx = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return f"product/{self.pk}/"

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productimage")
    image = models.ImageField(verbose_name="Images product uchun", upload_to="iamges/")

    def __str__(self) -> str:
        return self.product

