from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('MacGyver_Game.py', base=base)
]

setup(name='Mac Gyver',
      version = '0.1',
      description = 'Mac Gyver Game',
      options = dict(build_exe = buildOptions),
      executables = executables)
