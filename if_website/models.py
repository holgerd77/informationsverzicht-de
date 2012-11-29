# coding=UTF-8

from django.db import models
from django.forms import ModelForm


class Unterzeichner(models.Model):
    name = models.CharField(max_length=120)
    help_text = "Notwendig zur Freischaltung, wird nicht veröffentlicht."
    email = models.EmailField(max_length=75, unique=True, help_text=help_text)
    wohnort = models.CharField(max_length=120)
    help_text = "Geschätzte bisherige monatliche Ausgaben für Nachrichtenerzeugnisse von Verlagen, "
    help_text += "die das Leistungsschutzrecht unterstützen, " 
    help_text += "nur ganze Zahlen, maximal 120 Euro (zur Vorbeugung von Missbrauch/Ergebnisverzerrung)."
    ausgaben = models.IntegerField(help_text=help_text)
    published = models.BooleanField(default=False)
    activation_hash = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class UnterzeichnerForm(ModelForm):
    class Meta:
        model = Unterzeichner
        fields = ('name', 'email', 'wohnort', 'ausgaben')
