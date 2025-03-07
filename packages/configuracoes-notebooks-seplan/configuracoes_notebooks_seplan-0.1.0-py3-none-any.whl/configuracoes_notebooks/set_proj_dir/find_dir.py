import os
import sys
from typing import Callable

class FindParentDirFromCurrentDir:

    def __init__(self, max_retries:int=10)->None:

        self.max_retries = max_retries

    def pegar_diretorio_atual(self)->str:

        if '__file__' in globals():
            return os.path.dirname(os.path.abspath(__file__))
        else:
            return os.getcwd()


    def subir_arvore_diretorios(self, diretorio:str, condicao:Callable)->str:

        retries = 0
        while not condicao(diretorio):
            diretorio = os.path.dirname(diretorio)
            retries+=1
            if retries>self.max_retries:
                raise RuntimeError(f'Máximo de tentativas alcançado. Diretorio atual: {diretorio}')
        
        return diretorio
    
    def find_parent_dir(self, parent:str)->str:

        diretorio_atual = self.pegar_diretorio_atual()
        #subir a arvore de diretorios a partir do diretorio atual até que a condição do diretorio
        #ser root seja alcançada

        is_parent = lambda diretorio_atual: os.path.basename(diretorio_atual)==parent

        return self.subir_arvore_diretorios(diretorio_atual, is_parent)
    
    def __call__(self, parent:str)->str:

        return self.find_parent_dir(parent)
    


find_parent_dir_from_curr_dir = FindParentDirFromCurrentDir()