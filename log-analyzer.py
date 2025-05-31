# version améliorée log-analyzer.py
from colorama import Fore, Style, init

init()

def analyser_log(fichier_log):
    stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    with open(fichier_log, "r") as f:
        for ligne in f:
            for niveau in stats:
                if ligne.startswith(niveau):
                    stats[niveau] += 1
                    if niveau == "INFO":
                        print(Fore.BLUE + ligne.strip())
                    elif niveau == "WARNING":
                        print(Fore.YELLOW + ligne.strip())
                    elif niveau == "ERROR":
                        print(Fore.RED + ligne.strip())

    with open("rapport.txt", "w") as rapport:
        rapport.write("=== Rapport de Log ===\n")
        for niveau, count in stats.items():
            rapport.write(f"{niveau}: {count}\n")

    print(Style.RESET_ALL + "Rapport généré dans 'rapport.txt'.")

if __name__ == "__main__":
    analyser_log("log.txt")
