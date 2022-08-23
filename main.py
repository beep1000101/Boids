import matplotlib.pyplot as plt

from boids import Flock
from config_parser import ConfigParser
from matplotlib.animation import FuncAnimation


def main():
    modes = ("play", "save")
    mode = modes[1]
    cp = ConfigParser()

    def animate(_: int, flock_object: Flock, quiver_object, dt: float):
        flock_object.update_flock_state(dt)
        ax.cla()
        quiver_object = ax.quiver(flock.get_positions_x(),
                                  flock.get_positions_y(),
                                  flock.get_velocity_versors_x(),
                                  flock.get_velocity_versors_y(),
                                  flock.get_phi_angles(),
                                  pivot=cp.init_pivot())

        plt.xlim(*cp.init_xlim())
        plt.ylim(*cp.init_ylim())
        return quiver_object

    flock = Flock(**cp.init_flock())

    plt.style.use('dark_background')
    fig, ax = plt.subplots(**cp.init_subplot())

    Q = ax.quiver(flock.get_positions_x(),
                  flock.get_positions_y(),
                  flock.get_velocity_versors_x(),
                  flock.get_velocity_versors_y(),
                  flock.get_phi_angles(),
                  pivot=cp.init_pivot())

    animation = FuncAnimation(fig,
                              animate,
                              fargs=(flock, Q, cp.init_animation_fargs()),
                              frames=600,
                              **cp.init_animation_kwargs())
    if mode == "play":
        plt.xlim(*cp.init_xlim())
        plt.ylim(*cp.init_ylim())
        plt.show()
    elif mode == "save":
        animation.save("filmik.gif", fps=60)
    else:
        print("invalid mode has been selected")


if __name__ == "__main__":
    main()
