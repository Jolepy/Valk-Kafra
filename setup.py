### Criar o Executavel.

from cx_Freeze import setup, Executable
import os

# Adicionando arquivos necessários
files = [
    ('background.gif', 'background.gif'),
    ('background_topdown.gif', 'background_topdown.gif'),
    ('img0.png', 'img0.png'),
    ('img1.png', 'img1.png'),
    ('img2.png', 'img2.png'),
    ('img3.png', 'img3.png'),
    ('Estoque.db', 'Estoque.db')
]

# Caminho para o ícone do executável
icon_path = 'Valk_Kafra.ico'

# Informações do executável
setup(
    name="Valk Kafra",
    version="1.4",
    description="Aplicativo de controle de itens usando SQLITE",
    options={"build_exe": {"include_files": files}},
    executables=[Executable("Valk.Kafra.py", base="Win32GUI", icon=icon_path)]
)
