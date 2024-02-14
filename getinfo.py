import requests
import datetime

# First, get the user's API key from the file accesskey.txt

# NOTE: if you are running this program yourself, you will need an API key
# from the WSDOT website. You can get one by going to https://wsdot.wa.gov/traffic/api/
# and entering your email.
# WARNING: The accesskey.txt and apiurl.txt must not end with a newline! make sure your
# editor is not automatically inserting them.

akf = open("accesskey.txt", "r")
accesskey = akf.read()
if(accesskey != ""):
    print("Access key succesfully read. (%s)" % accesskey)
else:
    print("Access key file is blank! See readme.md.")
    akf.close()
    exit()

# Next, get the api endpoint url from the file.

urlfile = open("apiurl.txt", 'r')
url = urlfile.read()
if(url != ""):
    print("Succesfully read url %s" % url)
else:
    print("URL file is blank! See readme.md.")
    urlfile.close()
    exit()

akf.close()
urlfile.close()

# Generate the REST request and try to get the data

payload = {'AccessCode' : "{" + accesskey + "}"} # Setup a payload for the request library
response = requests.get(url, params = payload)
print("GET", response.url)

if(response.status_code != requests.codes.ok):
    print("An error occurred. Check your URL and try again. (Error %s)" % response.status_code)
    exit()
else:
    print("Succesfully retrived request with status %s" % response.status_code)

passinfo = response.json()

# Write the recieved data to a file with a particular format. This also strips unneccessary
# information such as elevation, latitude/longitude, etc.

passinfofile = open("passinfo.txt", "w")

for mountain in passinfo:
    formatinfo = (mountain["MountainPassName"] + "|" + mountain["RestrictionOne"]["TravelDirection"] + " - " + mountain["RestrictionOne"]["RestrictionText"] + "|" + mountain["RestrictionTwo"]["TravelDirection"] + " - " + mountain["RestrictionTwo"]["RestrictionText"] + "|" + mountain["RoadCondition"] + "|" + mountain["WeatherCondition"] + "|" +  str(mountain["TemperatureInFahrenheit"]) + "\n")
    print(formatinfo)
    passinfofile.write(formatinfo)

passinfofile.write(str(datetime.datetime.now()))



