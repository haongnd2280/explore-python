import configparser


config = configparser.ConfigParser()

# Define DEFAULT section
# DEFAULT section which provides default values for all other sections
config["DEFAULT"] = {
    "ServerAlignInterval": "45",    # keys are case-insensitive when read by configparser
    "Compression": "yes",
    "CompressionLevel": "9"
}

# Define forge.example section
config["forge.example"] = {}
config["forge.example"]["User"] = "hg"

# Define topsecret.server.example section
config["topsecret.server.example"] = {}
print(config["topsecret.server.example"])         # empty dict

topsecret = config["topsecret.server.example"]
topsecret["Port"] = "50022"                       # mutate the parser
topsecret["ForwardX11"] = "no"                    # same here
print(config["topsecret.server.example"])         # we can see the topsecret.server.example is changed

config["DEFAULT"]["FowardX11"] = "yes"

# Write configuration to file
with open("example.ini", "w") as config_file:
    config.write(config_file)      # Keys in sections are case-insensitive and stored in lowercase
