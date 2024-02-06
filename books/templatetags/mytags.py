from django import template

register = template.Library()

@register.filter
def add_mohammad(text):
    new_text = "mohammad: "+text
    return new_text