from random import uniform
from random import seed as SEED
from time import time
from numpy import pi
from numpy import stack
from numpy import array
from numpy import sin
from numpy import cos
from numpy.random import rand
from brain import Brain


class Flock():

    def __init__(self,
                 number_of_boids: int = 10,
                 velocity_max: float = 1,
                 left_bound: float = 0,
                 lower_bound: float = 0,
                 distance: float = 10) -> None:

        seed: float = time() + uniform(-1000, 1000)
        SEED(str(seed).encode("utf-8"))

        self.number_of_boids: int = 1 if number_of_boids <= 0 else number_of_boids
        self.velocity: float = velocity_max
        self.left_bound: float = left_bound
        self.lower_bound: float = lower_bound
        self.velocity_max: float = velocity_max
        self.distance: float = distance

        self.positions: array[
            array[float]] = rand(number_of_boids, 2) * (distance - left_bound) + left_bound
        self.angles: array[float] = array([uniform(0, 2 * pi) for _ in range(number_of_boids)])
        self.velocities: array[float] = array([self.velocity for _ in range(number_of_boids)])

    def get_positions_x(self) -> array:
        return self.positions[:, 0]

    def get_positions_y(self) -> array:
        return self.positions[:, 1]

    def get_velocities_x(self) -> array:
        return self.velocities * sin(self.angles)

    def get_velocities_y(self) -> array:
        return self.velocities * cos(self.angles)

    def get_phi_angles(self) -> array:
        return self.angles

    def get_velocity_versors_x(self) -> array:
        return sin(self.angles)

    def get_velocity_versors_y(self) -> array:
        return cos(self.angles)

    def update_flock_state(self, dt: float) -> None:
        # .5, .3 ciekawe rzeczy robia
        visibility_radius = 4
        mass_center_weight = .5
        avg_angle_weight = .03
        mass_center_vector, avg_angle_vector = Brain.get_nearest_neighbors(
            self.positions, visibility_radius, self.angles, self.number_of_boids)
        # wywalic angles
        neighbour_mass = mass_center_weight * (mass_center_vector - self.angles)
        neighbor_angles = avg_angle_weight * (avg_angle_vector - self.angles)
        self.angles = self.angles + array(
            [12 * uniform(-pi / 180, pi / 180)
             for _ in range(len(self.angles))]) + neighbour_mass + neighbor_angles
        self.positions = self.positions + dt * stack(
            (self.get_velocities_x(), self.get_velocities_y()), axis=1)
        self.positions[:, 0] = (self.positions[:, 0] + self.left_bound
                                + self.distance) % (self.left_bound + self.distance)
        self.positions[:, 1] = (self.positions[:, 1] + self.lower_bound
                                + self.distance) % (self.lower_bound + self.distance)
