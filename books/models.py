from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    number = models.CharField(max_length=255, blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    read_date = models.CharField(max_length=255, blank=True, null=True)
    add_date = models.DateTimeField('date added')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class Review(models.Model):
    NO_STARS = '☆☆☆☆☆'
    ONE_STAR = '★☆☆☆☆'
    TWO_STARS = '★★☆☆☆'
    THREE_STARS = '★★★☆☆'
    FOUR_STARS = '★★★★☆'
    FIVE_STARS = '★★★★★'
    REVIEW_CHOICES = [
        (NO_STARS, 'No stars'),
        (ONE_STAR, 'One star'),
        (TWO_STARS, 'Two stars'),
        (THREE_STARS, 'Three stars'),
        (FOUR_STARS, 'Four stars'),
        (FIVE_STARS, 'Five stars')
    ]
    book = models.OneToOneField(
        Book,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    stars = models.CharField(max_length=255, choices=REVIEW_CHOICES, default=NO_STARS)
    thoughts = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.stars