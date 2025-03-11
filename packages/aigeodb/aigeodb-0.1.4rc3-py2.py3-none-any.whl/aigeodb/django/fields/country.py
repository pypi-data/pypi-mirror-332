from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from ...core.database import DatabaseManager
from .widgets import BaseSelectWidget


class CountrySelectWidget(BaseSelectWidget):
    """Widget for country selection with Select2 integration.

    This widget provides:
    - Asynchronous country search
    - Country display with ISO code
    - Automatic value handling
    """

    def __init__(self, attrs=None):
        attrs = attrs or {}
        attrs["class"] = "country-select"
        attrs["data-placeholder"] = "Search for a country..."
        super().__init__(attrs=attrs)
        self._db = DatabaseManager()

    def get_url(self):
        """Get URL for country search endpoint."""
        return reverse("aigeodb:search-countries")

    def get_object_by_id(self, value):
        """Get country object by ID.

        Args:
            value: Country ID (int or str)

        Returns:
            Country object or None if not found
        """
        try:
            value = int(value)
            return self._db.get_country_by_id(value)
        except (TypeError, ValueError):
            return None

    def format_choice(self, country):
        """Format country for display.

        Args:
            country: Country object

        Returns:
            Formatted string: "Country Name (ISO2)"
        """
        return f"{country.name} ({country.iso2})" if country else ""


class CountryField(models.IntegerField):
    """Field for storing country ID from aigeodb"""

    description = "Field for storing country ID from aigeodb"

    def __init__(self, *args, **kwargs):
        self.db = DatabaseManager()
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            "widget": CountrySelectWidget(),
        }
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
                "Invalid value for CountryField. Expected integer or None."
            )

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value:
            country = self.db.get_country_by_id(value)
            if not country:
                raise ValidationError(f"Country with ID {value} does not exist")
