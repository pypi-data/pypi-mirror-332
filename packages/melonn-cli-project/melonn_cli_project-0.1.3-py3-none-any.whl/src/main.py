import os
import subprocess
import shutil
import typer

app = typer.Typer(help="CLI para la creación y eliminación de proyectos.")

def check_aws_cdk():
    """Verifica si AWS CDK está instalado."""
    try:
        result = subprocess.run("cdk --version", capture_output=True, text=True, shell=True, check=True)
        typer.echo(f"✅ AWS CDK encontrado: {result.stdout.strip()}")
    except subprocess.CalledProcessError:
        typer.echo("⚠️ Error al ejecutar CDK.")
        raise typer.Exit(code=1)
    except FileNotFoundError:
        typer.echo("❌ AWS CDK no está instalado. Instálalo con: npm install -g aws-cdk")
        raise typer.Exit(code=1)

def initialize_cdk_project(iac_folder):
    """Inicializa un proyecto AWS CDK en la carpeta 'iac'."""
    typer.echo(f"🚀 Inicializando AWS CDK en {iac_folder}...")
    try:
        subprocess.run("cmd /c cdk init app --language=typescript", cwd=iac_folder, shell=True, check=True)
        typer.echo("✅ AWS CDK inicializado correctamente en la carpeta 'iac'.")
    except subprocess.CalledProcessError:
        typer.echo("❌ Error al inicializar AWS CDK.")
        raise typer.Exit(code=1)

@app.command("create-project")
def create_project(name: str = typer.Argument(..., help="Nombre del proyecto")):
    """Crea la estructura base del proyecto dentro de 'projects'."""
    typer.echo(f"🚀 Creando el proyecto {name} dentro de 'projects'...")
    check_aws_cdk()

    # Crear carpeta projects si no existe
    projects_folder = os.path.join(os.getcwd(), "projects")
    os.makedirs(projects_folder, exist_ok=True)

    # Crear la carpeta del proyecto dentro de projects
    project_folder = os.path.join(projects_folder, name)
    os.makedirs(project_folder, exist_ok=True)
    
    # Crear subcarpetas
    deployment_scripts_folder = os.path.join(project_folder, "deployment-scripts")
    iac_folder = os.path.join(project_folder, "iac")
    python_folder = os.path.join(project_folder, "python")
    internal_services_folder = os.path.join(python_folder, "internal-services")

    os.makedirs(deployment_scripts_folder, exist_ok=True)
    os.makedirs(iac_folder, exist_ok=True)
    os.makedirs(python_folder, exist_ok=True)
    os.makedirs(internal_services_folder, exist_ok=True)
   
    typer.echo(f"✅ Carpeta creada: {project_folder}")
    typer.echo("📁 Subcarpetas creadas dentro del proyecto:")
    typer.echo("   - deployment-scripts")
    typer.echo("   - iac")
    typer.echo("   - python/internal-services")
    
    # Crear archivos en deployment-scripts
    scripts = {
        "build.sh": "#!/bin/bash\n# Script for the construction phase",
        "install.sh": "#!/bin/bash\n# Script for installing dependencies",
        "post_build.sh": "#!/bin/bash\n# Script for post-construction phase",
        "pre_build.sh": "#!/bin/bash\n# Script for the pre-construction phase"
    }
    for script_name, script_content in scripts.items():
        script_path = os.path.join(deployment_scripts_folder, script_name)
        with open(script_path, "w") as script_file:
            script_file.write(script_content + "\n")
        os.chmod(script_path, 0o755)
        typer.echo(f"✅ Archivo creado: deployment-scripts/{script_name}")
    
    # Inicializar AWS CDK en 'iac'
    initialize_cdk_project(iac_folder)
    
    # Crear estructura dentro de 'python'
    vscode_folder = os.path.join(python_folder, ".vscode")
    os.makedirs(vscode_folder, exist_ok=True)
    
    vscode_files = {
        "launch.json": "{}",
        "settings.json": """{
  "python.languageServer": "Pylance",
  // Ruff config.
  "[python]": {
    "editor.detectIndentation": false,
    "editor.insertSpaces": true,
    "editor.tabSize": 4,
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports": "explicit"
    },
    "editor.formatOnSave": true
  },
  "notebook.formatOnSave.enabled": true,
  "notebook.codeActionsOnSave": {
    "notebook.source.fixAll": "explicit",
    "notebook.source.organizeImports": "explicit"
  },
  "ruff.importStrategy": "fromEnvironment",
  // MyPy config.
  "mypy-type-checker.args": [
    "--config-file=pyproject.toml"
  ],
  "mypy-type-checker.importStrategy": "fromEnvironment",
  // autoDocstring config.
  "autoDocstring.docstringFormat": "numpy",
  "autoDocstring.includeName": true,
  "autoDocstring.startOnNewLine": false,
  "autoDocstring.generateDocstringOnEnter": true,
  // Files config.
  "files.trimTrailingWhitespace": true,
  "files.trimFinalNewlines": true,
  // Editor config.
  "editor.renderWhitespace": "boundary",
  "editor.formatOnSave": true,
  "pythonIndent.trimLinesWithOnlyWhitespace": true
}"""
    }
    for file_name, content in vscode_files.items():
        with open(os.path.join(vscode_folder, file_name), "w") as f:
            f.write(content)
        typer.echo(f"✅ Archivo creado: .vscode/{file_name}")

    # Crear archivos adicionales en 'python'
    additional_files = {
        ".env.example": """\
DATABASE_URL_READER=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_PORT=

DATABASE_RS_URL_READER=
DATABASE_RS_USER=
DATABASE_RS_PASSWORD=
DATABASE_RS_PORT=
DATABASE_RS_NAME=

DS_CORE_BUCKET_NAME=

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_SESSION_TOKEN=
""",
        "pyproject.toml": """\
[tool.mypy]
python_version = "3.12"
ignore_missing_imports = true
follow_imports = "silent"
no_implicit_optional = true
strict_optional = true
warn_unused_configs = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
warn_return_any = false
check_untyped_defs = true
disallow_untyped_calls = false
disallow_untyped_defs = true
disallow_incomplete_defs = true
disallow_untyped_decorators = false
disallow_subclassing_any = true
disallow_any_unimported = false
disallow_any_expr = false
disallow_any_decorated = false
disallow_any_explicit = false
disallow_any_generics = false
allow_untyped_globals = true
allow_redefinition = false
local_partial_types = false
implicit_reexport = true
strict_equality = true
show_error_context = false
show_column_numbers = false
show_error_codes = true

[tool.ruff]
target-version = "py312"
line-length = 80
extend-include = ["*.ipynb"]
extend-exclude = ["tests", "test"]
[tool.ruff.lint]
select = ["F", "E", "D"]
extend-select = ["W", "N", "UP", "B", "A", "C4", "PT", "SIM", "PD", "PLE", "RUF"]
ignore = ["SIM300"]
fixable = ["F", "I", "E", "W", "UP", "B", "A", "C4"]
unfixable = []
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"
[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
[tool.ruff.lint.isort]
no-sections = false
force-single-line = true
force-sort-within-sections = false
lines-after-imports = 2
section-order = [
  "future",
  "standard-library",
  "third-party",
  "first-party",
  "local-folder"
]
default-section = "first-party"
known-third-party = [
    "numpy",
    "pandas",
    "keras",
    "tensorflow",
    "sklearn",
    "matplotlib",
    "scipy",
    "h5py",
    "seaborn",
    "numba",
    "gym",
    "PyQt6",
    "PyQt5",
    "pyqtgraph",
    "torch",
    "tqdm"
]
[tool.ruff.lint.mccabe]
max-complexity = 10
[tool.ruff.lint.pycodestyle]
ignore-overlong-task-comments = true
[tool.ruff.lint.pydocstyle]
convention = "numpy"
[tool.ruff.lint.flake8-annotations]
allow-star-arg-any = false
ignore-fully-untyped = false
""",
        "requirements.txt": """\
git+https://github.com/we-are-melonn/lib-python-aws-utils.git@e82ce8716b324187407f4484f7c61d603a9730b8
git+https://github.com/we-are-melonn/lib-python-redshift-connector.git@e1af265513a1df6a72f8079f055251fdeacb866b
git+https://github.com/we-are-melonn/lib-python-custom-errors.git@f02877062b83a5a93ce3d88512fd3beb4d7597e6
git+https://github.com/we-are-melonn/lib-python-slack-notifier.git@fb47159d82d3b998be89a0f4890a2f0f999b61db

python-dotenv==1.0.1
boto3==1.36.24

# Linting/Tooling
mypy==1.15.0
ruff==0.9.6
cfn-lint==1.25.1
"""
    }

    for file_name, content in additional_files.items():
        file_path = os.path.join(python_folder, file_name)
        with open(file_path, "w") as f:
            f.write(content)
        typer.echo(f"✅ Archivo creado: python/{file_name}")

    # Preguntar si se desea crear un microservicio dentro de internal-services
    if typer.confirm("📌 ¿Deseas crear un microservicio dentro de 'internal-services'?"):
        microservice_name = typer.prompt("🔹 Ingresa el nombre del microservicio")
        create_microservice(microservice_name, name)

        # Generar archivo launch.json con el nombre del microservicio
        launch_json_content = f"""{{
    "version": "0.2.0",
    "configurations": [
        {{
            "name": "{microservice_name}",
            "type": "debugpy",
            "request": "launch",
            "args": [
                "{microservice_name}"
            ],
            "program": "${{workspaceFolder}}/internal-services/{microservice_name}/src/handler.py",
            "stopOnEntry": true,
            "justMyCode": false
        }},
        {{
            "name": "Python: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${{file}}",
            "console": "integratedTerminal",
            "justMyCode": true
        }}
    ]
}}"""

        with open(os.path.join(vscode_folder, "launch.json"), "w") as f:
            f.write(launch_json_content)

        typer.echo(f"✅ Archivo creado: .vscode/launch.json con el nombre del microservicio '{microservice_name}'")

    typer.echo("🎉 Proyecto creado exitosamente con toda la estructura solicitada!")

@app.command("create-microservice")
def create_microservice(
    name: str = typer.Argument(..., help="Nombre del microservicio"),
    project: str = typer.Argument(..., help="Nombre del proyecto donde se creará el microservicio")
):
    """Crea un microservicio dentro de 'internal-services'."""
    typer.echo(f"🚀 Creando el microservicio '{name}' dentro del proyecto '{project}'...")

    # Verificar si el proyecto existe
    project_folder = os.path.join(os.getcwd(), "projects", project)
    internal_services_folder = os.path.join(project_folder, "python", "internal-services")

    if not os.path.exists(internal_services_folder):
        typer.echo(f"❌ El proyecto '{project}' no tiene la carpeta 'internal-services'. Verifica el nombre o crea el proyecto primero.")
        raise typer.Exit(code=1)

    # Crear microservicio dentro de internal-services
    microservice_folder = os.path.join(internal_services_folder, name)
    os.makedirs(microservice_folder, exist_ok=True)

    typer.echo(f"✅ Carpeta creada: {microservice_folder}")

    # Crear subcarpetas dentro del microservicio
    events_folder = os.path.join(microservice_folder, "events")
    layers_folder = os.path.join(microservice_folder, "layers")
    src_folder = os.path.join(microservice_folder, "src")

    os.makedirs(events_folder, exist_ok=True)
    os.makedirs(layers_folder, exist_ok=True)
    os.makedirs(src_folder, exist_ok=True)

    typer.echo(f"✅ Carpetas creadas dentro del microservicio:")
    typer.echo("   - events")
    typer.echo("   - layers")
    typer.echo("   - src")

    # Crear subcarpetas dentro de 'src'
    service_folder = os.path.join(src_folder, "service")
    os.makedirs(service_folder, exist_ok=True)
    
    typer.echo(f"✅ Carpeta creada dentro de 'src': service")

    # Preguntar si se desea crear la carpeta 'database'
    if typer.confirm("📌 ¿Deseas crear la carpeta 'database' dentro del microservicio?"):
        database_folder = os.path.join(src_folder, "database")
        os.makedirs(database_folder, exist_ok=True)
        typer.echo("✅ Carpeta creada dentro de 'src': database")

        # Crear archivos en 'database'
        with open(os.path.join(database_folder, "__init__.py"), "w") as f:
            f.write('"""Database module."""\n')
            typer.echo("✅ Archivo creado: src/database/__init__.py")

    # Crear archivo handler.py en 'src'
    handler_file = os.path.join(src_folder, "handler.py")
    with open(handler_file, "w") as f:
        f.write("""\"\"\"Module lambda handler.\"\"\"

import os
import json
import sys
from pathlib import Path

def run(event, stage):
    print(f"Processing event in {stage} environment:")
    print(json.dumps(event, indent=2))

if __name__ == "__main__":
    event_file_path = os.path.join(
        os.path.dirname(__file__), f"../../events/{sys.argv[1]}.json"
    )

    with Path(event_file_path).open(encoding="utf-8") as file:
        event_data = json.load(file)

    run(event_data, "dev")
""")
        typer.echo("✅ Archivo creado: src/handler.py con contenido correctamente indentado")




    # Crear archivo en 'events'
    with open(os.path.join(events_folder, f"{name}.json"), "w") as f:
        f.write("{}")
        typer.echo(f"✅ Archivo creado: events/{name}.json")

    # Crear archivo en 'layers'
    with open(os.path.join(layers_folder, "requirements.txt"), "w") as f:
        f.write("# Dependencies for layers\n")
        typer.echo("✅ Archivo creado: layers/requirements.txt")

    # Crear archivos en 'service'
    with open(os.path.join(service_folder, "__init__.py"), "w") as f:
        f.write('"""Module service."""\n')
        typer.echo("✅ Archivo creado: src/service/__init__.py")

    with open(os.path.join(service_folder, "main.py"), "w") as f:
        f.write('"""Module service main."""\n')
        typer.echo("✅ Archivo creado: src/service/main.py")

    typer.echo(f"✅ Microservicio '{name}' creado en '{microservice_folder}' con toda la estructura solicitada.")

@app.command("delete-project")
def delete_project(name: str = typer.Argument(..., help="Nombre del proyecto a eliminar")):
    """Elimina un proyecto completo dentro de 'projects'."""
    project_folder = os.path.join(os.getcwd(), "projects", name)

    if os.path.exists(project_folder):
        if typer.confirm(f"⚠️ ¿Estás seguro de que deseas eliminar el proyecto '{name}'?"):
            shutil.rmtree(project_folder)
            typer.echo(f"🗑️ Proyecto '{name}' eliminado con éxito.")
    else:
        typer.echo(f"❌ No se encontró el proyecto '{name}'.")

@app.command("delete-microservice")
def delete_microservice(
    name: str = typer.Argument(..., help="Nombre del microservicio a eliminar"),
    project: str = typer.Argument(..., help="Nombre del proyecto donde se encuentra el microservicio")
):
    """Elimina un microservicio dentro de 'internal-services'."""
    typer.echo(f"🚀 Intentando eliminar el microservicio '{name}' del proyecto '{project}'...")

    # Definir rutas
    project_folder = os.path.join(os.getcwd(), "projects", project)
    internal_services_folder = os.path.join(project_folder, "python", "internal-services")
    microservice_folder = os.path.join(internal_services_folder, name)

    if os.path.exists(microservice_folder):
        if typer.confirm(f"⚠️ ¿Estás seguro de que deseas eliminar el microservicio '{name}' en el proyecto '{project}'?"):
            shutil.rmtree(microservice_folder)
            typer.echo(f"🗑️ Microservicio '{name}' eliminado con éxito.")

            # Eliminar archivo de eventos si existe
            event_file = os.path.join(project_folder, "events", f"{name}.json")
            if os.path.exists(event_file):
                os.remove(event_file)
                typer.echo(f"🗑️ Archivo de evento '{name}.json' eliminado.")
        else:
            typer.echo("❌ Cancelando eliminación del microservicio.")
    else:
        typer.echo(f"❌ No se encontró el microservicio '{name}' en el proyecto '{project}'. Verifica el nombre.")


if __name__ == "__main__":
    app()
