import sys
import os
import click
from rich.console import Console
from rich.table import Table
from libscan.scanner import install_dependencies, generate_requirements

console = Console()

@click.command()
@click.argument("script_path", type=click.Path(exists=True))
@click.option("-r", "--requirements", is_flag=True, help="Generate a requirements.txt file.")
@click.option("-h", "--help", is_flag=True, help="Show help message.")
def main(script_path, requirements, help):
    """LibScan: A Python dependency scanner and installer."""
    
    if help:
        console.print("Usage: libscan [script.py] [options]", style="bold green")
        console.print("\nOptions:", style="cyan")
        console.print("  -r, --requirements     Generate requirements.txt file", style="yellow")
        console.print("  -h, --help             Show this message and exit.", style="yellow")
        return

    if requirements:
        generate_requirements(script_path)
        return

    console.print(f"Scanning for dependencies in [bold blue]{script_path}[/bold blue]...", style="bold cyan")
    install_dependencies(script_path)

if __name__ == "__main__":
    main()
