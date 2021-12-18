# Redeeming Steam keys.
import steam.client
import re
import time

STEAM_MAX_ALLOWED_REDEMPTIONS = 50
STEAM_COOLDOWN_MINUTES = 60
STEAM_INCORRECT_REDEMPTION_PENALTY = 2

def read_keys(fn='keys.txt'):
    keys = []
    with open(fn, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        check = get_key(line)
        if check:
            name = lines[i-1]
            key = line.split(' ')[2]
            keys.append(key)
            print(name, key)
    return keys

def get_key(line):
    key = re.findall(r'(\w{5}-){2}\w{5}', line)
    return key

def check_attempts(attempt_count):
    if attempt_count > STEAM_MAX_ALLOWED_REDEMPTIONS:
        print("Maximum amount of redemptions reached.")
        print("Waiting " + str(STEAM_COOLDOWN_MINUTES) + " minutes.")
        print("This program can be safely stopped and restarted after the allotted time.")
        time.sleep(60*STEAM_COOLDOWN_MINUTES)
        return 0
    return attempt_count + 1

def redeem(keys):
    # Init Steam client.
    steam_client: steam.client.SteamClient = steam.client.SteamClient()
    attempt_count = 0

    print("Steam Login \n")
    # Login to Steam client.
    steam_client.cli_login()

    for key in keys:
        # Print current key.
        print("Key:", key)

        attempt_count = check_attempts(attempt_count)
        # Try to redeem key.
        result, result_details, receipt_info = steam_client.register_product_key(key)

        # Has game already?
        has_already = result == steam.client.EResult.Fail and result_details == 9

        # If did not has already and did not success.
        if not has_already and result != steam.client.EResult.OK:
            # Raise exception.
            print("Code redeem failed!", result, result_details, receipt_info)
            attempt_count = attempt_count + STEAM_INCORRECT_REDEMPTION_PENALTY
            #raise Exception("Code redeem failed!", result, result_details, receipt_info)


        if has_already:
            attempt_count = attempt_count + STEAM_INCORRECT_REDEMPTION_PENALTY
            print("Already have game")

        # Key was redeemed.
        else:
            print("\tRedeemed!")

    # Logout from Steam.
    steam_client.logout()


if __name__ == '__main__':
    keys = read_keys()
    redeem(keys)
    exit(0)