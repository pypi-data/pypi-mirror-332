from django.db import models
from django.core.exceptions import ValidationError
from django_select2.forms import ModelSelect2Widget
from ...core.database import DatabaseManager


class CitySelectWidget(ModelSelect2Widget):
    """Widget for city selection"""
    search_fields = ['name__icontains']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        db = DatabaseManager()
        self.choices = [('', '---------')] + [
            (str(city.id), f"{city.name}, {city.country.name}")
            for city in db.get_all_cities()
        ]


class CityField(models.CharField):
    """Field for storing city ID from aigeodb"""
    
    description = "Field for storing city ID from aigeodb"
    
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 50  # City ID max length
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'widget': CitySelectWidget,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value:
            db = DatabaseManager()
            city = db.get_city_by_id(int(value))
            if not city:
                raise ValidationError(
                    f'City with ID {value} does not exist'
                ) 