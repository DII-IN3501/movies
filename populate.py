from movieApp.models import Pelicula
from movieApp.models import Subtitulo
from movieApp.models import Persona
from movieApp.models import Participacion

peli = Pelicula(titulo="Matrix")

sub1 = Subtitulo(idioma="ES", pelicula=peli)
sub2 = Subtitulo(idioma="EN", pelicula=peli)

keanu = Persona(nombre="Keanu Reeves", nacionalidad="Canadiense")

neo = Participacion(pelicula=peli, persona=keanu, cargo="Actor")

peli.save()
sub1.save()
sub2.save()
keanu.save()
neo.save()
