"""Example script demonstrating the usage of the service provided by askhelmut."""

from dotenv import load_dotenv
from rich.console import Console

from askhelmut import Service

console = Console()

load_dotenv()

message = Service.get_hello_world()
console.print(f"[blue]{message}[/blue]")
