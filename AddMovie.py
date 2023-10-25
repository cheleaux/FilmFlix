from connect import *
from checks import *

def insertSong(): 
    print('\n\n\n')
    insertion = {
        'movieTitle': input('Movie Title: ').title(),
        'releaseYear': int(input('Year Of Release: ')),
        'duration': int(input('Duration (minutes): ')),
        'rating': getContentRating(),
        'genre': getGenre().title()
    }

    if confirmInsert( insertion.values() ):
        processInsert( insertion.values() )
    else:
        print('\n\nInsert cancelled...')

def getContentRating():
    print('\n\n')
    optionList = ['1', '2', '3']
    ratingList = ['G','PG','R']
    inpRequest = 'Content Rating:\n-----------\n1. G - General Audiences\n2. PG - Parental Guidence Advised\n3. R - Restricted\n--: '
    selector = input(inpRequest)

    if selector not in optionList:
        selector = getvalidatedOption( selector, inpRequest, optionList )

    rating = ratingList[int(selector)-1]
    return rating

def getGenre():
    print('\n\n')
    genreList = ['Action','Animation','Crime','Comedy','Fantasy','Fighting','Sci-Fi','Adventure']
    optionList = ['1', '2', '3', '4', '5', '6', '7', '8' ]
    inpRequest = 'Genre:\n-----------\n1. Action\n2. Animation\n3. Crime\n4. Comedy\n5. Fantasy\n6. Fighting\n7. Sci-Fi\n8. Adventure\n--: '

    selector = input( inpRequest )
    if selector not in optionList:
        selector = getvalidatedOption( selector, inpRequest, optionList )
        
    genre = genreList[int(selector)-1]
    return genre

def confirmInsert( insertion ):
    print(insertion)
    title, year, duration, rating, genre = insertion
    record = ' | '.join([title, str(year), (str(duration) + ' mins'), rating, genre])
    inpRequest = f'Please confirm you would like to confirm the following insert (Y/N):\n-----------\n{ record }\n-----------\n---: '
    selector = getvalidatedOption( None, inpRequest )
    return isConfirmed( selector )

def processInsert( insertion ):
    title, year, duration, rating, genre = insertion
    dbCursor.execute('INSERT INTO tblFilms VALUES ( NULL, ?, ?, ?, ?, ? )', ( title, year, duration, rating, genre ))
    dbCon.commit()
    print('Movie has been inserted...')

if __name__ == '__main__':
    insertSong()