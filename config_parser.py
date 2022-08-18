import configparser

from os import path


class ConfigParserBaseClass:
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        _path = path.join(path.realpath(path.dirname(__name__)), "config.ini")
        self.config.read(_path)

    """FLOCK PARAMS"""

    def _get_number_of_boids(self) -> int:
        return int(self.config["flock_params"]["number_of_boids"])

    def _get_boid_max_velocity(self) -> int:
        return int(self.config["flock_params"]["boid_velocity_max"])

    """MATPLOTLIB PARAMS"""

    def _get_xlim_min(self) -> int:
        return int(self.config["matplotlib_params"]["xlim_min"])

    def _get_xlim_max(self) -> int:
        return int(self.config["matplotlib_params"]["xlim_max"])

    def _get_ylim_min(self) -> int:
        return int(self.config["matplotlib_params"]["ylim_min"])

    def _get_ylim_max(self) -> int:
        return int(self.config["matplotlib_params"]["ylim_max"])

    def _get_figsize(self) -> int:
        return int(self.config["matplotlib_params"]["figsize"])

    """QUIVER PARAMS"""

    def _get_quiver_pivot(self) -> str:
        return self.config["quiver_params"]["quiver_pivot"]

    """ANIMATION PARAMS"""

    def _get_dt(self) -> float:
        return float(self.config["animation_params"]["dt"])

    def _get_interval(self) -> int:
        return int(self.config["animation_params"]["interval"])

    def _get_blit(self) -> bool:
        return bool(int(self.config["animation_params"]["blit"]))

    """UNIVERSE SIZE"""

    def _get_left_bound(self) -> int:
        return int(self.config["universe_size"]["left_bound"])

    def _get_lower_bound(self) -> int:
        return int(self.config["universe_size"]["lower_bound"])

    def _get_distance(self) -> int:
        return int(self.config["universe_size"]["distance"])
