import numpy as np

from boids import Flock


class PositionHandler:
    def __init__(self, flock_positions_x: np.array, flock_positions_y: np.array) -> None:
        self.__flock_positions_x = flock_positions_x
        self.__flock_positions_y = flock_positions_y

    def update_x(self, flock_positions_x: np.array) -> None:
        self.__flock_positions_x = flock_positions_x

    def update_y(self, flock_positions_y: np.array) -> None:
        self.__flock_positions_y = flock_positions_y

    def __create_mirror_images(self) -> None:
        # finish algorithm creating mirror images to properly
        # create a neighborhood on torus
        self.__mirror_images_x = None
        self.__mirror_images_y = None

    def get_mirror_images_x(self) -> np.array:
        return self.__mirror_images_x

    def get_mirror_images_y(self) -> np.array:
        return self.__mirror_images_y
