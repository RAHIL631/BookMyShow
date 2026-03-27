import os
import django
import random
from datetime import datetime, timedelta

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookmyseat.settings')
django.setup()

from movies.models import Movie, Theater, Seat

def populate():
    print("Starting data population...")
    
    # Sample Data for Categories
    categories = {
        'movie': [
            {'name': 'Interstellar', 'rating': '9.2', 'cast': 'Matthew McConaughey, Anne Hathaway', 'genre': 'Sci-Fi, Adventure', 'duration': '2h 49m'},
            {'name': 'The Dark Knight', 'rating': '9.5', 'cast': 'Christian Bale, Heath Ledger', 'genre': 'Crime, Action', 'duration': '2h 32m'},
            {'name': 'Inception', 'rating': '9.0', 'cast': 'Leonardo DiCaprio, Joseph Gordon-Levitt', 'genre': 'Action, Sci-Fi', 'duration': '2h 28m'},
        ],
        'event': [
            {'name': 'Lollapalooza Music Festival', 'rating': '8.8', 'cast': 'Dua Lipa, Imagine Dragons', 'genre': 'Music Festival', 'duration': '8h'},
            {'name': 'Global Tech Summit 2024', 'rating': '8.2', 'cast': 'Sundar Pichai, Satya Nadella', 'genre': 'Conference', 'duration': '6h'},
        ],
        'play': [
            {'name': 'The Lion King Musical', 'rating': '9.3', 'cast': 'Broadway Cast', 'genre': 'Musical, Drama', 'duration': '2h 30m'},
            {'name': 'Hamlet - Live', 'rating': '8.5', 'cast': 'Benedict Cumberbatch', 'genre': 'Classic, Tragedy', 'duration': '3h'},
        ],
        'sport': [
            {'name': 'Wimbledon Finals', 'rating': '9.0', 'cast': 'Djokovic vs Alcaraz', 'genre': 'Tennis', 'duration': '4h'},
            {'name': 'IPL Final 2024', 'rating': '9.6', 'cast': 'RCB vs MI', 'genre': 'Cricket', 'duration': '4h'},
        ],
        'activity': [
            {'name': 'Himalayan Trekking Expedition', 'rating': '9.4', 'cast': 'Professional Guides', 'genre': 'Adventure', 'duration': '4 Days'},
            {'name': 'Fine Wine Tasting', 'rating': '8.6', 'cast': 'Sommelier John', 'genre': 'Workshop', 'duration': '2h'},
        ]
    }

    # Theater Names
    theater_names = ["PVR Cinema", "INOX", "Cinepolis", "IMAX Screen 1", "Stardust Theater"]

    for cat_slug, items in categories.items():
        for item in items:
            # Create Movie/Show
            movie, created = Movie.objects.get_or_create(
                name=item['name'],
                defaults={
                    'rating': item['rating'],
                    'cast': item['cast'],
                    'description': f"Experience the magic of {item['name']}. A masterpiece in the {item['genre']} category.",
                    'category': cat_slug,
                    'genre': item['genre'],
                    'duration': item['duration'],
                    'language': 'English/Hindi',
                    'image': 'movies/default.jpg' # Assuming a default image exists or it will be handled
                }
            )
            
            if created:
                print(f"Created {cat_slug}: {item['name']}")
                # Create some Theaters/Sessions for this item
                for i in range(2):
                    t_name = random.choice(theater_names)
                    time = datetime.now() + timedelta(days=random.randint(1, 5), hours=random.randint(10, 22))
                    theater = Theater.objects.create(
                        name=t_name,
                        movie=movie,
                        time=time
                    )
                    
                    # Create some seats for this theater
                    for r in range(1, 6): # 5 rows
                        for c in range(1, 11): # 10 seats per row
                            Seat.objects.create(
                                theater=theater,
                                seat_number=f"{chr(64+r)}{c}",
                                is_booked=random.choice([True, False, False, False]) # 25% booked
                            )

    print("Population complete!")

if __name__ == "__main__":
    populate()
