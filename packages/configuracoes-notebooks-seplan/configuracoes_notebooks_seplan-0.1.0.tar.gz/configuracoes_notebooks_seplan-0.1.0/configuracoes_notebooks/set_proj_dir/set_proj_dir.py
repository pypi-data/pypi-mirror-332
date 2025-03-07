from .find_dir import find_parent_dir_from_curr_dir
from .find_git_proj_dir import find_git_proj_dir
from .set_dir_in_path import set_dir_in_path

def set_proj_root_in_path():

    proj_root = find_git_proj_dir()
    print(f'O diretorio do seu projeto é {proj_root}')
    root_path = find_parent_dir_from_curr_dir(proj_root)
    print(f'Caminho absoluto do diretorio encontrado {root_path}')

    set_dir_in_path(root_path)
    print(f'Caminho no path.')

    