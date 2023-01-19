from django import template
register = template.Library()
#https://stackoverflow.com/questions/4651172/reference-list-item-by-index-within-django-template
@register.filter
def index(indexable, i):
    return indexable[i]
