from django import template

register = template.Library()

@register.filter(name='divide')
def divide(value, arg):
    try:
        return (value % arg) + 1
    except (ValueError, TypeError):
        return value
