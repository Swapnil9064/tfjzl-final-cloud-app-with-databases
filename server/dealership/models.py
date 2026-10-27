from django.db import models
class Dealer(models.Model):
    full_name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=20, blank=True)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    short_name = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    def __str__(self): return self.full_name
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    def __str__(self): return self.name
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField(null=True, blank=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL, null=True, blank=True, related_name="cars")
class DealerReview(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=100)
    review = models.TextField()
    sentiment = models.CharField(max_length=30, default="neutral")
