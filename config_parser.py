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

    def _get_figsize(self) -> tuple:
        return tuple(
            [int(element) for element in self.config["matplotlib_params"]["figsize"].split(",")])

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


class ConfigParser(ConfigParserBaseClass):
    def init_pivot(self) -> str:
        return self._get_quiver_pivot()

    def init_xlim(self) -> tuple:
        return tuple([self._get_xlim_min(), self._get_xlim_max()])

    def init_ylim(self) -> tuple:
        return tuple([self._get_ylim_min(), self._get_ylim_max()])

    def init_flock(self) -> dict:
        return {
            "number_of_boids": self._get_number_of_boids(),
            "boid_velocity_max": self._get_boid_max_velocity()
        }

    def init_figsize(self) -> dict:
        return {"figsize": tuple(self._get_figsize())}

    def init_animation_fargs(self) -> float:
        return self._get_dt()

    def init_animation_kwargs(self) -> dict:
        return {"interval": self._get_interval(), "blit": self._get_blit()}
