from django.http import HttpResponse
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'informationsverzicht_de.views.home', name='home'),
    # url(r'^informationsverzicht_de/', include('informationsverzicht_de.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'if_website.views.index', name='index'),
    url(r'^mitzeichnen/$', 'if_website.views.mitzeichnen', name='mitzeichnen'),
    url(r'^freischalten/$', 'if_website.views.freischalten', name='freischalten'),
    url(r'^unterzeichner/$', 'if_website.views.unterzeichner', name='unterzeichner'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^robots\.txt$', lambda r: HttpResponse("", mimetype="text/plain")),
    url(r'^(?P<page>[-\w]+)/$', 'if_website.views.static_page', name='static_page'),
)
