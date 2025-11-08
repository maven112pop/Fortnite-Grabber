import requests
from bs4 import BeautifulSoup
import os
import sys

def print_banner():
    banner = r"""
  ______   _   _          _____                  _       _                   
 |  ____| | \ | |        / ____|                | |     | |                  
 | |__    |  \| |       | |  __   _ __    __ _  | |__   | |__     ___   _ __ 
 |  __|   | . ` |       | | |_ | | '__|  / _` | | '_ \  | '_ \   / _ \ | '__|
 | |      | |\  |       | |__| | | |    | (_| | | |_) | | |_) | |  __/ | |   
 |_|      |_| \_|        \_____| |_|     \__,_| |_.__/  |_.__/   \___| |_|     
                                                            
                    FN GRABBER
    """
    print(banner)

def fn_grabber():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    username = input("Enter Fortnite username: Bossman450    ").strip()
    platform = input("Enter platform (epic): ").strip().lower()

    url = f"https://epic-lookup.com/user/{platform}/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print("\nFetching account ID...\n")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Error accessing site: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")

    # Look for the Account ID (based on the current HTML structure)
    account_id_elem = soup.find("strong", class_="font-mono text-sm break-all")

    if account_id_elem:
        # If the Account ID is found, print it
        print(f"✅ Account ID for {username} on {platform}:\n\n{account_id_elem.text.strip()}\n")
    else:
        # If not found, print a message
        print(f"❌ Account ID not found for {username} on {platform}. Please check the username and platform.\n")

    # Prevent terminal from closing automatically
    input("Press Enter to exit...")

# Run it
if __name__ == "__main__":
    fn_grabber()
