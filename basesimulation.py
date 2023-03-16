import numpy as np

from particle import Particle
from particle_species import ParticleSpecies


class BaseSimulation:
    """
    A base simulation written as an exercise in concert with my PhD qualifying exam
    Extend for MD (brownian dynamics) and MC simulations
    """
    def __init__(self, temperature, maxSteps, **kwargs):
        """
        :keyword interactions a list of Interaction objects
        """
        self._particles = []
        self._particle_species = []
        self._temperature = temperature
        self._max_steps = maxSteps
        self._interactions = [] if 'interactions' not in kwargs else kwargs['interactions']

    def export(self, topfile="init.top", trajfile="trajectory.dat", particles_file=None, patches_file=None):
        """
        Exports simulation to a format which is readable by oxview
        :param topfile: a topology file (lists particle types)
        :param trajfile: a file which lists the positions and rotations of particles over time
        :param particles_file: TODO
        :param patches_file: TODO
        """
        pass

    def init_particle_types(self, particle_type_files):
        """
        :param particle_type_files: TODO
        """
        pass

    def confgen(self, **kwargs):
        """
        TODO
        :param kwargs:
        :return:
        """
        pass

    def init_particle_positions(self, topfile, conffile, particle_type_files):
        """

        :param topfile: a file listing the particle types (oxdna format)
        :param conffile: a file listing the particle positions and rotations (oxdna format)
        """

        self.init_particle_types(particle_type_files)

        with open(topfile, 'r') as f:
            # first line contains data we have already read from particle_type_files so skip
            f.readline()
            # space-seperated list of the species of each particle, length = num particles
            particle_instance_types = f.readline().split(" ")
            self._particles = [None for _ in particle_instance_types]  # construct list of particles

        with open(conffile, 'r') as f:
            f.readline()  # skip first line (time, always zero for initial configuration)
            w, d, h = f.readline().split(" ")  # depth, width, height of simulation bounding box
            a, b, c = f.readline().split(" ")  # I have no idea what is on line 3 TODO !!!
            nextline = f.readline()
            particle_idx = 0
            while nextline:
                # the remainder of the oxDNA format conf file is taken up by sets of vectors
                # each line is the data for a particle and is composed of 5 vectors
                # values are deliniated with spaces, vectors are not deliniated
                # first 3 values are position x, y, z
                # next 3 are base vector a1 x, y, z
                # next 3 are base normal vector a3 x, y, z
                # final six are velocity vectors, which are zero at initialization (we can ignore)
                x, y, z, v1x, v1y, v1z, nx, ny, nz = nextline.split(" ")[:9]


                particle_type_idx = particle_instance_types[particle_idx]

                # construct a particle
                self._particles[particle_idx] = Particle(
                    particle_idx,
                    particle_instance_types[particle_idx],
                    np.array((x, y, z)),
                    a1=np.array((v1x, v1y, v1z)),
                    a3=np.array((nx, ny, nz))
                )

                # increment
                nextline = f.readline()
                particle_idx += 1

    def particle_positions_to_matrix(self):
        """
        :return: a matrix of particle position vectors
        """
        return np.array([particle.get_position() for particle in self._particles])

    def step(self):
        """
        executes a step of the simulation
        This method should be extended by child classes
        """
        pass

    def run_simulation(self):
        """

        :return:
        """

    def print_stuff(self):
        """
        TODO: rename function!!!
        prints some information about the simulation
        """