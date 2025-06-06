import os
import requests
from datetime import datetime
from typing import List, Dict

BOOKING_API_HOST = "booking-com.p.rapidapi.com"
BOOKING_API_KEY_ENV = "BOOKING_RAPIDAPI_KEY"

def search_hotels(city_id: str, checkin: str, checkout: str, adults: int = 1) -> List[Dict]:
    """Search hotels on Booking.com via RapidAPI.

    Args:
        city_id: Destination city identifier from Booking.com.
        checkin: Check-in date in YYYY-MM-DD format.
        checkout: Check-out date in YYYY-MM-DD format.
        adults: Number of adults.

    Returns:
        A list of hotel data dictionaries or an empty list on failure.
    """
    api_key = os.getenv(BOOKING_API_KEY_ENV)
    if not api_key:
        raise RuntimeError(f"Set the {BOOKING_API_KEY_ENV} environment variable.")

    url = f"https://{BOOKING_API_HOST}/v1/hotels/search"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": BOOKING_API_HOST,
    }
    params = {
        "checkout_date": checkout,
        "units": "metric",
        "dest_id": city_id,
        "dest_type": "city",
        "locale": "en-gb",
        "checkin_date": checkin,
        "adults_number": adults,
        "order_by": "popularity",
        "filter_by_currency": "USD",
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
        return []

    data = response.json()
    return data.get("result", [])


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Search Booking.com for hotels")
    parser.add_argument("city_id", help="Destination city ID")
    parser.add_argument("checkin", help="Check-in date YYYY-MM-DD")
    parser.add_argument("checkout", help="Check-out date YYYY-MM-DD")
    parser.add_argument("--adults", type=int, default=1, help="Number of adults")
    args = parser.parse_args()

    try:
        results = search_hotels(args.city_id, args.checkin, args.checkout, args.adults)
    except RuntimeError as err:
        print(err)
        return

    print(f"Found {len(results)} results")
    for hotel in results[:10]:
        name = hotel.get("hotel_name", "Unknown")
        price = hotel.get("min_total_price")
        currency = hotel.get("currencycode")
        print(f"{name} - {price} {currency}")


if __name__ == "__main__":
    main()
