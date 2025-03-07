from .find_dir import find_parent_dir_from_curr_dir
from .find_git_proj_dir import find_git_proj_dir
from .set_dir_in_path import set_dir_in_path

def set_proj_root_in_path():

    root = find_git_proj_dir()
    root_path = find_git_proj_dir(root)

    set_dir_in_path(root_path)

    