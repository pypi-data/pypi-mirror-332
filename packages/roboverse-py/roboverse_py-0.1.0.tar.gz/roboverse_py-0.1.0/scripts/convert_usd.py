import argparse
import os
import shutil
from glob import glob

from loguru import logger as log
from omni.isaac.lab.app import AppLauncher
from rich.logging import RichHandler

log.configure(handlers=[{"sink": RichHandler(), "format": "{message}"}])

parser = argparse.ArgumentParser()
parser.add_argument("--headless", default=True)
parser.add_argument("--input_path", default="")
parser.add_argument("--output_path", default="")
parser.add_argument("--ensure_root_rigid_body_api", action="store_true")
parser.add_argument("--remove_all_rigid_body_api", action="store_true")
parser.add_argument("--overwrite", action="store_true")
parser.add_argument("--refresh", action="store_true")
args = parser.parse_args()
app_launcher = AppLauncher(args)
simulation_app = app_launcher.app

from pxr import Usd, UsdPhysics


def copy_usd(usd_path: str, dst_usd_path: str = ""):
    if dst_usd_path == "":
        dst_usd_path = "data_isaaclab/" + usd_path.removeprefix("data/")

    os.makedirs(os.path.dirname(dst_usd_path), exist_ok=True)
    shutil.copy(usd_path, dst_usd_path)
    return dst_usd_path


def is_articulation(usd_path: str):
    joint_count = 0
    stage = Usd.Stage.Open(usd_path)
    for prim in stage.Traverse():
        if prim.IsA(UsdPhysics.Joint):
            joint_count += 1
    return joint_count > 0


def count_rigid_api(stage):
    rigid_api_count = 0
    for prim in stage.Traverse():
        if prim.HasAPI(UsdPhysics.RigidBodyAPI):
            rigid_api_count += 1
    return rigid_api_count


def ensure_single_rigid_api(usd_path):
    stage = Usd.Stage.Open(usd_path)

    # Statics
    rigid_api_count = count_rigid_api(stage)
    log.info(f"Found {rigid_api_count} rigid body APIs in {usd_path}")
    if rigid_api_count == 1 and not args.refresh:
        log.info(f"Skipping {usd_path} because it has exactly 1 rigid body API")
        return

    # Remove all rigid body
    for prim in stage.Traverse():
        if prim.HasAPI(UsdPhysics.RigidBodyAPI):
            prim.RemoveAPI(UsdPhysics.RigidBodyAPI)
        # if prim.HasAPI(UsdPhysics.CollisionAPI):
        #     prim.RemoveAPI(UsdPhysics.CollisionAPI)

    # Apply rigid body API
    defaultPrim = stage.GetDefaultPrim()
    UsdPhysics.RigidBodyAPI.Apply(defaultPrim)

    # Check again
    rigid_api_count = count_rigid_api(stage)
    if rigid_api_count != 1:
        raise RuntimeError(f"Failed to ensure single rigid body API in {usd_path}, got {rigid_api_count}")

    log.info(f"Saved {usd_path}")
    stage.Save()


def ensure_root_rigid_body_api(usd_path):
    stage = Usd.Stage.Open(usd_path)
    defaultPrim = stage.GetDefaultPrim()
    UsdPhysics.RigidBodyAPI.Apply(defaultPrim)


def remove_all_rigid_body_api(usd_path):
    stage = Usd.Stage.Open(usd_path)
    for prim in stage.Traverse():
        if prim.HasAPI(UsdPhysics.RigidBodyAPI):
            prim.RemoveAPI(UsdPhysics.RigidBodyAPI)
    stage.Save()


def do_it(usd_path: str, dst_usd_path: str = ""):
    if dst_usd_path == "":
        dst_usd_path = "data_isaaclab/" + usd_path.removeprefix("data/")

    if os.path.exists(dst_usd_path) and not args.overwrite:
        log.info(f"Skipping {dst_usd_path} because it already exists")
        return

    copy_usd(usd_path, dst_usd_path)
    if is_articulation(dst_usd_path):
        log.info(f"Only copying {usd_path} because it is an articulation")
    else:
        log.info(f"Processing {usd_path}")
        ensure_single_rigid_api(dst_usd_path)

    if args.ensure_root_rigid_body_api:
        log.info(f"Ensuring root rigid body API for {dst_usd_path}")
        ensure_root_rigid_body_api(dst_usd_path)

    if args.remove_all_rigid_body_api:
        log.info(f"Removing all rigid body APIs for {dst_usd_path}")
        remove_all_rigid_body_api(dst_usd_path)


def data2isaaclab():
    ## Rigid body
    usd_dirs = [
        "data/assets/maniskill2/plug_charger",
        "data/assets/rlbench/close_box",
        "data/assets/rlbench/phone_on_base",
        "data/assets/rlbench/basketball_in_hoop",
        "data/assets/rlbench/get_ice_from_fridge",
        "data/assets/rlbench/put_books_on_bookshelf",
        "data/assets/rlbench/put_shoes_in_box",
        "data/assets/rlbench/set_the_table",
        "data/assets/rlbench/place_cups",
        "data/assets/rlbench/put_plate_in_colored_dish_rack",
        "data/assets/rlbench/put_item_in_drawer",
        "data/assets/rlbench/take_item_out_of_drawer",
        "data/assets/rlbench/screw_nail",
        "data/assets/rlbench/stack_chairs",
        "data/assets/rlbench/hockey",
        "data/assets/rlbench/stack_cups",
        "data/assets/rlbench/slide_block_to_target",
        "data/assets/rlbench/open_drawer",
        "data/assets/rlbench/take_shoes_out_of_box",
        "data/assets/rlbench/put_bottle_in_fridge",
    ]
    usd_paths = []
    for usd_dir in usd_dirs:
        usd_paths += glob(f"{usd_dir}/**/*.usd", recursive=True)
    log.info(f"Processing {len(usd_paths)} USD files")
    for usd_path in usd_paths:
        do_it(usd_path)


def single_convert(usd_path, dst_usd_path):
    do_it(usd_path, dst_usd_path)


if __name__ == "__main__":
    single_convert(args.input_path, args.output_path)
