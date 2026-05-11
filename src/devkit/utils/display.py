from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def make_table(title: str, border_style: str = 'green') -> Table:
    """Create a styled Rich table."""
    return Table(title=title, border_style=border_style)

def show_panel(content: str, title: str, border_style: str = 'cyan'):
    """Print a styled Rich panel."""
    console.print(Panel(content, title=title, border_style=border_style))