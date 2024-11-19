import configparser


config = configparser.ConfigParser()
print(config.sections())     # empty list 

config.read("example.ini")
print(config.sections())     # 2 sections (enclosed by []); does not print DEFAULT section

print("forge.example" in config)
print("python.org" in config)

print(config["forge.example"]["User"])
print(config["forge.example"]["user"])     # same as above, as key is case-insensitive

print(config["DEFAULT"]["Compression"])    # section is case-sensitive
print(config["DEFAULT"]["compression"])    # same as above

topsecret = config["topsecret.server.example"]
print(topsecret["ForwardX11"])
print(topsecret["forwardx11"])
print(topsecret["Port"])

for key, value in config["forge.example"].items():
    print(key, value, sep=": ")      # this will print all the keys in DEFAULT section as well

for key, value in config["topsecret.server.example"].items():
    print(key, value, sep=": ")      # this will print all the keys in DEFAULT section as well