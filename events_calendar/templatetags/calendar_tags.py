from django import template

register = template.Library()

@register.filter
def get_list_item(list, index):
    return list[index]