import random
import re
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def repeat(value, times=2):
    return value * times

@register.filter
def clean(value):
    cusses = ['stupid', 'stinky', 'darn', 'shucks', 'crud', 'dirt']
    for cuss in cusses:
        cuss_re = re.compile(re.escape(cuss), re.IGNORECASE)
        chars = ''.join([random.choice('!@#$%^&*') for letter in cuss])
        value = cuss_re.sub(chars, value)
    return value