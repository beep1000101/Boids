from boids import Flock
from numpy import array
from config_parser import ConfigParser


class PositionHandler:
    def __init__(self, flock_positions_x: array, flock_positions_y: array) -> None:
        self._flock_positions_x = flock_positions_x
        self._flock_positions_y = flock_positions_y
        self._universe_size = ConfigParser().get_figsize()

    def _get_center_of_the_universe_vector(self) -> tuple:
        return tuple([component / 2 for component in self.__universe_size])

    def _create_mirror_images(self) -> None:
        # finish algorithm creating mirror images to properly
        # create a neighborhood on torus
        self._mirror_images_x = None
        self._mirror_images_y = None

    def update_positions(self, flock_positions_x: array, flock_positions_y: array) -> None:
        self._flock_positions_x = flock_positions_x
        self._flock_positions_y = flock_positions_y

    def get_mirror_images_x(self) -> array:
        return self.__mirror_images_x

    def get_mirror_images_y(self) -> array:
        return self.__mirror_images_y
