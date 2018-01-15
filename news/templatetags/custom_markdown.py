import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()  #need to add for customized filter


@register.filter(is_safe=True)  #register template filter
@stringfilter  #expect strings to be arg
def custom_markdown(value):
    return mark_safe(markdown.markdown(value,
        extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
                                       safe_mode=True,
                                       enable_attributes=False))