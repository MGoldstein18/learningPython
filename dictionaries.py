# working with given dictionary to create, modify and display a new dictionary
tarot = {1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune",
         11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

# create empty dictionary
spread = {}

# add key value pairs to new dictionary and remove them from the other one
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

# display the new dictionary with an appropriate sentence
for key, value in spread.items():
    print("Your {key} is the {value} card.".format(key=key, value=value))
