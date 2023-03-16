import numpy as np


class Particle:
    def __init__(self, idx, species, position, a1, a3):
        """
        Constructs a new particle instance from species, rotation, and position
        :param idx: the index of this particle in the simulation
        :param species: the particle's species
        :param position: the particle's starting position
        :param a1: the particle's base vector for the particle's rotation
        :param a3: the base normal vector for the particle's rotation
        """
        self._idx = idx
        self._species = species
        self._position = position
        # rotational stuff
        self._a1 = a1
        self._a3 = a3
        self._a2 = np.cross(a1, a3)

    def rotate(self, rotation):
        pass

    def get_position(self):
        return self._position

    def get_species(self):
        return self._species

    def __iter__(self):
        return InteractionSiteIterator(self)


class InteractionSiteIterator:
    def __init__(self, particle):
        self._parent = particle
        self._idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx > len(self._parent.get_species()):
            raise StopIteration
        else:
            self._idx += 1
            return self._parent.get_species(self._idx)