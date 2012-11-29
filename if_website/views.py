# coding=UTF-8
import os
from django.core.mail import send_mail
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from if_website.models import Unterzeichner, UnterzeichnerForm


def index(request):
    anz_personen = Unterzeichner.objects.filter(published=True).count()
    ausgaben_monat = Unterzeichner.objects.filter(published=True).aggregate(Sum('ausgaben'))['ausgaben__sum']
    if ausgaben_monat == None:
        ausgaben_monat = 0
    ausgaben_jahr = 12 * ausgaben_monat
    latest_unterzeichner_list = Unterzeichner.objects.filter(published=True).order_by('-date_added')[0:6]
    
    c = RequestContext(request, {
        'anz_personen': anz_personen,
        'ausgaben_monat': ausgaben_monat,
        'ausgaben_jahr': ausgaben_jahr, 
        'unterzeichner_list': latest_unterzeichner_list,
    })
    return render_to_response("if_website/index.html", c)

def mitzeichnen(request):
    if request.method == 'POST':
        form = UnterzeichnerForm(request.POST)
        if form.is_valid() and form.cleaned_data['ausgaben'] <= 120:
            u = form.save(commit=False) 
            u.activation_hash = os.urandom(16).encode('hex')
            u.save()
            
            subject = "Deine Mitzeichnung auf informationsverzicht.de"
            msg  = "Du hast Dich auf informationsverzicht.de mit Deiner Mitzeichnung" + "\n"
            msg += "gegen ein Leistungsschutzrecht ausgesprochen." + "\n\n"
            msg += "Zum Freischalten Deiner Mitzeichnung klicke auf folgenden Link:" +"\n"
            msg += "http://informationsverzicht.de/freischalten/?activation_hash=" + u.activation_hash + "\n\n"
            
            send_mail(subject, msg, 'info@informationsverzicht.de', [u.email], fail_silently=False)
            
            return render_to_response('if_website/mitgezeichnet.html')
    else:
        form = UnterzeichnerForm()
    
    c = RequestContext(request, {
        'form': form,
    })
    
    return render_to_response("if_website/mitzeichnen.html", c)

def freischalten(request):
    
    name = ''
    
    if 'activation_hash' in request.GET:
        unterzeichner = Unterzeichner.objects.filter(activation_hash=request.GET['activation_hash'])
        if len(unterzeichner) == 1:
            u = unterzeichner[0]
            u.published = True
            u.save()
            name = u.name
    c = RequestContext(request, {
        'name': name,
    })
    return render_to_response("if_website/freischalten.html", c)
    

def unterzeichner(request):
    unterzeichner_list = Unterzeichner.objects.filter(published=True).order_by('-date_added')
    c = RequestContext(request, {
        'unterzeichner_list': unterzeichner_list,
    })
    return render_to_response("if_website/unterzeichner.html", c)


def static_page(request, page):
    return render_to_response('if_website/' + page + '.html')