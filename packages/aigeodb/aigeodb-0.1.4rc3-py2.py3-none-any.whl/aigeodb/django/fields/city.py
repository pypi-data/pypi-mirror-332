from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from ...core.database import DatabaseManager
from .widgets import BaseSelectWidget


class CitySelectWidget(BaseSelectWidget):
    """Widget for city selection with Select2 integration.

    This widget provides:
    - Asynchronous city search
    - City display with country name
    - Automatic value handling
    """

    def __init__(self, attrs=None):
        attrs = attrs or {}
        attrs["class"] = "city-select"
        attrs["data-placeholder"] = "Search for a city..."
        super().__init__(attrs=attrs)
        self._db = DatabaseManager()

    def get_url(self):
        """Get URL for city search endpoint."""
        return reverse("aigeodb:search-cities")

    def get_object_by_id(self, value):
        """Get city object by ID.

        Args:
            value: City ID (int or str)

        Returns:
            City object or None if not found
        """
        try:
            value = int(value)
            return self._db.get_city_by_id(value)
        except (TypeError, ValueError):
            return None

    def format_choice(self, city):
        """Format city for display.

        Args:
            city: City object

        Returns:
            Formatted string: "City Name, Country Name"
        """
        return f"{city.name}, {city.country.name}" if city else ""


class CityField(models.IntegerField):
    """Field for storing city ID from aigeodb"""

    description = "Field for storing city ID from aigeodb"

    def __init__(self, *args, **kwargs):
        self.db = DatabaseManager()
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {"widget": CitySelectWidget}
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def to_python(self, value):
        """Convert value to integer ID"""
        if value in (None, ""):
            return None
        try:
            return int(value)
        except (TypeError, ValueError):
            raise ValidationError(
                "Invalid value for CityField. Expected integer or None."
            )

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value:
            city = self.db.get_city_by_id(value)
            if not city:
                raise ValidationError(f"City with ID {value} does not exist")
