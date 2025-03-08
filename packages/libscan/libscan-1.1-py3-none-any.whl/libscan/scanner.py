import sys
import os
import subprocess
import ast
import pkg_resources
import click  # Ensure click is imported
from rich.console import Console
from rich.progress import track
from rich.table import Table

console = Console()

def is_builtin_module(module_name):
    """Checks if a module is a built-in Python module."""
    return module_name in sys.builtin_module_names

def get_imports(file_path):
    """Extracts import statements from a Python file."""
    imported_modules = set()

    with open(file_path, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename=file_path)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_modules.add(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imported_modules.add(node.module.split('.')[0])

    return imported_modules

def install_packages(modules):
    """Installs external modules using pip."""
    for module in track(modules, description="[bold magenta]Installing packages...[/bold magenta]"):
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", module], check=True)
            console.print(f"\n✅ [bold green on black]{module}[/bold green on black] installed successfully.\n")
        except subprocess.CalledProcessError:
            console.print(f"⚠️ [bold red]{module} installation failed.[/bold red]")

def find_local_file(module_name, search_paths):
    """Searches for a local Python file corresponding to a module."""
    for path in search_paths:
        module_path = os.path.join(path, f"{module_name}.py")
        if os.path.exists(module_path):
            return module_path
    return None

def get_installed_version(package_name):
    """Returns the installed version of a package, or 'unknown' if not found."""
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        return "unknown"

def process_file(file_path, visited_files, search_paths, external_modules):
    """Processes a Python file, finds dependencies, and detects local imports."""
    if file_path in visited_files:
        return
    visited_files.add(file_path)

    modules = get_imports(file_path)

    # Check if the imported modules are external packages or local Python files
    for module in modules:
        if is_builtin_module(module) or module == 'os':
            continue  # Skip built-in modules like os, sys
        local_file = find_local_file(module, search_paths)
        if local_file:
            process_file(local_file, visited_files, search_paths, external_modules)
        else:
            external_modules.add(module)

def install_dependencies(file_path):
    """Main function to detect and install dependencies."""
    visited_files = set()
    script_dir = os.path.dirname(os.path.abspath(file_path))
    search_paths = [script_dir]
    external_modules = set()

    process_file(file_path, visited_files, search_paths, external_modules)

    # Remove 'os' and other built-in modules explicitly from the external dependencies list
    external_modules = {module for module in external_modules if not is_builtin_module(module)}

    if not external_modules:
        console.print("✅ [bold green]No external dependencies found![/bold green]")
        return

    # Print the title with color
    console.print("\n[bold blue]📦 Dependencies found:[/bold blue]")

    # Create the table for displaying dependencies
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Module", style="bold green")

    for module in external_modules:
        table.add_row(module)
    console.print(table)

    # Using rich console to display a colored message before prompting
    console.print("\n[bold yellow]Do you want to install these packages? (y/n):[/bold yellow]", end=' ')
    
    # Now we prompt the user using click, with the default set to 'y'
    choice = click.prompt("", default="y", type=str).lower()
    
    if choice == 'y':
        install_packages(external_modules)
    else:
        console.print("❌ [bold red]Installation canceled.[/bold red]")
        sys.exit(0)

def generate_requirements(file_path):
    """Generates a `requirements.txt` file with installed versions."""
    visited_files = set()
    script_dir = os.path.dirname(os.path.abspath(file_path))
    search_paths = [script_dir]
    external_modules = set()

    process_file(file_path, visited_files, search_paths, external_modules)

    # Remove 'os' and other built-in modules explicitly from the external dependencies list
    external_modules = {module for module in external_modules if not is_builtin_module(module)}

    if not external_modules:
        console.print("✅ [bold green]No external dependencies found![/bold green]")
        return

    with open("requirements.txt", "w") as f:
        for module in external_modules:
            version = get_installed_version(module)
            if version != "unknown":
                f.write(f"{module}=={version}\n")
            else:
                f.write(f"{module}\n")

    console.print("✅ [bold green]`requirements.txt` file generated successfully![/bold green]")
