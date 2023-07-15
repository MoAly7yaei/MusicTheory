from main import *
import openai


key = open("API_KEY.txt", "r")
openai.organization = "org-Ha0wnxNbk8ahY55M08rvOFuu"
openai.api_key = key.read()
key.close()
openai.Model.list()
from random import *


i = 5
output = []

while i != 0:
    msg = ""
    n = int(input("You have to select the root note of the scale using numbers (Read the Readme.txt file for more details): "))
    scale_name = input("You have to select the name of the scale mentioned in Readme.txt: ")

    msg = "Please Read every note without skipping one: "
    msg = msg + str(scale_finder(n,scale_name))
    msg = msg + " if the root note is "
    msg = msg + NOTES[n]
    msg = msg + ". with knowing that b is mean bemol find out about this musical scale, and tell me breaf info about it."

    
    response = openai.Completion.create(model="text-davinci-003", prompt = msg, temperature= 0.77, max_tokens=3700)

    conf = "If the set of note: " + str(scale_finder(n,scale_name)) + " Are not Related to the text: " + str(response) + " Just Confirm it without saying yes or no."

    response2 = openai.Completion.create(model="text-davinci-003", prompt = conf, temperature= randrange(0,1), max_tokens=3700)


    print()
    print("Scale Note is: ", str(scale_finder(n,scale_name)))
    print()
    print(response.choices[0].text)
    print()
    print("The Message below is a conformation if the Answer above was Correct or not: ",response2.choices[0].text)


    i -= 15