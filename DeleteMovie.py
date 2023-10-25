from connect import *
from checks import *

def DeleteMovie():
    print('(Please select using the numbered options)')
    deletionColumn = getDeletionColumn()
    deletionValue = getDeletionValue( deletionColumn )
    confirmationQuery = f"SELECT title FROM tblFilms WHERE LIKE( ?, { deletionColumn })"

    if deletionColumn == 'filmID':
        condition = str(deletionValue)
    else:
        condition = (f'%{ deletionValue }%')

    toBeDeleted = getSelectedList( confirmationQuery, condition )
    if toBeDeleted:
        processDeleteQuery( toBeDeleted, deletionColumn, condition )
    else:
        print('\n\nItem(s) does not exist\n\n')
        return

def getDeletionColumn():
    optionList = [ '1', '2', '3', '4', '5', '6']
    columns = {1:'filmID', 2:'title', 3:'yearReleased', 4:'rating', 5:'genre'}
    
    inputText = 'Choose to delete by:\n-----------\n1. Movie ID\n2. Movie Title\n\nOr\n\nDelete all films of specied...\n-----------\n3. Year Of Release\n4. Rating\n5. Genre\n----: '
    selector = input(inputText)
    if selector not in optionList:
        selector = getvalidatedOption( selector, inputText, optionList)

    deleteBy = columns[int(selector)]
    return deleteBy

def getDeletionValue( column ):
    if column == 'title' or column == 'filmID':
        return input(f'Please enter the { column if column != "filmID" else "movie ID"  }: ')
    else:
        return inputFromAvailible( column )

def inputFromAvailible( column ):
    query = f'SELECT DISTINCT { column } FROM tblFilms'
    dbCursor.execute( query )
    results = dbCursor.fetchall()
    counter = 1
    inputString = 'Please select from following options:\n-----------'
    checkList = []

    for item in results:
        itemString = item[0] if isinstance( item[0], str ) else str(item[0])
        listItem = f'\n{ str( counter ) }. { itemString }'
        inputString += listItem
        checkList.append(itemString)
        counter += 1

    optionList = list(map(lambda x: str(x), range(1,len(checkList)+1)))
    selector = input(f'{ inputString }\n\n---: ')
    if selector not in optionList:
        selector = getvalidatedOption( selector, f'{ inputString }\n\n---: ', optionList )

    value = checkList[int(selector)-1]
    return value

def getSelectedList( query, condition):
    dbCursor.execute( query, [ condition ] )
    return dbCursor.fetchall()

def constructionComfirmationString( itemList ):
    toBeDeletedStr = f'\n\nThe following will be deleted:\n-----------'
    if len(itemList) >= 1:
        for item in itemList:
            itemStr = f'\n{item[0]}'
            toBeDeletedStr += itemStr
    else:
        print('Movie does not exist')
        return
    toBeDeletedStr += '\n-----------\nPlease confirm (Y/N)\n---: '
    return toBeDeletedStr

def getConfirmation( confirmationStr ):
    selector = getvalidatedOption( None, confirmationStr )
    return isConfirmed( selector )

def processDeleteQuery( itemList, column, condition ):
        comfirmationString = constructionComfirmationString( itemList )
        if getConfirmation( comfirmationString ):
            deletionQuery = f'DELETE FROM tblFilms WHERE LIKE( ?, { column })'
            dbCursor.execute( deletionQuery, [ condition ] )
            dbCon.commit()
            print(f'\n\nItem(s) have been deleted\n\n')
        elif not getConfirmation( comfirmationString ):
            print('\n\nItem(s) will not be deleted\n\n')

if __name__ == '__main__':
    DeleteMovie()