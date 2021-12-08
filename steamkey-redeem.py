# Redeeming Steam keys.
import steam.client
import re


def read_keys(fn='keys.txt'):
    keys = []
    with open(fn, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        ret = get_key(line)
        if ret:
            key = ret
            name = lines[i-2]
            
            keys.append((name, key))
    return keys

def get_key(line):
    if '-' in line:
        split = line.split(' ')
        key = split[-1]
       
        if key.count('-') == 2:
            return key
        else: 
            return None

def redeem(keys):
    # Init Steam client.
    steam_client: steam.client.SteamClient = steam.client.SteamClient()

    print("Steam Login \n")
    # Login to Steam client.
    steam_client.cli_login()

    for name, key in keys:
        # Print current key.
        print("Name:", name, "Key:", key)

        # Try to redeem key.
        eresult, result_details, receipt_info = steam_client.register_product_key(key)

        # Has game already?
        has_already = eresult == steam.client.EResult.Fail and result_details == 9

        # If did not has already and did not success.
        if not has_already and eresult != steam.client.EResult.OK:
            # Raise exception.
            print("Code redeem failed!", eresult, result_details, receipt_info)
            continue
            #raise Exception("Code redeem failed!", eresult, result_details, receipt_info)


        if has_already:
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
