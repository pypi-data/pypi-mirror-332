import subprocess
import os

def find_git_proj_dir():
    try:
        # Obtém o diretório raiz do repositório
        repo_path = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
        # Retorna apenas o nome do último diretório (nome do projeto)
        return os.path.basename(repo_path)
    except subprocess.CalledProcessError:
        raise RuntimeError('Aparentemente não está um projeto git.')