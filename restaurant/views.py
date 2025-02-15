from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Booking
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

@csrf_exempt
def book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Extract data
            first_name = data.get('first_name')
            reservation_date = data.get('reservation_date')
            reservation_slot = data.get('reservation_slot')

            # Validate data
            if not all([first_name, reservation_date, reservation_slot]):
                return JsonResponse({'error': 'Missing required fields'})

            # Check if slot is already booked
            existing_booking = Booking.objects.filter(
                reservation_date=reservation_date,
                reservation_slot=reservation_slot
            ).first()

            if existing_booking:
                return JsonResponse({'error': 'This time slot is already booked'})

            # Create booking
            booking = Booking.objects.create(
                first_name=first_name,
                reservation_date=reservation_date,
                reservation_slot=reservation_slot
            )
            return JsonResponse({'message': 'Booking successful'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    
    # If GET request, render the booking form
    return render(request, 'index.html')

def bookings(request, date=None):
    # If it's a regular request without date, show the bookings page
    if date is None:
        return render(request, 'bookings.html')
        
    # If it's an API request with date, return JSON data
    if request.method != 'GET':
        return JsonResponse({'error': 'Only GET method is allowed'})
        
    try:
        # Get bookings for specific date
        bookings = Booking.objects.filter(reservation_date=date)
        
        # Serialize the bookings
        booking_list = []
        for booking in bookings:
            booking_list.append({
                'id': booking.id,
                'first_name': booking.first_name,
                'reservation_date': booking.reservation_date.strftime('%Y-%m-%d'),
                'reservation_slot': booking.reservation_slot
            })
        
        return JsonResponse(booking_list, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)})

def format_booking_time(slot):
    return f"{slot}:00"
