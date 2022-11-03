from random import uniform
from random import seed as SEED
from time import time
from numpy import pi
from numpy import stack
from numpy import array
from numpy import sin
from numpy import cos


class Flock():

    def __init__(self,
                 number_of_boids: int = 10,
                 velocity_max: float = 1,
                 left_bound: float = 0,
                 lower_bound: float = 0,
                 distance: float = 10) -> None:

        number_of_boids: int = 1 if number_of_boids <= 0 else number_of_boids
        seed: float = time() + uniform(-1000, 1000)
        SEED(str(seed).encode("utf-8"))

        self.velocity: float = velocity_max
        self.left_bound: float = left_bound
        self.lower_bound: float = lower_bound
        self.velocity_max: float = velocity_max
        self.distance: float = distance

        self.positions: array[array[float]] = array([
            array([
                uniform(left_bound, left_bound + distance),
                uniform(lower_bound, lower_bound + distance)
            ]) for _ in range(number_of_boids)
        ])
        self.angles = array([uniform(0, 2 * pi) for _ in range(number_of_boids)])
        self.velocities = array([self.velocity for _ in range(number_of_boids)])

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
        self.angles = self.angles + array(
            [12 * uniform(-pi / 180, pi / 180) for _ in range(len(self.angles))])
        self.positions = self.positions + dt * stack(
            (self.get_velocities_x(), self.get_velocities_y()), axis=1)
        self.positions[:, 0] = (self.positions[:, 0] + self.left_bound
                                + self.distance) % (self.left_bound + self.distance)
        self.positions[:, 1] = (self.positions[:, 1] + self.lower_bound
                                + self.distance) % (self.lower_bound + self.distance)
