# 💡 Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples
# (canal, volume e liga/desliga)

from rich import print
from rich.panel import Panel

class ControleRemoto:
    def __init__(self):
        self.on_off = False
        self.canal = 1
        self.volume = 2
        self.mensagem = "[red]Televisão desligada[/]"

    def atualizar_tela(self):
        if not self.on_off:
            self.mensagem = "[red]Televisão desligada[/]"
        else:
            ## FEITO POR I.A.
            c = [f"[black on yellow] {i} [/]" if i == self.canal else f" {i} "
                for i in range(1, 10)]

            vol = ""
            for i in range(8):
                if i < self.volume:
                    vol += "[cyan]█[/]"
                else:
                    vol += "[grey]█[/]"

            self.mensagem = (
                "[red]@[/] Power\n\n"
                "   CANAL\n"
                f"{c[0]}{c[1]}{c[2]}\n"
                f"{c[3]}{c[4]}{c[5]}\n"
                f"{c[6]}{c[7]}{c[8]}\n\n"
                f"VOLUME: {vol}\n\n"
                "<CH>   + VL -"
            )
            ## ATÉ AQUI

    def screen(self):
        self.atualizar_tela()
        return Panel(self.mensagem, title="[ TV ]", width=30)

    def power(self):
        self.on_off = not self.on_off

    def channel(self, direcao):
        if self.on_off:
            if direcao == ">":
                self.canal = 1 if self.canal == 9 else self.canal + 1
            elif direcao == "<":
                self.canal = 9 if self.canal == 1 else self.canal - 1

    def volume_control(self, direcao):
        if self.on_off:
            if direcao == "+" and self.volume < 8:
                self.volume += 1
            elif direcao == "-" and self.volume > 0:
                self.volume -= 1


# --- Loop ---
tv = ControleRemoto()

while True:
    print(tv.screen())
    entry = input("")

    if entry == "0":
        break
    elif entry == "@":
        tv.power()
    elif entry in "<>":
        tv.channel(entry)
    elif entry in "+-":
        tv.volume_control(entry)