import json
from fuzzywuzzy import process 

# Load data from json file
data = json.load(open("./data/data.json"))

# When user input not found in db
def notFound(charactor):
    return "Sorry, Found No Information on \""+ charactor+ "\", Please double check!"

# Get charactor information
def charactorInfo(charactor):
    charactor = charactor.upper()

    if charactor in data:
        return data[charactor]

    # Checking charactor match using string comparison
    elif process.extractOne(charactor, data.keys(), score_cutoff=80):
        similarCharcator = process.extractOne(charactor, data.keys(), score_cutoff=80)[0]
        isSimilar = input ("Did you mean %s instead? Enter Y if yes, or N if no: " %similarCharcator) 

        if isSimilar.upper() == "Y":
            return data[similarCharcator]

        else:
            return notFound(charactor)

    else:
        return notFound(charactor)

userInput = input("Enter StarWars Charactor Name: ")
print(charactorInfo(userInput))
