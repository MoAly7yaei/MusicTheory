from main import *
import openai
openai.organization = "org-Ha0wnxNbk8ahY55M08rvOFuu"
openai.api_key = "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"
openai.Model.list()


i = 5
output = []

while i != 0:
    msg = ""
    n = int(input("You have to select the root note of the scale using numbers (Read the Readme.txt file for more details): "))
    scale_name = input("You have to select the name of the scale mentioned in Readme.txt: ")

    msg = "find out more about this music scale notes: "
    msg = msg + scale_finder(n,scale_name)
    #response = openai.ask(scale_finder(n,scale_name))
    response = openai.Completion.create(model="text-davinci-003", prompt=msg, temperature=1, max_tokens=3000)

    print(response["choices"])

    print()
    i -= 1