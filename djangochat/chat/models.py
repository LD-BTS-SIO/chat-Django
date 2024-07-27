from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=200)  # Longueur raisonnable pour un nom de salle

class Message(models.Model):
    value = models.TextField()  # Utilisez TextField pour des textes longs
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=255)  # Longueur raisonnable pour un nom d'utilisateur
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Utilisez ForeignKey pour des relations
