import click
from pathlib import Path
from rich.console import Console
from rich.table import Table
from . import core

console = Console()

def printPreview(results: list[tuple[str, str]], dry_run: bool):
    table = Table(show_header=True, header_style="bold")
    table.add_column("Before", style="dim")
    table.add_column("After")
    for old, new in results:
        changed = old != new
        table.add_row(old, f"[green]{new}[/green]" if changed else f"[dim]{new}[/dim]")
    console.print(table)
    if dry_run:
        console.print("[yellow]Dry-run - no files changed. [/yellow]")
    else:
        changed = sum(1 for o, n in results if o != n)
        console.print(f"[green]{changed} File(s) renamed.[/green]")

@click.group()
def main():
    """File Renaming Tool"""
    pass

@main.command()
@click.argument("folder", type=click.Path(exists=True, path_type=Path))
@click.option("--old", required=True, help="Text which should be changed")
@click.option("--new", required=True, help="renaming text")
@click.option("--pattern", default=None, help="only files that match this Regex pattern")
@click.option("--dry-run", is_flag=True, help="only preview, no changes")
def replace(folder, old, new, pattern, dry_run):
    """change text in filename"""
    files = core.getFiles(folder, pattern)
    results = core.renameReplace(files, old, new, dry_run)
    printPreview(results, dry_run)

@main.command()
@click.argument("folder", type=click.Path(exists=True, path_type=Path))
@click.option("--prefix", default="file_", show_default=True, help="prefix before number")
@click.option("--pattern", default=None)
@click.option("--dry-run", is_flag=True)
def number(folder, prefix, pattern, dry_run):
    """enumreate files"""
    files = core.getFiles(folder, pattern)
    results = core.renameNumber(files, prefix, dry_run)
    printPreview(results, dry_run)

@main.command()
@click.argument("folder", type=click.Path(exists=True, path_type=Path))
@click.option("--created", is_flag=True, help="creation date instead of changed date")
@click.option("--dry-run", is_flag=True)
def date(folder, created, pattern, dry_run):
    """add date as prefix"""
    files = core.getFiles(folder, pattern)
    results = core.renameByDate(files, created, dry_run)
    printPreview(results, dry_run)

@main.command()
@click.argument("folder", type=click.Path(exists=True, path_type=Path))
@click.option("--from-ext", required=True, help="old end (e.g. .jpg)")
@click.option("--to-ext", required=True, help="new end (e.g. .png")
@click.option("--dry-run", is_flag=True)
def ext(folder, fromExt, toExt, dry_run):
    """file ending change"""
    files = core.getFiles(folder, None)
    results = core.renameExtension(files, fromExt, toExt, dry_run)
    printPreview(results, dry_run)
