
def getvalidatedOption( selection, request, options = ['Y', 'N']):
    if selection == None:
        selection = input(request).upper()
    while selection not in options:
            print('\n\n--- Invalid Selection\n\n')
            selection = input(request).upper()
    return selection

# Todo: stop getvalidatedOption from running twice 

def isConfirmed( selector ):
    if selector == 'Y':
        return  True
    if selector == 'N':
        return False
