from django.contrib import admin
from .models import Movie, Theater, Seat,Booking

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'rating', 'language', 'genre']
    list_filter = ['category', 'language', 'genre']
    search_fields = ['name', 'cast']

@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ['name', 'movie', 'time']
    list_filter = ['movie', 'time']
    search_fields = ['name']

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['theater', 'seat_number', 'is_booked']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'theater', 'seat', 'booked_at']
    list_filter = ['movie', 'theater', 'booked_at']
    search_fields = ['user__username', 'movie__name']
