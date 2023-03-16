import numpy as np


class InteractionSite:
    """
    An interaction site is any point on the particle that can engage in interactions
    Every particle should have at least one interaction site (the hard-sphere shell)
    """
    def __init__(self, identifier, position, maxRadius):
        """
        :param identifier: an integer that will identify this interaction site for interactions
        :param position: a vector for the site's position
        """

        self._id = identifier
        self._position = position
        self._maxRadius = maxRadius


class ParticleSpecies:
    def __init__(self, identifier, interaction_sites):
        """(
        :param interaction_sites: points on the particle that can engage in interactions
        """
        self._id = identifier
        self._interaction_sites = interaction_sites

        # calculate maximum interaction radius
        # the particle will ignore other particles outside this radius
        self._max_interaction_radius = max([intsite.max_radius() for intsite in self])

    def __getitem__(self, i):
        """
        :param i: integer indexer i < len(interaction_sites)
        :return:
        """
        assert -1 < i < len(self)
        return self._interaction_sites[i]

    def num_interaction_sites(self):
        return len(self)

    def __len__(self):
        return len(self.num_interaction_sites())
