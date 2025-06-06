# TravelAgentPro Booking Search Agent

This repository contains a simple Python script for searching hotels on Booking.com using the RapidAPI service.

## Requirements
- Python 3.11+
- `requests` library
- A RapidAPI key with access to the Booking.com API (set in the `BOOKING_RAPIDAPI_KEY` environment variable)

## Usage
Run the script with a destination city ID and check-in/check-out dates:

```bash
python booking_search_agent.py <city_id> <checkin_date> <checkout_date> [--adults N]
```

Example:

```bash
BOOKING_RAPIDAPI_KEY=YOUR_KEY python booking_search_agent.py -551262 2025-06-10 2025-06-15 --adults 2
```

The script prints up to ten results with the hotel name and price. If the request fails, an error message is shown.
