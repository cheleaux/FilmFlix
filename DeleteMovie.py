from connect import *

def inputFromAvailible( column ):
    dbCursor.execute('SELECT DISTINCT ? FROM tblFilms', column )
    results = dbCursor.fetchall()
    counter = 1
    inputString = 'Please select from following options:'
    checkList = []

    for item in results:
        itemString = item[0] if isinstance( item[0], str ) else str(item[0])
        listItem = f'\n{ str( counter ) }. { itemString }'
        inputString += listItem
        checkList.append(itemString)
        counter += 1

    value = input(f'{ inputString }\n\n---: ')

    while value not in checkList:
        print('\n\n--- Invalid Selection\n\n')
        value = input(f'{ inputString }\n\n---: ')
    
    return value


# def getDeletionValue( column ):
#     if column == 'title' or column == 'filmID':
#         return input(f'Please enter the { column }: ')
#     else:
#         return inputFromAvailible( column )
        

# def getDeletionColumn():
#     deleteByInt = input('Choose to delete by:\n1. Movie ID\n2. Movie Title\n\nOr\n\nDelete all films of specied...\n3. Year Of Release\n4. Rating\n5. Genre')
#     if deleteByInt == 1:
#         deleteBy = 'filmID'
#     elif deleteByInt == 2:
#         deleteBy = 'title'
#     elif deleteByInt == 3:
#         deleteBy = 'yearReleased'
#     elif deleteByInt == 4:
#         deleteBy = 'rating'
#     elif deleteByInt == 5:
#         deleteBy = 'genre'
#     return deleteBy

# def DeleteMovie():
#     deletionColumn = getDeletionColumn()
#     deletionValue = getDeletionValue( deletionColumn )
#     deletionQuery = f'DELETE FROM tblFilms WHERE { deletionColumn } = ?'
#     dbCursor.execute( deletionQuery, deletionValue )

