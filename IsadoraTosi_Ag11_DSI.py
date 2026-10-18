# Lista com os níveis de água do reservatório
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)


# Define uma cor para cada nível de água
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE


# Exibe os níveis de água no terminal
for i in range(len(niveis)):
    nivel = i + 1
    cor = definir_cor(nivel)
    mensagem = niveis[i]

    print(cor + f"Nível {nivel}: {mensagem}" + Style.RESET_ALL)