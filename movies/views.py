from django.shortcuts import render, redirect ,get_object_or_404
from .models import Movie,Theater,Seat,Booking
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

def movie_list(request, category=None):
    search_query = request.GET.get('search')
    category_query = category or request.GET.get('category')
    language_query = request.GET.get('language')
    
    movies = Movie.objects.all()
    
    if search_query:
        movies = movies.filter(name__icontains=search_query)
    
    if category_query:
        movies = movies.filter(category=category_query)
    
    if language_query:
        movies = movies.filter(language__icontains=language_query)
        
    return render(request, 'movies/movie_list.html', {
        'movies': movies, 
        'active_category': category_query,
        'active_language': language_query
    })

def theater_list(request,movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    theater=Theater.objects.filter(movie=movie)
    return render(request,'movies/theater_list.html',{'movie':movie,'theaters':theater})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})



@login_required(login_url='/login/')
def book_seats(request, theater_id):
    theaters = get_object_or_404(Theater, id=theater_id)
    seats = Seat.objects.filter(theater=theaters)
    if request.method == 'POST':
        selected_Seats = request.POST.getlist('seats')
        error_seats = []
        booking_ids = []
        if not selected_Seats:
            return render(request, "movies/seat_selection.html", {'theater': theaters, "seats": seats, 'error': "No seat selected"})
        
        for seat_id in selected_Seats:
            seat = get_object_or_404(Seat, id=seat_id, theater=theaters)
            if seat.is_booked:
                error_seats.append(seat.seat_number)
                continue
            try:
                booking = Booking.objects.create(
                    user=request.user,
                    seat=seat,
                    movie=theaters.movie,
                    theater=theaters
                )
                booking_ids.append(str(booking.id))
                seat.is_booked = True
                seat.save()
            except IntegrityError:
                error_seats.append(seat.seat_number)
        
        if error_seats:
            error_message = f"The following seats are already booked: {','.join(error_seats)}"
            return render(request, 'movies/seat_selection.html', {'theater': theaters, "seats": seats, 'error': error_message})
        
        return redirect('booking_success', booking_ids=','.join(booking_ids))
    
    return render(request, 'movies/seat_selection.html', {'theaters': theaters, "seats": seats})

@login_required
def booking_success(request, booking_ids):
    ids = booking_ids.split(',')
    bookings = Booking.objects.filter(id__in=ids, user=request.user)
    if not bookings:
        return redirect('profile')
    
    total_price = len(bookings) * 250  # Assuming a flat price for now
    
    return render(request, 'movies/booking_success.html', {
        'bookings': bookings,
        'total_price': total_price,
        'movie': bookings[0].movie,
        'theater': bookings[0].theater
    })


def run_migrations(request):
    try:
        from django.core.management import call_command
        from django.http import HttpResponse
        import os
        
        # Run Migrations
        call_command('migrate', interactive=False)
        
        # Populate Data if needed
        from .models import Movie
        if Movie.objects.count() == 0:
            try:
                from populate_db import populate
                populate()
            except ImportError:
                # Fallback if populate_db is not importable
                pass
                
        return HttpResponse("""
            <div style="font-family: sans-serif; text-align: center; padding: 50px;">
                <h1 style="color: #10b981;">Success! 🚀</h1>
                <p>Database migrations and data population are complete.</p>
                <a href="/" style="display: inline-block; padding: 10px 20px; background: #3b82f6; color: white; text-decoration: none; border-radius: 5px; margin-top: 20px;">Go to Home</a>
                <p style="font-size: 0.8em; color: #6b7280; margin-top: 20px;">(You may need to refresh the home page twice to see new data)</p>
            </div>
        """)
    except Exception as e:
        return HttpResponse(f"<h1>Error!</h1><p>{str(e)}</p>")

