import os
import sys
from typing import Callable


def set_dir_in_path(diretorio:str)->str:

    if not os.path.exists(diretorio):
        raise ValueError(f'Diretorio {diretorio} inexistente.')

    sys.path.append(diretorio)
