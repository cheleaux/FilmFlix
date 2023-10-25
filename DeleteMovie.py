from connect import *

def inputFromAvailible( column ):
    query = f'SELECT DISTINCT { column } FROM tblFilms'
    dbCursor.execute( query )
    results = dbCursor.fetchall()
    counter = 1
    inputString = '\n\nPlease select from following options:\n-----------'
    checkList = []

    for item in results:
        itemString = item[0] if isinstance( item[0], str ) else str(item[0])
        listItem = f'\n{ str( counter ) }. { itemString }'
        inputString += listItem
        checkList.append(itemString)
        counter += 1

    selection = input(f'{ inputString }\n\n---: ')

    while int(selection) not in range(1,len(checkList)):
        print('\n\n--- Invalid Selection\n\n')
        selection = input(f'{ inputString }\n\n---: ')
    
    value = checkList[int(selection)-1]

    return value

def getDeletionValue( column ):
    if column == 'title' or column == 'filmID':
        return input(f'Please enter the { column if column != "filmID" else "movie ID"  }: ')
    else:
        return inputFromAvailible( column )

def getDeletionColumn():
    inputText = 'Choose to delete by:\n-----------\n1. Movie ID\n2. Movie Title\n\nOr\n\nDelete all films of specied...\n-----------\n3. Year Of Release\n4. Rating\n5. Genre\n----: '
    
    deleteByInt = int(input(inputText))

    while deleteByInt not in range( 1, 6 ):
        print('\n\n!!Invalid Selection!!\n')
        deleteByInt = int(input(inputText))

    if deleteByInt == 1:
        deleteBy = 'filmID'
    elif deleteByInt == 2:
        deleteBy = 'title'
    elif deleteByInt == 3:
        deleteBy = 'yearReleased'
    elif deleteByInt == 4:
        deleteBy = 'rating'
    elif deleteByInt == 5:
        deleteBy = 'genre'

    return deleteBy

def constructionComfirmationString( itemList ):
    toBeDeletedStr = f'\n\nThe following will be deleted:\n-----------'
    if len(itemList) > 1:
        for item in itemList:
            itemStr = f'\n{item[0]}'
            toBeDeletedStr += itemStr
    elif len(itemList) == 1:
        toBeDeletedStr += f'  { itemList[0][0] }'
    else:
        print('Movie does not exist')
    return toBeDeletedStr

def getConfirmation( comfirmationStr ):
    optionList = ['Y','N']
    confirmation = input( comfirmationStr + '\n-----------\nPlease confirm (Y/N)\n---: ')
    while confirmation.upper() not in optionList:
        print('\n\n--- Invalid Selection\n\n')
        confirmation = input( comfirmationStr + '\n-----------\nPlease confirm (Y/N)\n---: ')
    if confirmation.upper() == 'Y':
        return  True
    if confirmation.upper() == 'N':
        return False
    
def DeleteMovie():
    deletionColumn = getDeletionColumn()
    deletionValue = getDeletionValue( deletionColumn )
    if deletionColumn == 'filmID':
        condition = str(deletionValue)
    else:
        condition = (f'%{ deletionValue }%')

    confirmationQuery = f"SELECT title FROM tblFilms WHERE LIKE( ?, { deletionColumn })"

    dbCursor.execute( confirmationQuery, [condition] )
    toBeDeleted = dbCursor.fetchall()

    if len(toBeDeleted) >= 1:
        comfirmationString = constructionComfirmationString( toBeDeleted )
        if getConfirmation( comfirmationString ):
            deletionQuery = f'DELETE FROM tblFilms WHERE LIKE( ?, { deletionColumn })'
            dbCursor.execute( deletionQuery, [condition] )
            dbCon.commit()
            print(f'\n\nItem(s) have been deleted\n\n')
        elif not getConfirmation( comfirmationString ):
            print('\n\nItem(s) will not be deleted\n\n')
            
if __name__ == '__main__':
    DeleteMovie()