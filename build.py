#pip install cx_freeze
import cx_Freeze
executables =[
    cx_Freeze.Executable(script="teste_1.py", icon="space.ico")
]
cx_Freeze.setup(
    name = "Space Marker",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["bgspace.jpeg", "marcacoes.txt", "rocket.png", "spacesound.mp3"]
        }
    }, executables = executables
)

#py geraSetup.py build
#py geraSetup.py bdist_msi