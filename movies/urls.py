from django.urls import path
from . import views
urlpatterns=[
    path('',views.movie_list,name='movie_list'),
    path('events/', views.movie_list, {'category': 'event'}, name='events'),
    path('plays/', views.movie_list, {'category': 'play'}, name='plays'),
    path('sports/', views.movie_list, {'category': 'sport'}, name='sports'),
    path('activities/', views.movie_list, {'category': 'activity'}, name='activities'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/theaters',views.theater_list,name='theater_list'),
    path('theater/<int:theater_id>/seats/book/',views.book_seats,name='book_seats'),
    path('booking/success/<str:booking_ids>/', views.booking_success, name='booking_success'),
]