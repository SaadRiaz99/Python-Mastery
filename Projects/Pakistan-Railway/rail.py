import json
import os


# ==========================================
# Configuration
# ==========================================

FILENAME = "pakrail.json"


# ==========================================
# Colors
# ==========================================

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"


# ==========================================
# Load JSON
# ==========================================

def load_data():

    if not os.path.exists(FILENAME):
        print(
            f"{Colors.RED}❌ File '{FILENAME}' not found!{Colors.RESET}"
        )
        return None

    try:

        with open(
            FILENAME,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except json.JSONDecodeError:

        print(
            f"{Colors.RED}❌ Invalid JSON file!{Colors.RESET}"
        )

        return None


# ==========================================
# Header
# ==========================================

def show_header():

    print(
        f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════╗
║                                              ║
║        🚆  PAKISTAN RAILWAY SYSTEM           ║
║                                              ║
║        Train Management Console              ║
║                                              ║
╚══════════════════════════════════════════════╝
{Colors.RESET}
"""
    )


# ==========================================
# Show Statistics
# ==========================================

def show_statistics(data):

    trains = data["trains"]

    total = len(trains)

    active = sum(
        1 for train in trains
        if train.get("active") is True
    )

    express = sum(
        1 for train in trains
        if train.get("category") == "Express"
    )

    passenger = sum(
        1 for train in trains
        if train.get("category") == "Passenger"
    )

    print(f"""
{Colors.YELLOW}╭────────────── SYSTEM STATISTICS ──────────────╮{Colors.RESET}

  🚆 Total Trains       : {Colors.GREEN}{total}{Colors.RESET}

  🟢 Active Trains      : {Colors.GREEN}{active}{Colors.RESET}

  ⚡ Express Trains     : {Colors.BLUE}{express}{Colors.RESET}

  👥 Passenger Trains   : {Colors.MAGENTA}{passenger}{Colors.RESET}

{Colors.YELLOW}╰───────────────────────────────────────────────╯{Colors.RESET}
""")


# ==========================================
# Show All Trains
# ==========================================

def show_all_trains(data):

    print(
        f"\n{Colors.CYAN}{Colors.BOLD}"
        "🚆 ALL TRAINS"
        f"{Colors.RESET}\n"
    )

    for index, train in enumerate(
        data["trains"],
        start=1
    ):

        status = (
            f"{Colors.GREEN}ACTIVE{Colors.RESET}"
            if train.get("active")
            else f"{Colors.RED}INACTIVE{Colors.RESET}"
        )

        print(
            f"{index:03} │ "
            f"{Colors.YELLOW}{train['number']:<6}{Colors.RESET} │ "
            f"{Colors.BOLD}{train['name']:<30}{Colors.RESET} │ "
            f"{train['from']} → {train['to']} │ "
            f"{status}"
        )


# ==========================================
# Search Train
# ==========================================

def search_train(data):

    query = input(
        f"\n{Colors.CYAN}🔎 Enter train name or number: {Colors.RESET}"
    ).strip().lower()

    results = []

    for train in data["trains"]:

        if (
            query in train["name"].lower()
            or query in train["number"].lower()
        ):
            results.append(train)

    if not results:

        print(
            f"\n{Colors.RED}❌ No train found.{Colors.RESET}"
        )
        return

    print(
        f"\n{Colors.GREEN}✅ {len(results)} train(s) found:{Colors.RESET}\n"
    )

    for train in results:

        print(
            f"""
{Colors.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}

🚆 Train Number : {Colors.YELLOW}{train['number']}{Colors.RESET}

📛 Train Name   : {train['name']}

📂 Category     : {train['category']}

📍 From         : {train['from']}

🏁 To           : {train['to']}

🟢 Status       : {
    'Active'
    if train.get('active')
    else 'Inactive'
}

{Colors.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}
"""
        )


# ==========================================
# Find Route
# ==========================================

def find_route(data):

    source = input(
        f"\n{Colors.CYAN}📍 From: {Colors.RESET}"
    ).strip().lower()

    destination = input(
        f"{Colors.CYAN}🏁 To: {Colors.RESET}"
    ).strip().lower()

    results = []

    for train in data["trains"]:

        if (
            source in train["from"].lower()
            and destination in train["to"].lower()
        ):
            results.append(train)

    if not results:

        print(
            f"\n{Colors.RED}"
            "❌ No direct train found."
            f"{Colors.RESET}"
        )

        return

    print(
        f"\n{Colors.GREEN}"
        f"🚆 {len(results)} train(s) available:"
        f"{Colors.RESET}\n"
    )

    for train in results:

        print(
            f"  {Colors.YELLOW}{train['number']}{Colors.RESET}"
            f"  {train['name']}"
        )


# ==========================================
# Train Details
# ==========================================

def train_details(data):

    number = input(
        f"\n{Colors.CYAN}🚆 Enter train number: {Colors.RESET}"
    ).strip().upper()

    train = next(
        (
            train
            for train in data["trains"]
            if train["number"] == number
        ),
        None
    )

    if not train:

        print(
            f"{Colors.RED}❌ Train not found.{Colors.RESET}"
        )

        return

    print(
        f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════╗
║              TRAIN DETAILS                  ║
╚══════════════════════════════════════════════╝
{Colors.RESET}

🚆 Number       : {Colors.YELLOW}{train['number']}{Colors.RESET}

📛 Name         : {train['name']}

📂 Category     : {train['category']}

📍 Departure    : {train['from']}

🏁 Destination  : {train['to']}

📊 Status       : {
    f"{Colors.GREEN}ACTIVE{Colors.RESET}"
    if train.get("active")
    else f"{Colors.RED}INACTIVE{Colors.RESET}"
}
"""
    )


# ==========================================
# Menu
# ==========================================

def menu():

    print(
        f"""
{Colors.BOLD}{Colors.BLUE}
╔══════════════════════════════════════════════╗
║                 MAIN MENU                    ║
╠══════════════════════════════════════════════╣
║                                              ║
║   1️⃣  Show Statistics                        ║
║   2️⃣  Show All Trains                        ║
║   3️⃣  Search Train                           ║
║   4️⃣  Find Route                             ║
║   5️⃣  Train Details                          ║
║   6️⃣  Exit                                   ║
║                                              ║
╚══════════════════════════════════════════════╝
{Colors.RESET}
"""
    )


# ==========================================
# Main Program
# ==========================================

def main():

    data = load_data()

    if data is None:
        return

    while True:

        show_header()

        menu()

        choice = input(
            f"{Colors.YELLOW}👉 Select option: {Colors.RESET}"
        ).strip()

        if choice == "1":

            show_statistics(data)

        elif choice == "2":

            show_all_trains(data)

        elif choice == "3":

            search_train(data)

        elif choice == "4":

            find_route(data)

        elif choice == "5":

            train_details(data)

        elif choice == "6":

            print(
                f"\n{Colors.GREEN}"
                "🚆 Thank you for using Pakistan Railway System!"
                f"{Colors.RESET}"
            )

            break

        else:

            print(
                f"\n{Colors.RED}"
                "❌ Invalid option!"
                f"{Colors.RESET}"
            )

        input(
            f"\n{Colors.CYAN}"
            "Press Enter to continue..."
            f"{Colors.RESET}"
        )


# ==========================================
# Run
# ==========================================

if __name__ == "__main__":
    main()


    
# with open(filename, "r" , encoding="utf-8") as f:
#     data = json.load(f)
#     for train in data["trains"]:
#         print(
#         train["number"],
#         "-",
#         train["name"],
#         "-",
#         train["from"],
#         "→",
#         train["to"]
#     )


class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
