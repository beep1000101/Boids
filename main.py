import matplotlib.pyplot as plt
import matplotlib.animation as animation

from boids import Flock


def main():
    def animate(i, flock_object: Flock, quiver_object, dt):
        flock_object.update_flock_state(dt)
        ax.cla()
        quiver_object = ax.quiver(flock.get_positions_x(),
                                  flock.get_positions_y(),
                                  flock.get_velocity_versors_x(),
                                  flock.get_velocity_versors_y(),
                                  flock.get_phi_angles(),
                                  pivot='mid')
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        return quiver_object

    flock = Flock(500, 15)

    fig, ax = plt.subplots(figsize=(12, 7))

    Q = ax.quiver(flock.get_positions_x(),
                  flock.get_positions_y(),
                  flock.get_velocity_versors_x(),
                  flock.get_velocity_versors_y(),
                  flock.get_phi_angles(),
                  pivot='mid')

    anim = animation.FuncAnimation(fig, animate, fargs=(flock, Q, 0.01), interval=50, blit=False)

    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.show()


if __name__ == "__main__":
    main()
