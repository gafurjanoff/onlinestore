from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    image = models.URLField(null=True, blank=True, default="https://i.pinimg.com/control2/236x/9a/32/51/9a3251e176544a068d5d6c9f46d51a8e.jpg")
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.URLField(null=True, blank=True, default="https://i.pinimg.com/control2/236x/9a/32/51/9a3251e176544a068d5d6c9f46d51a8e.jpg")
    title = models.CharField(max_length=255)
    description = models.TextField()
    old_price = models.FloatField()
    current_price = models.FloatField()

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.description[:50]} - {self.category}"

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("product", "user"),)

    @property
    def total_price(self):
        return self.quantity * self.product.current_price

    def __str__(self) -> str:
        return f"{self.product.title    } - {self.user}"