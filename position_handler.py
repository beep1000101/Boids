from boids import Flock
from numpy import array


class PositionHandler:
    def __init__(self, flock_positions_x: array, flock_positions_y: array) -> None:
        self.__flock_positions_x = flock_positions_x
        self.__flock_positions_y = flock_positions_y

    def update_x(self, flock_positions_x: array) -> None:
        self.__flock_positions_x = flock_positions_x

    def update_y(self, flock_positions_y: array) -> None:
        self.__flock_positions_y = flock_positions_y

    def __create_mirror_images(self) -> None:
        # finish algorithm creating mirror images to properly
        # create a neighborhood on torus
        self.__mirror_images_x = None
        self.__mirror_images_y = None

    def get_mirror_images_x(self) -> array:
        return self.__mirror_images_x

    def get_mirror_images_y(self) -> array:
        return self.__mirror_images_y
