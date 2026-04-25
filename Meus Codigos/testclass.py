from rich.console import Console
from rich.panel import Panel

# Força o sistema de cores (color_system pode ser "standard", "256" ou "truecolor")
console = Console(force_terminal=True, color_system="truecolor")

console.print("[bold red]Teste de Cor[/] funcionando!")
console.print(Panel("Painel Colorido", style="on blue", title="Sucesso"))