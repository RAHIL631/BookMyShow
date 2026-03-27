from django.db import models
from django.contrib.auth.models import User 

class Movie(models.Model):
    name= models.CharField(max_length=255)
    image= models.ImageField(upload_to="movies/")
    rating = models.DecimalField(max_digits=3,decimal_places=1)
    cast= models.TextField()
    description= models.TextField(blank=True,null=True) # optional
    CATEGORY_CHOICES = [
        ('movie', 'Movie'),
        ('event', 'Event'),
        ('play', 'Play'),
        ('sport', 'Sport'),
        ('activity', 'Activity'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='movie')
    duration = models.CharField(max_length=50, default='2h')
    language = models.CharField(max_length=100, default='English')
    genre = models.CharField(max_length=100, default='Drama')
    release_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Theater(models.Model):
    name = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='theaters')
    time= models.DateTimeField()

    def __str__(self):
        return f'{self.name} - {self.movie.name} at {self.time}'

class Seat(models.Model):
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE,related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_booked=models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['theater', 'seat_number'], name='unique_seat_per_theater')
        ]

    def __str__(self):
        return f'{self.seat_number} in {self.theater.name}'

class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    seat=models.OneToOneField(Seat,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    theater=models.ForeignKey(Theater,on_delete=models.CASCADE)
    booked_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Booking by {self.user.username} for {self.seat.seat_number} at {self.theater.name}'