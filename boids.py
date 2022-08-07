import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# from IPython.display import HTML
from matplotlib import rc
from random import uniform
from random import seed as SEED
from time import time


# BOID CLASS, BIRD OF PREY MAY INHERIT FROM IT, I DONT KNOW YET
class Boid:
    def __init__(self,
                 velocity_max: float = 1,
                 left_bound: float = 0,
                 lower_bound: float = 0,
                 distance: float = 10) -> None:
        seed: int = time() + uniform(-1000, 1000)
        SEED(str(seed).encode("utf-8"))
        self.phi_angle: float = uniform(0, 2 * np.pi)
        self.velocity: float = velocity_max
        self.left_bound: float = left_bound
        self.lower_bound: float = lower_bound
        self.velocity_max: float = velocity_max
        self.distance: float = distance
        self.position: np.array = np.array(
            [uniform(left_bound, left_bound + distance),
             uniform(lower_bound, lower_bound + distance)])

    def get_position(self) -> float:
        return self.position

    def get_position_x(self) -> float:
        return self.position[0]

    def get_position_y(self) -> float:
        return self.position[1]

    def get_velocity(self) -> float:
        return self.velocity

    def get_velocity_x(self) -> float:
        return self.velocity * np.cos(self.phi_angle)

    def get_velocity_y(self) -> float:
        return self.velocity * np.sin(self.phi_angle)

    def get_velocity_versor_x(self) -> float:
        return np.cos(self.phi_angle)

    def get_velocity_versor_y(self) -> float:
        return np.sin(self.phi_angle)

    def get_phi(self) -> float:
        return self.phi_angle

    def update_boid_state(self, dt) -> None:
        self.phi_angle += 12 * uniform(-np.pi / 180, np.pi / 180)
        # self.velocity += (1/5)*uniform(-self.velocity_max, self.velocity_max)
        self.position += dt * np.array([self.get_velocity_x(), self.get_velocity_y()])
        self.position[0] = (self.position[0] + self.left_bound + self.distance) % (self.left_bound + self.distance)
        self.position[1] = (self.position[1] + self.lower_bound + self.distance) % (self.lower_bound + self.distance)


class Flock(Boid):
    def __init__(self, number_of_boids: int = 10, velocity_max: float = 1) -> None:
        number_of_boids: int = 1 if number_of_boids <= 0 else number_of_boids
        self._flock_array: np.array = np.array([Boid(velocity_max=velocity_max) for _ in range(number_of_boids)])

    def get_positions_x(self) -> np.array:
        return np.array([boid.get_position_x() for boid in self._flock_array])

    def get_positions_y(self) -> np.array:
        return np.array([boid.get_position_y() for boid in self._flock_array])

    def get_velocities_x(self) -> np.array:
        return np.array([boid.get_velocity_x() for boid in self._flock_array])

    def get_velocities_y(self) -> np.array:
        return np.array([boid.get_velocity_y() for boid in self._flock_array])

    def get_velocity_versors_x(self) -> np.array:
        return np.array([boid.get_velocity_versor_x() for boid in self._flock_array])

    def get_velocity_versors_y(self) -> np.array:
        return np.array([boid.get_velocity_versor_y() for boid in self._flock_array])

    def get_phi_angles(self) -> np.array:
        return np.array([boid.get_phi() for boid in self._flock_array])

    def update_flock_state(self, dt) -> None:
        for boid in self._flock_array:
            boid.update_boid_state(dt)