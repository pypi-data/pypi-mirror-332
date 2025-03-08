"""
Command to set up the environment for an AgentWeave project.
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from agentweave.utils.config import is_agentweave_project, load_project_config

console = Console()


def install_env(
    python_version: str = typer.Option(
        "3.9",
        "--python-version",
        "-p",
        help="Python version to use for the virtual environment",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Force recreation of the virtual environment if it already exists",
    ),
    skip_frontend: bool = typer.Option(
        False,
        "--skip-frontend",
        "-s",
        help="Skip frontend dependencies installation",
    ),
    dev: bool = typer.Option(
        True,
        "--dev/--no-dev",
        help="Install the project as a development package",
    ),
):
    """
    Set up the environment for an AgentWeave project.

    This command creates a virtual environment and installs all required dependencies
    for both the backend and frontend (if present). It also installs the project as a
    development package to ensure imports work correctly.

    Examples:
        agentweave install_env
        agentweave install_env --python-version 3.10
        agentweave install_env --force
        agentweave install_env --skip-frontend
        agentweave install_env --no-dev
    """
    # Check if we're in an AgentWeave project
    if not is_agentweave_project():
        console.print(
            "[red]Not in an AgentWeave project. Please run this command in the root of an AgentWeave project.[/red]"
        )
        raise typer.Exit(1)

    project_config = load_project_config()
    project_name = project_config.get("name", "AgentWeave project")

    console.print(
        f"\n[bold cyan]Setting up environment for: [/bold cyan][bold white]{project_name}[/bold white]"
    )

    # Get project root directory
    project_dir = Path.cwd()
    venv_dir = project_dir / ".venv"

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}[/bold cyan]"),
        console=console,
    ) as progress:
        # Step 1: Create virtual environment
        task = progress.add_task("Creating virtual environment...", total=None)

        try:
            # Check if virtual environment already exists
            if venv_dir.exists():
                if force:
                    console.print(
                        "[yellow]Removing existing virtual environment...[/yellow]"
                    )
                    shutil.rmtree(venv_dir)
                else:
                    console.print(
                        "[yellow]Virtual environment already exists. Use --force to recreate it.[/yellow]"
                    )
                    progress.update(
                        task, description="Using existing virtual environment"
                    )

            if not venv_dir.exists():
                # Create virtual environment
                progress.update(task, description="Creating virtual environment...")
                try:
                    subprocess.run(
                        [sys.executable, "-m", "venv", str(venv_dir)],
                        check=True,
                        capture_output=True,
                    )
                except subprocess.CalledProcessError as e:
                    console.print(
                        f"[red]Error creating virtual environment: {e.stderr.decode()}[/red]"
                    )
                    raise typer.Exit(1)

                progress.update(
                    task, description="Virtual environment created successfully!"
                )

            # Step 2: Install backend dependencies
            progress.update(task, description="Installing backend dependencies...")

            # Determine the pip executable path based on the operating system
            if sys.platform == "win32":
                pip_path = venv_dir / "Scripts" / "pip"
            else:
                pip_path = venv_dir / "bin" / "pip"

            # Install requirements if requirements.txt exists
            requirements_file = project_dir / "requirements.txt"
            if requirements_file.exists():
                try:
                    subprocess.run(
                        [str(pip_path), "install", "-U", "pip", "setuptools", "wheel"],
                        check=True,
                        capture_output=True,
                    )
                    subprocess.run(
                        [str(pip_path), "install", "-r", str(requirements_file)],
                        check=True,
                        capture_output=True,
                    )
                except subprocess.CalledProcessError as e:
                    console.print(
                        f"[red]Error installing backend dependencies: {e.stderr.decode()}[/red]"
                    )
                    raise typer.Exit(1)

                progress.update(
                    task, description="Backend dependencies installed successfully!"
                )
            else:
                console.print(
                    "[yellow]No requirements.txt found. Skipping backend dependencies installation.[/yellow]"
                )

            # Step 3: Install the project as a development package
            if dev:
                progress.update(
                    task, description="Installing project as a development package..."
                )

                # Create or update setup.py if it doesn't exist
                setup_py_path = project_dir / "setup.py"
                if not setup_py_path.exists():
                    # Get project name for the package name - convert to snake_case
                    package_name = re.sub(r"[^a-zA-Z0-9]", "_", project_name.lower())
                    package_name = re.sub(
                        r"_+", "_", package_name
                    )  # Replace multiple underscores with a single one

                    # Create setup.py content
                    setup_py_content = f"""
from setuptools import setup, find_packages

setup(
    name="{package_name}",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.8",
)
"""
                    with open(setup_py_path, "w") as f:
                        f.write(setup_py_content)

                    console.print("[green]Created setup.py for the project.[/green]")

                # Create __init__.py in relevant directories to make them packages
                for dir_path in ["tools", "agents", "memory", "backend"]:
                    init_path = project_dir / dir_path / "__init__.py"
                    if (project_dir / dir_path).exists() and not init_path.exists():
                        with open(init_path, "w") as f:
                            f.write(f"# Package initialization for {dir_path}\n")

                # Install the project in development mode
                try:
                    subprocess.run(
                        [str(pip_path), "install", "-e", "."],
                        check=True,
                        capture_output=True,
                        cwd=str(project_dir),
                    )
                    progress.update(
                        task, description="Project installed as development package!"
                    )
                except subprocess.CalledProcessError as e:
                    console.print(
                        f"[red]Error installing project package: {e.stderr.decode()}[/red]"
                    )
                    console.print("[yellow]Continuing with setup...[/yellow]")

            # Step 4: Install frontend dependencies (if frontend directory exists and skip_frontend is False)
            frontend_dir = project_dir / "frontend"
            if frontend_dir.exists() and not skip_frontend:
                progress.update(task, description="Installing frontend dependencies...")

                # Check if package.json exists
                package_json = frontend_dir / "package.json"
                if package_json.exists():
                    # Check if npm is installed
                    try:
                        subprocess.run(
                            ["npm", "--version"],
                            check=True,
                            capture_output=True,
                        )
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        console.print(
                            "[yellow]npm not found. Please install Node.js and npm to set up the frontend.[/yellow]"
                        )
                        progress.update(
                            task, description="Skipping frontend setup (npm not found)"
                        )
                    else:
                        # Install frontend dependencies
                        try:
                            subprocess.run(
                                ["npm", "install"],
                                check=True,
                                capture_output=True,
                                cwd=str(frontend_dir),
                            )
                        except subprocess.CalledProcessError as e:
                            console.print(
                                f"[red]Error installing frontend dependencies: {e.stderr.decode()}[/red]"
                            )
                            raise typer.Exit(1)

                        progress.update(
                            task,
                            description="Frontend dependencies installed successfully!",
                        )
                else:
                    console.print(
                        "[yellow]No package.json found in frontend directory. Skipping frontend setup.[/yellow]"
                    )
            elif skip_frontend:
                progress.update(
                    task,
                    description="Skipping frontend setup (--skip-frontend flag used)",
                )

            # Final step: Create a .env.local file if it doesn't exist
            env_local = project_dir / ".env.local"
            if not env_local.exists():
                env_example = project_dir / ".env.example"
                if env_example.exists():
                    shutil.copy(env_example, env_local)
                    console.print("[green]Created .env.local from .env.example[/green]")
                else:
                    # Create a basic .env.local
                    with open(env_local, "w") as f:
                        f.write(
                            """# Local environment variables
OPENAI_API_KEY=

# Vector store settings
VECTOR_STORE_DIR=./vector_store
"""
                        )
                    console.print("[green]Created a basic .env.local file[/green]")

            # Update completion message
            progress.update(
                task, description="Environment setup completed successfully!"
            )

            console.print(
                "\n[bold green]✓ Environment set up successfully![/bold green]"
            )
            console.print("\n[cyan]To activate the virtual environment:[/cyan]")

            if sys.platform == "win32":
                console.print("  .venv\\Scripts\\activate")
            else:
                console.print("  source .venv/bin/activate")

            console.print("\n[cyan]To run the project:[/cyan]")
            console.print("  agentweave run")

        except Exception as e:
            console.print(f"[red]Error setting up environment: {str(e)}[/red]")
            raise typer.Exit(1)


# Export the command as app
app = install_env
