import sys
from os import system as system

# convert key_string to a dictionary
keys = """Win 10 Home: TX9XD-98N7V-6WMQ6-BX7FG-H8Q99,
            Win 10 Home N: 3KHY7-WNT83-DGQKR-F7HPR-844BM,
            Win 10 Home Single Language: 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH,
            Win 10 Home Country Specific: PVMJN-6DFY6-9CCP6-7BKTT-D3WVR,
            Win 10 Professional: W269N-WFGWX-YVC9B-4J6C9-T83GX,
            Win 10 Professional N: MH37W-N47XK-V7XM9-C7227-GCQG9,
            Win 10 Education: NW6C2-QMPVW-D7KKK-3GKT6-VCFB2,
            Win 10 Education N: 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ,
            Win 10 Enterprise: NPPR9-FWDCX-D2C8J-H872K-2YT43,
            Win 10 Enterprise N: DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4 3"""
keys = keys.replace(" ", "").replace("\n", "").split(",")
keys = {key_string.split(":")[0]: key_string.split(":")[1] for key_string in keys}

# show up the names from the keys
print("#" * 1000)
for i, (name, key) in enumerate(keys.items()):
    print("{}: {}".format(i, name))

print(": any key to esc...")
print("#" * 1000)
print("This script need ADMIN rights to activate windows!")

# select a key
try:
    choice = int(input("Select your prefered version:\n"))
    assert 0 < choice < len(keys)

except ValueError:
    print("Couldn't convert input!")
    sys.exit(2)

except AssertionError:
    print("Please enter a number between {} and {}".format(0, len(keys)))
    sys.exit(2)

selected = list(keys.items())[choice]
print("selected {}".format(selected[0]))

# start activation process
print("activation starts...")
commands = ["slmgr /upk", "slmgr.vbs /cpky", "slmgr /ckms", "slmgr /skms localhost",
            "slmgr /ipk {}".format(selected[1]), "slmgr /skms kms.digiboy.ir", "slmgr /ato"]
for cmd in commands:
    system(cmd)

print("mybe succesfull!")
sys.exit("succesfull!")
