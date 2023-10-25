from connect import *
from checks import *

def updateMovieDetails():
    print('\n\n\n')
    tableColumns = { 0:'filmID', 1:'title', 2:'yearReleased', 3:'rating', 4:'duration', 5:'genre'}
    seletionClause = getSeletionClause( tableColumns )
    setClause = getSetClause( tableColumns )
    print(f'UPDATE tblFilms\n{ setClause }\n{ seletionClause }')

    # dbCursor.execute('UPDATE tblFilms SET ')

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

def getSetClause( columns ):
    optionList = [ '1', '2', '3', '4', '5' ]
    inpRequest = 'What details would you like to change?(Please select a number)\n-----------\n1. Movie Title\n2. Year of release\n3. Rating\n4. Duration\n5. Genre\n-----------\n---: '
    selector = input(inpRequest)
    
    if selector not in optionList:
        selector = getvalidatedOption( selector, inpRequest, optionList )
    
    columnToUpdate = columns[int(selector)]

    if columnToUpdate == 'yearReleased':
        columnName = 'year of release'
    else:
        columnName = columnToUpdate

    updateTo = input(f'What would you like to change the { columnName } to: ')

    setClause = f'SET { columnToUpdate } = { updateTo }'
    return setClause
    
updateMovieDetails()