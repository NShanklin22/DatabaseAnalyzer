import re
def analyzeDatabase(databaseNames, approvedNames):
    # Define list to store correct and incorrect names
    correctNames = []
    incorrectNames = []

    # Grade to track % names approved
    Grade = 0

    for i in range(len(databaseNames)):
        name = databaseNames[i]
        if name[0] == "x":
            name = name[1:]
        if re.search(r'\d', name):
            non_digit_chars = re.findall(r'\D', name)
            name = "".join(non_digit_chars)

        print(name[0:2])
        if name[0:2] == "Zn":
            name = name[0:2] + name[3:]
            print(name)

        if(name in approvedNames.values):
            correctNames.append(name)
        else:
            incorrectNames.append(name)

    #Write the filtered names to a csv file
    with open('data/correctNames.csv', 'w') as f:
        for i in range(len(correctNames)):
            f.write(f"{correctNames[i]}\n")

    #Write the filtered names to a csv file
    with open('data/incorrectNames.csv', 'w') as f:
        for i in range(len(incorrectNames)):
            f.write(f"{incorrectNames[i]}\n")

    Grade = len(correctNames) / (len(correctNames) + len(incorrectNames)) * 100
    Grade = round(Grade, 2)

    totalIncorrect = len(incorrectNames)
    totalCorrect = len(correctNames)

    return Grade,totalIncorrect,totalCorrect