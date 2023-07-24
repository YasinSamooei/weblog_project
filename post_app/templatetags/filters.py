from django import template
# Library instance
register=template.Library()
#--------------------------------

#cutter filter
@register.filter()
def cutter(value,arg):
    return value[:arg]
#--------------------------------