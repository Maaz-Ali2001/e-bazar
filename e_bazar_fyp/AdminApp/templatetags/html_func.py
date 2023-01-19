from django import template

register = template.Library()

@register.simple_tag
def status_venid(stat=None,id=None):
    return stat+','+str(id)

@register.simple_tag
def get_id(value):
    for k,v in value.items():
        if k=='_id':
            return v