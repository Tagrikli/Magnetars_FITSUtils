from CustomFITSParser import FitsParser

file = "P1_100716044_1.fit"

parser = FitsParser(file)
with open("sample.json",'w') as file:
    file.write(parser.to_JSON())

