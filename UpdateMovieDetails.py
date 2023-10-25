from connect import *
from checks import *

def updateMovieDetails():
    print('\n\n\n')
    tableColumns = { 0:'filmID', 1:'title', 2:'yearReleased', 3:'rating', 4:'duration', 5:'genre' }
    seletionClause = getSeletionClause( tableColumns )
    setClause = getSetClause( tableColumns )
    updateQuery = f'UPDATE tblFilms { setClause } { seletionClause }'
    # print(updateQuery)
    dbCursor.execute(updateQuery)
    dbCon.commit()
    print('Item has been updated')

def getSeletionClause( columns ):
    optionList = [ '1', '2' ]
    inpRequest = 'How will you select the movie you wish to modify?(Please select a number)\n-----------\n1. Movie ID\n2. Movie Title\n---: '
    selector = input(inpRequest)

    if selector not in optionList:
        selector = getvalidatedOption( selector, inpRequest, optionList )

    column = columns[ int(selector)-1 ]
    selection = input(f'What is the { "movie ID" if selector == "1" else "movie title" }: ')
    selectionClause = f'WHERE { column } = { selection }'
    return selectionClause

def getNewValue( column, selector ):
    if column == 'yearReleased':
        properName = 'year of release'
    else:
        properName = column

    if int(selector) not in range(1,3):
        return f"'{ input(f'What would you like to change the { properName } to: ') }'"
    else:
        return input(f'What would you like to change the { properName } to: ')

def getSetClause( columns ):
    print('\n\n')
    optionList = [ '1', '2', '3', '4', '5' ]
    inpRequest = 'What details would you like to change?(Please select a number)\n-----------\n1. Movie Title\n2. Year of release\n3. Rating\n4. Duration\n5. Genre\n-----------\n---: '
    selector = input(inpRequest)
    
    if selector not in optionList:
        selector = getvalidatedOption( selector, inpRequest, optionList )
    
    columnToUpdate = columns[int(selector)]
    updateTo = getNewValue( columnToUpdate, selector)
    setClause = f'SET { columnToUpdate } = { updateTo }'
    return setClause
    
updateMovieDetails()