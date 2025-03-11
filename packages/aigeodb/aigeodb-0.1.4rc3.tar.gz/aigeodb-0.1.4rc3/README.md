# AigeoDB

A Python package for working with world cities, countries, regions database. This package provides easy access to a comprehensive database of world locations.

## About

Developed by [Unrealos Inc.](https://unrealos.com/) - We create innovative SaaS and PaaS solutions powered by AI for business. Our expertise includes:
- AI-powered business solutions
- SaaS platforms
- PaaS infrastructure
- Custom enterprise software

## Features

- Easy-to-use interface for querying geographical data
- Built-in database downloader and updater
- Support for searching cities, countries, and regions
- Geolocation features (nearby cities search)
- SQLAlchemy models for all database entities
- Django integration with custom model fields

## Installation

Basic installation:
```bash
pip install aigeodb
```

## Core Usage

### Basic Example

```python
from aigeodb import DatabaseManager

# Initialize the database manager
db = DatabaseManager()

# Search for cities
cities = db.search_cities("Moscow", limit=5)
for city in cities:
    print(f"{city.name}, {city.country_code}")

# Get country information
country = db.get_country_info("US")
print(country.name, country.iso2)

# Find nearby cities
nearby = db.get_nearby_cities(40.7128, -74.0060, radius_km=100)
for city in nearby:
    print(f"{city.name}, {city.state_code}")
```

### API Reference

```python
# DatabaseManager methods
db = DatabaseManager()

# Search cities by name
cities = db.search_cities("Moscow", limit=5)

# Get country information
country = db.get_country_info("US")

# Calculate distance between two points
new_york = (40.7128, -74.0060)  # (latitude, longitude)
london = (51.5074, -0.1278)
distance = db.calculate_distance(new_york, london)
print(f"Distance between cities: {distance:.1f}km")

# Find nearby cities (simple usage)
cities = db.get_nearby_cities(
    latitude=40.7128, 
    longitude=-74.0060,
    radius_km=100,
    limit=10
)
for city in cities:
    print(f"{city.name}, {city.state_code}")

# Find nearby cities with distances
cities_with_distances = db.get_nearby_cities(
    latitude=40.7128,
    longitude=-74.0060,
    radius_km=100,
    limit=10,
    with_distance=True
)
for city, distance in cities_with_distances:
    print(f"{city.name}: {distance:.1f}km")

# Get cities by country
cities = db.get_cities_by_country("US")

# Get states/regions by country
states = db.get_states_by_country("US")

# Get database statistics
stats = db.get_statistics()
```

### Distance Calculation

The package uses [geopy](https://geopy.readthedocs.io/) for precise distance calculations using the geodesic formula. Coordinates are passed as tuples of (latitude, longitude).

Example distances:
```python
# Some major city coordinates
new_york = (40.7128, -74.0060)
london = (51.5074, -0.1278)
paris = (48.8566, 2.3522)
tokyo = (35.6762, 139.6503)
seoul = (37.5665, 126.9780)

# Calculate distances
print(f"New York to London: {db.calculate_distance(new_york, london):.1f}km")  # ~5,570km
print(f"Paris to Tokyo: {db.calculate_distance(paris, tokyo):.1f}km")  # ~9,713km
print(f"Tokyo to Seoul: {db.calculate_distance(tokyo, seoul):.1f}km")  # ~1,160km
```

### Database Content

The package includes:
- Countries (250 records)
- Regions (6 records)
- Subregions (22 records)
- States/Regions/Municipalities (5,038 records)
- Cities/Towns/Districts (151,072 records)


---

## Django Integration

AigeoDB provides Django model fields with Select2-powered autocomplete support for cities and countries. The integration is completely self-contained and doesn't require additional packages.

### Setup

Add to INSTALLED_APPS:
```python
INSTALLED_APPS = [
    ...
    'aigeodb.django',  # Our fields and widgets
]
```

Add URLs to your project's urls.py:
```python
from django.urls import path, include

urlpatterns = [
    ...
    path('aigeodb/', include('aigeodb.django.urls')),  # Required for search functionality
]
```

### Using Fields

```python
from django.db import models
from aigeodb.django.fields import CityField, CountryField

class Location(models.Model):
    city = CityField()
    country = CountryField()
    
    # Fields can be optional
    departure_city = CityField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.city.name}, {self.country.name}"
```

### Features

- Built-in Select2 integration with AJAX search
- Automatic dark mode support
- Efficient data loading and caching
- Built-in data validation
- Admin interface integration
- Thread-safe database access

### Admin Integration

The fields work out of the box in Django admin - no additional configuration needed:

```python
from django.contrib import admin

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'country')
    search_fields = ('city', 'country')
```

### Field Options

Both `CityField` and `CountryField` support standard Django model field options:

```python
from django.db import models
from aigeodb.django.fields import CityField, CountryField

class Location(models.Model):
    # Standard field options
    city = CityField(
        null=True,
        blank=True
    )
    
    # Default settings
    country = CountryField()

    def __str__(self):
        return f"{self.city.name}, {self.country.name}"
```

The fields automatically provide:
- Select2 integration with AJAX search
- Minimum 2 characters before search starts
- 300ms search delay for better performance
- Automatic dark mode support
- Built-in data validation

### API Endpoints

The package provides two AJAX endpoints for search functionality:

- `/aigeodb/search-cities/` - Search cities by name
  - Parameters:
    - `term`: Search query string (min 2 characters)
  - Returns: Array of city objects with id, name, and country_name

- `/aigeodb/search-countries/` - Search countries by name
  - Parameters:
    - `term`: Search query string (min 2 characters)
  - Returns: Array of country objects with id, name, and iso2

Example response for cities:
```json
[
    {
        "id": 123,
        "name": "New York",
        "country_name": "United States"
    }
]
```

Example response for countries:
```json
[
    {
        "id": 840,
        "name": "United States",
        "iso2": "US"
    }
]
```

## License

MIT License - see the LICENSE file for details.

## Credits

- Data source: [countries-states-cities-database](https://github.com/dr5hn/countries-states-cities-database)
- Developed by [Unrealos Inc.](https://unrealos.com/)
