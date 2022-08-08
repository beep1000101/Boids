import matplotlib.pyplot as plt
import matplotlib.animation as animation

from boids import Flock
from config_parser import ConfigParser


def main():
    cofig_parser = ConfigParser()

    def animate(i, flock_object: Flock, quiver_object, dt):
        flock_object.update_flock_state(dt)
        ax.cla()
        quiver_object = ax.quiver(flock.get_positions_x(),
                                  flock.get_positions_y(),
                                  flock.get_velocity_versors_x(),
                                  flock.get_velocity_versors_y(),
                                  flock.get_phi_angles(),
                                  pivot='mid')

        plt.xlim(*cofig_parser.get_matplotlib_xlim_params())
        plt.ylim(*cofig_parser.get_matplotlib_ylim_params())
        return quiver_object

    flock = Flock(**cofig_parser.get_flock_params())

    fig, ax = plt.subplots(figsize=cofig_parser.get_figsize())

    Q = ax.quiver(flock.get_positions_x(),
                  flock.get_positions_y(),
                  flock.get_velocity_versors_x(),
                  flock.get_velocity_versors_y(),
                  flock.get_phi_angles(),
                  pivot='mid')

    anim = animation.FuncAnimation(fig, animate, fargs=(flock, Q, 0.01), interval=50, blit=False)

    plt.xlim(*cofig_parser.get_matplotlib_xlim_params())
    plt.ylim(*cofig_parser.get_matplotlib_ylim_params())
    plt.show()


if __name__ == "__main__":
    main()
