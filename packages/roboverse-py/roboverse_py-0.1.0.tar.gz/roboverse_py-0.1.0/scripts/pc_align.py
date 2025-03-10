from __future__ import annotations

import numpy as np
import open3d as o3d
from scipy.spatial.transform import Rotation as R


def align_objects(
    obj_path_A: str, obj_path_B: str, num_points: int = 10000, max_dist: float = 0.02
) -> tuple[np.ndarray, float]:
    """
    Align two 3D objects and return the quaternion rotation and alignment confidence.

    Args:
        obj_path_A (str): Path to the first OBJ file (target object)
        obj_path_B (str): Path to the second OBJ file (object to be aligned)
        num_points (int, optional): Number of points to sample from each mesh. Defaults to 10000.
        max_dist (float, optional): Maximum correspondence distance for ICP. Defaults to 0.02.

    Returns:
        tuple[np.ndarray, float]:
            - Quaternion rotation [x, y, z, w] to align object B to object A
            - Confidence score (0-1) where 1 indicates perfect alignment
    """
    # Load OBJ files as meshes
    mesh_A = o3d.io.read_triangle_mesh(obj_path_A)
    mesh_B = o3d.io.read_triangle_mesh(obj_path_B)

    # Convert meshes to point clouds by sampling points on the surface
    pcd_A = mesh_A.sample_points_uniformly(number_of_points=num_points)
    pcd_B = mesh_B.sample_points_uniformly(number_of_points=num_points)

    # Initial alignment using identity matrix
    trans_init = np.eye(4)

    # Perform point-to-point registration
    registration_result = o3d.pipelines.registration.registration_icp(
        pcd_A,
        pcd_B,
        max_correspondence_distance=max_dist,
        estimation_method=o3d.pipelines.registration.TransformationEstimationPointToPoint(),
        init=trans_init,
    )

    # Extract the rotation matrix and make a writeable copy
    rotation_matrix = registration_result.transformation[:3, :3].copy()

    # Convert rotation matrix to quaternion
    quaternion = R.from_matrix(rotation_matrix).as_quat()

    # Calculate confidence score based on fitness and RMSE
    # fitness: higher is better (1 = perfect), RMSE: lower is better (0 = perfect)
    confidence = registration_result.fitness * (1 - min(registration_result.inlier_rmse, max_dist) / max_dist)

    return quaternion, confidence


if __name__ == "__main__":
    # Example usage
    obj_A = "/Users/charliecheng/Documents/research/roboverse_repo/RoboVerse/salad_dressing/meshes/salad_dressing.obj"
    obj_B = "/Users/charliecheng/Documents/research/roboverse_repo/mjcf2urdf/LIBERO-master/libero/libero/assets/stable_hope_objects/salad_dressing/textured.obj"

    quat, conf = align_objects(obj_A, obj_B)
    print("Quaternion (x, y, z, w):")
    print(quat)
    print("\nAlignment confidence (0-1):")
    print(conf)
