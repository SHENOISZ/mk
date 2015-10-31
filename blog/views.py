__author__ = 'marcelo'

from django.http import HttpResponse
from django.shortcuts import RequestContext, loader, render
from formularios.models import form_blog, contador
from Compilator.Compilator import variable
import Compilator.Compilator

def index(request):

    form = form_blog.objects.all()

    if Compilator.Compilator.CHANGE == 0:
        Compilator.Compilator.CHANGE = 1
    elif Compilator.Compilator.CHANGE == 1:
        Compilator.Compilator.CHANGE = 2
    else:
        Compilator.Compilator.CHANGE = 0

    var = variable()
    var.compile('templates/base.html', 'templates/cache/base.min.html', 'none')

    template = loader.get_template('cache/base.min.html')

    context = RequestContext(request, { 'tag': 'Marcelo Rodrigues', 'color': 'color: #ff00ee;', 'form': form, })
    return HttpResponse(template.render(context))

def ajax(request):
    try:
        nome = request.GET.get('nome')
        email = request.GET.get('email')
        comment = request.GET.get('comment')
        publish = request.GET.get('publish')
        publish = str(publish).replace('space', ' ')
        if nome != '' and email != '' and comment != '':
            form_blog.objects.create()
            cont = contador.objects.all()[0]

            form = form_blog.objects.all()[cont.count]
            form.nome = nome
            form.email = email
            form.comment = comment
            form.publish = publish
            form_blog.save(form)

            cont.count += 1
            contador.save(cont)
            reg = 'nome='+ nome+ ';email='+ email+ ';comentario='+ comment+ ';publish='+ publish+ ';'
            print 'ajax'
            return HttpResponse(reg)
        else:
            return HttpResponse('')
    except:
        return HttpResponse('')