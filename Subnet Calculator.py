def klasse(IP):
    # finder ud af hvilken klasse ip'en tilhøre ved at tjekke om det første tal i ip'en er mellem de bestemte ranges
    """
    klasse.__doc__ = En klasse der tager en string med en ip addresse, og returner en string alt efter hvilken ip den bliver givet
    """
    Dontfail = True
    if 0 <= IP[0] <= 127:
        return ("denne ip tilhøre klasse A")
    elif 128 <= IP[0] <= 191:
        return ("denne ip tilhøre klasse B")
    elif 192 <= IP[0] <= 255:
        return ("Denne ip tilhøre klasse C")
    else:
        return ("Dette er ikke en gyldig ip")


bits = [128, 64, 32, 16, 8, 4, 2, 1]


def subnet_mask(Prefix):
    # otte_bit finder det antal oktetter der skal have 8 bits
    otte_bit = int(Prefix / 8)
    # Subnetmask bruger den variable fra otte_bit til at lægge 255 * variabel til subnetmasken
    Subnetmask = otte_bit * "255."
    # rest finder ud af hvor mange bits der er tilbage udover det 8 går op i
    rest = Prefix % 8
    x = 0
    y = 0
    # her bruges et loop, en liste og 2 variabler til at fastlå hvor meget den sidste oktet skal være på
    for i in range(rest):
        x += bits[y]
        y += 1
    nuller = ''
    if Prefix <= 8:
        nuller = '.0.0'
    elif 8 <= Prefix <= 16:
        nuller = '.0.0'
    elif 17 <= Prefix <= 23:
        nuller = '.0'

    return f'{Subnetmask}{x}{nuller}'


prefix = int(input("Hvad er dit prefix: "))
ip = input("hvad er din ip: ")

# får outputtet fra function i en iterable
subnet_str = subnet_mask(prefix)
# splitter str ip ud i en STR liste
test = ip.split(".")
#
subnet_int = subnet_str.split(".")
# laver ip om til en INT liste
test = list(map(int, test))
# laver subnet om til en INT liste
subnet_int = list(map(int, subnet_int))

NetworkAddress = [test[0] & subnet_int[0],
                  test[1] & subnet_int[1],
                  test[2] & subnet_int[2],
                  test[3] & subnet_int[3]]

BroadcastAddress = [NetworkAddress[0] | (255 - subnet_int[0]),
                    NetworkAddress[1] | (255 - subnet_int[1]),
                    NetworkAddress[2] | (255 - subnet_int[2]),
                    NetworkAddress[3] | (255 - subnet_int[3])]

NetworkAddress = ".".join(str(i) for i in NetworkAddress)
BroadcastAddress = ".".join(str(i) for i in BroadcastAddress)
print(klasse(test))
print(f'adressens subnet mask: {subnet_mask(prefix)}')
print(f'network address: {NetworkAddress}')
print(f'broadcast adresse: {BroadcastAddress}')