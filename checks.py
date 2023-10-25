
def getValidOption( selection, optionList, request ):
    while selection not in optionList:
        print('\n\n--- Invalid Selection\n\n')
        selection = input(request)
    return selection
