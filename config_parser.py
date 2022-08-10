import configparser

from os import path


class ConfigParser:
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        __path = path.join(path.realpath(path.dirname(__name__)), "config.ini")
        self.config.read(__path)

    def get_flock_params(self) -> dict:
        return {key: int(value) for key, value in self.config["flock_params"].items()}

    def get_matplotlib_xlim_params(self) -> tuple:
        return tuple([int(value) for key, value in self.config["matplotlib_params"].items() if key.startswith("xlim")])

    def get_matplotlib_ylim_params(self) -> tuple:
        return tuple([int(value) for key, value in self.config["matplotlib_params"].items() if key.startswith("ylim")])

    def get_figsize(self) -> tuple:
        return tuple(int(value) for value in self.config["matplotlib_params"]["figsize"].split(","))

    def get_quiver_pivot(self) -> str:
        return self.config["quiver_params"]["quiver_pivot"]

    def get_animation_dt(self) -> float:
        return float(self.config["animation_params"]["dt"])

    def get_animation_kwargs(self) -> dict:
        __content = self.config["animation_params"]["kwargs"].split(",")
        return {"interval": int(__content[0]), "blit": bool(int(__content[1]))}
