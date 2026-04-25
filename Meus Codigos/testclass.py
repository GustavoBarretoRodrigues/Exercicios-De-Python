from rich.console import Console
from rich.panel import Panel

console = Console()
console.print("[bold red]Teste de Cor[/] funcionando!")
console.print(Panel("Painel Colorido", style="on blue", title="Sucesso"))