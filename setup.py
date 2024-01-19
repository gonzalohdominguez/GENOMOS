import sys
import os
from cx_Freeze import setup, Executable

files = ['assets', 'genotype_files', 'pys2_msgboxes', 'genotype_db.db']

# Las aplicaciones GUI requieren una base diferente en Windows
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

company_name = 'CENEXA'
product_name = 'GENOMOS'

bdist_msi_options = {
    'upgrade_code': '{66620F3A-DC3A-11E2-B341-002219E9B01E}',
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
    }

exe = Executable(script="app.py", base=base, icon="icono.ico", shortcut_name="GENOMOS", shortcut_dir="DesktopFolder")


setup(
    name = "GENOMOS",
    version = "0.5",
    description = "",
    autor = "Gonzalo Hernán Domínguez",
    icono = "icono.ico", 
    options = {'build_exe': {'include_files': files}, 'bdist_msi': bdist_msi_options}, 
    executables = [exe]
)