import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookmyseat.settings')
django.setup()

from movies.models import Movie

def update_images():
    print("Updating movie images in database...")
    
    image_map = {
        'Interstellar': 'movies/interstellar.png',
        'The Dark Knight': 'movies/dark_knight.png',
        'Inception': 'movies/inception.png',
        'Lollapalooza Music Festival': 'movies/lollapalooza.png',
        'Global Tech Summit 2024': 'movies/tech_summit.png',
        'The Lion King Musical': 'movies/lion_king.png',
        'Hamlet - Live': 'movies/hamlet.png',
        'Wimbledon Finals': 'movies/wimbledon.png',
        'IPL Final 2024': 'movies/ipl.png',
        'Himalayan Trekking Expedition': 'movies/himalayan_trek.png',
        'Fine Wine Tasting': 'movies/wine_tasting.png'
    }

    for name, path in image_map.items():
        try:
            movie = Movie.objects.get(name=name)
            movie.image = path
            movie.save()
            print(f"Updated image for: {name}")
        except Movie.DoesNotExist:
            print(f"Movie not found: {name}")

    print("Database update complete!")

if __name__ == "__main__":
    update_images()
