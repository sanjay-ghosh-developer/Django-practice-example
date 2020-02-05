from django import template

register = template.Library()

@register.filter(name='cut')#use of decorator
def cuts(value,arg):
        """
        This cuts out all value of 'arg' from string!
        """
    return value.replace(arg,'')

# register.filter('cut',cuts)#simple use
