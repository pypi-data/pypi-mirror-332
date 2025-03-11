from django.conf import settings
from django.forms import widgets
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class BaseSelectWidget(widgets.Select):
    """Base widget for all select fields with Select2 integration.

    This widget provides:
    - Select2 integration with AJAX search
    - Dark mode support
    - Automatic value handling
    - Error handling
    """

    template_name = "django/forms/widgets/select.html"
    option_template_name = "django/forms/widgets/select_option.html"

    def __init__(self, attrs=None, choices=()):
        attrs = attrs or {}
        attrs["class"] = f"admin-autocomplete {attrs.get('class', '')}"
        attrs.update(
            {
                "data-ajax-url": None,
                "data-placeholder": "Search...",
                "data-minimum-input-length": "2",
                "data-theme": "admin",
            }
        )
        super().__init__(attrs=attrs, choices=choices)

    def get_context(self, name, value, attrs):
        """Get context for rendering the widget."""
        context = super().get_context(name, value, attrs)

        # Set AJAX URL
        context["widget"]["attrs"]["data-ajax-url"] = self.get_url()

        # Add initial value if exists
        if value:
            try:
                obj = self.get_object_by_id(value)
                if obj:
                    context["widget"]["choices"] = [(value, self.format_choice(obj))]
            except Exception as e:
                if settings.DEBUG:
                    print(f"Error getting object: {str(e)}")

        return context

    def render(self, name, value, attrs=None, renderer=None):
        """Custom render method to handle Select2 initialization."""
        output = super().render(name, value, attrs, renderer)

        if value:
            try:
                obj = self.get_object_by_id(value)
                if obj:
                    widget_id = attrs.get("id", f"id_{name}")
                    # Add selected option data
                    data = {"id": value, "text": self.format_choice(obj)}
                    script = (
                        "<script>"
                        "const WIDGET_INITIAL_DATA = window.WIDGET_INITIAL_DATA || {};"
                        f'WIDGET_INITIAL_DATA["{widget_id}"] = {data};'
                        "</script>"
                    )
                    output = format_html(
                        "{}\n" + script, output, id=widget_id, data=mark_safe(f"{data}")
                    )
            except Exception as e:
                if settings.DEBUG:
                    print(f"Error rendering select2: {str(e)}")

        return output

    def get_url(self):
        """Get URL for autocomplete API endpoint."""
        raise NotImplementedError("Subclasses must implement get_url()")

    def get_object_by_id(self, value):
        """Retrieve object by its ID from database."""
        raise NotImplementedError("Subclasses must implement get_object_by_id()")

    def format_choice(self, obj):
        """Format object for display in select widget."""
        raise NotImplementedError("Subclasses must implement format_choice()")
