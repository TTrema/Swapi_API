from django.db import models


class Planet(models.Model):
    """A planet i.e. Tatooine"""

    name = models.CharField(max_length=100, unique=True)
    rotation_period = models.CharField(max_length=40, blank=True)
    orbital_period = models.CharField(max_length=40, blank=True)
    diameter = models.CharField(max_length=40, blank=True)
    climate = models.CharField(max_length=40, blank=True)
    gravity = models.CharField(max_length=40, blank=True)
    terrain = models.CharField(max_length=40, blank=True)
    surface_water = models.CharField(max_length=40, blank=True)
    population = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name


class People(models.Model):
    """A person i.e. - Luke Skywalker"""

    name = models.CharField(max_length=100, primary_key=True)
    height = models.CharField(max_length=10, blank=True)
    mass = models.CharField(max_length=10, blank=True)
    hair_color = models.CharField(max_length=20, blank=True)
    skin_color = models.CharField(max_length=20, blank=True)
    eye_color = models.CharField(max_length=20, blank=True)
    birth_year = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=40, blank=True)
    homeworld = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


# class Transport(models.Model):

#     name = models.CharField(max_length=40)
#     model = models.CharField(max_length=40)
#     manufacturer = models.CharField(max_length=80)
#     cost_in_credits = models.CharField(max_length=40)
#     length = models.CharField(max_length=40)
#     max_atmosphering_speed = models.CharField(max_length=40)
#     crew = models.CharField(max_length=40)
#     passengers = models.CharField(max_length=40)
#     cargo_capacity = models.CharField(max_length=40)
#     consumables = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


# class Starship(Transport):
#     """A starship is a transport with a hypderdrive"""

#     hyperdrive_rating = models.CharField(max_length=40)
#     MGLT = models.CharField(max_length=40)
#     starship_class = models.CharField(max_length=40)
#     pilots = models.ManyToManyField(People, related_name="starships", blank=True)


# class Vehicle(Transport):
#     """A vehicle is anything without hyperdrive capability"""

#     vehicle_class = models.CharField(max_length=40)
#     pilots = models.ManyToManyField(People, related_name="vehicles", blank=True)


# class Species(models.Model):
#     "A species is a type of alien or person"

#     name = models.CharField(max_length=40)
#     classification = models.CharField(max_length=40)
#     designation = models.CharField(max_length=40)
#     average_height = models.CharField(max_length=40)
#     skin_colors = models.CharField(max_length=200)
#     hair_colors = models.CharField(max_length=200)
#     eye_colors = models.CharField(max_length=200)
#     average_lifespan = models.CharField(max_length=40)
#     homeworld = models.ForeignKey(Planet, blank=True, null=True, on_delete=models.CASCADE)
#     language = models.CharField(max_length=40)
#     people = models.ManyToManyField(People, related_name="species")

#     def __str__(self):
#         return self.name


# class Film(models.Model):
#     """A film i.e. The Empire Strikes Back (which is also the best film)"""

#     title = models.CharField(max_length=100)
#     episode_id = models.IntegerField()
#     opening_crawl = models.TextField(max_length=1000)
#     director = models.CharField(max_length=100)
#     producer = models.CharField(max_length=100)
#     release_date = models.DateField()
#     characters = models.ManyToManyField(People, related_name="films", blank=True)
#     planets = models.ManyToManyField(Planet, related_name="films", blank=True)
#     starships = models.ManyToManyField(Starship, related_name="films", blank=True)
#     vehicles = models.ManyToManyField(Vehicle, related_name="films", blank=True)
#     species = models.ManyToManyField(Species, related_name="films", blank=True)

#     def __str__(self):
#         return self.title


# class Hero(models.Model):
#     name = models.CharField(max_length=100)
#     homeworld = models.ForeignKey(Planet, related_name="heroes", on_delete=models.CASCADE)
