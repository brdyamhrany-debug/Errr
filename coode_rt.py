import random
import os
import time
import sys

# Color settings for Termux
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    banner = f"""
{RED}#################################################
#                                               #
#   {WHITE}{BOLD}Filter code enhancement       
       .-"      "-.
      /            \
     |              |
     |,  .-.  .-.  ,|
     | )(/  \__)( |
     |/     /\     \|
     (_     ^^     _)
      \__|IIIIII|__/
       | \IIIIII/ |
       \          /
        --------
.0{RED}                      #
#                                               #
#################################################{RESET}
    """
    print(banner)

def run_logic():
    bag = ("https://Spam.Support.rubika.ir/+999", "https://Support.Spam.ir/+999")
    bag_1 = random.choice(bag)

    numbers = [
        "(8.8.8.8.8.8.8.8.888.8.8.8.88.888.8.8.8.8.8.888.8.8.88)",
        "[support=9.8.7.6.5.4.3.2.1]",
        "(+999=/9.9.9.9.9.9.soport.999.999.999.suport-rubika)",
        "(report/support-rubika/+999/spam)",
        "(78Xrubika-spam)",
        "(1.2.5.8.9.6.3.4.5.3.2.1.4.7.8.5.9.6.1.)",
        "(c-10.00.01.000.01.01.10.00.10.01.11.000)",
        "(#rubika-spam-support=/+999)",
        "(11.11.support-spam.12.12)",
        "(111.222.999.888.666.555.444.333.777)",
        "(1.5.6.999.8.6.2.4.6.2.3.4.1.5.8)",
        "(10.9.8.7.6.5.4.3.2.1.0)",
        "(Yftth://Spam_Account.sopport.Bot)"
    ]

    start_number = str(random.randint(0, 0))
    result = start_number + '+' + '+'.join([str(random.choice(numbers)) for _ in range(9)])
    return f"{bag_1}.{result}"

def main():
    print_banner()
    user_input = input(f"{YELLOW} [COODE filtre]: {RESET}")
    print(f"\n{CYAN}[*] Processing with input: {user_input}{RESET}")
    time.sleep(1) 
    print(f"{CYAN}[*] Generating Spam Chain...{RESET}")
    time.sleep(1.5)

    final_result = run_logic()
    
    print("\n" + "="*50)
    print(f"{GREEN}{BOLD}SUCCESSFUL OUTPUT:{RESET}")
    print(f"{RED}{final_result}{RESET}")
    print("="*50 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Stopped by user.{RESET}")
