from sklearn.neighbors import BallTree
from numpy import array
from numpy import concatenate
from numpy import nan
from numpy import isnan
from numpy import dot
from numpy.linalg import norm
from numpy import arccos
# from numpy import angle as vector_angle

center_of_the_universe = [component / 2 for component in (10, 10)]


class Brain:

    @staticmethod
    def find_nearest_neigbors() -> None:
        pass

    @staticmethod
    def between(number):
        if number > 1:
            return 1
        elif number < -1:
            return -1
        return number

    @classmethod
    def get_nearest_neighbors(cls, boid_positions: array, visibility_radius: float, flock_angles,
                              boid_number) -> array:
        mirror_images = cls._get_mirror_images(boid_positions)

        ball_tree = BallTree(mirror_images, leaf_size=2)

        distances, boid_indices = ball_tree.query(boid_positions, k=5)

        distances = distances[:, 1:]
        indices = boid_indices[:, 1:]
        indices = indices % boid_number
        # Mask distances that exceed visibility radius
        distances[~(distances < visibility_radius)] = nan
        # Use mask on indicies
        indices = indices * distances / distances
        indices = array([row[~isnan(row)].astype(int) for row in indices], dtype=object)

        mass_center_vector = []
        avg_angle_vector = []
        # wziac kat miedzy boidem a sasiadem
        for boid_index, row in enumerate(indices):
            my_index = boid_indices[boid_index, 0] % boid_number
            my_position = boid_positions[my_index]
            # mass_center = [
            #     arccos(
            #         cls.between(
            #             dot(boid_positions[index], my_position) /
            #             (norm(boid_positions[index]) * norm(my_position)))) for index in row
            # ] if row.size > 0 else 0
            mass_center = [boid_positions[index] for index in row] if row.size > 0 else None
            mass_center = sum(mass_center) / len(mass_center) if mass_center else 0
            mass_center = arccos(
                cls.between(
                    dot(mass_center, my_position) /
                    (norm(mass_center) * norm(my_position)))) if norm(mass_center) else 0

            avg_angle = [flock_angles[index] for index in row]
            avg_angle = sum(avg_angle) / len(avg_angle) if avg_angle else 0

            mass_center_vector.append(mass_center)
            avg_angle_vector.append(avg_angle)

        return array(mass_center_vector), array(avg_angle)

    @staticmethod
    def _get_mirror_images(boid_positions: array) -> array:
        left_image = boid_positions[boid_positions[:, 0] > center_of_the_universe[0]]
        left_image[:, 0] = left_image[:, 0] - 2 * center_of_the_universe[0]

        right_image = boid_positions[boid_positions[:, 0] < center_of_the_universe[0]]
        right_image[:, 0] = right_image[:, 0] + 2 * center_of_the_universe[0]

        top_image = boid_positions[boid_positions[:, 1] < center_of_the_universe[1]]
        top_image[:, 1] = top_image[:, 1] + 2 * center_of_the_universe[1]

        bottom_image = boid_positions[boid_positions[:, 1] > center_of_the_universe[1]]
        bottom_image[:, 1] = bottom_image[:, 1] - 2 * center_of_the_universe[1]

        mirror_images = concatenate((left_image, right_image, top_image, bottom_image))

        return mirror_images
