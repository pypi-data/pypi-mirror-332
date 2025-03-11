from django.db import models
from django.core.exceptions import ValidationError
from django_select2.forms import ModelSelect2Widget
from ...core.database import DatabaseManager


class CountrySelectWidget(ModelSelect2Widget):
    """Widget for country selection"""
    search_fields = ['name__icontains']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        db = DatabaseManager()
        self.choices = [('', '---------')] + [
            (str(country.id), f"{country.name} ({country.iso2})")
            for country in db.get_all_countries()
        ]


class CountryField(models.CharField):
    """Field for storing country ID from aigeodb"""
    
    description = "Field for storing country ID from aigeodb"
    
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 50  # Country ID max length
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'widget': CountrySelectWidget,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value:
            db = DatabaseManager()
            country = db.get_country_by_id(int(value))
            if not country:
                raise ValidationError(
                    f'Country with ID {value} does not exist'
                ) 