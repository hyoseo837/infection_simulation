import cx_Freeze

executables = [cx_Freeze.Executable("finalSimulator.py")]

cx_Freeze.setup(
    name = "Infection_Simulator",
    options = {"build_exe": {"packages":["pygame"], "include_files":["image"]}},
    
    executables = executables

    )