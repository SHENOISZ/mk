__author__ = 'marcelo'
from django.template.loader_tags import Library
from Compilator.Compilator import variable

register = Library()

var = variable()

@register.simple_tag
def compile(arg):

    path = str(arg)
    extensao = path.split('.')[1]
    novopath = ''

    if extensao == 'less':
        novopath = path.replace('/less', '/cache').replace('.less', '.min.css')

    if extensao == 'js':
        novopath = path.replace('/js', '/cache').replace('.js', '.min.js')

    var.compile(arg, novopath, 'base')

    """
    var.compile('media/less/icons.less', 'media/cache/icons.min.css', 'base')
    var.compile('media/js/base.js', 'media/cache/base.min.js', 'none')

    """
    return novopath
