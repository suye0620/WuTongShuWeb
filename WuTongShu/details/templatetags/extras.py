from django import template

register = template.Library()

@register.filter(name='mod')
def mod(value, arg):
    return value % arg
@register.filter(name='gv')
def get_value(value, key):
    """
    获取字典中指定键的值
    """
    return value.get(key, '')