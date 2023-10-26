from connect import *
from checks import *
from Context import *

def insertSong(): 
    print('\n\n\n')
    insertion = {
        'movieTitle': input('Movie Title: ').title(),
        'releaseYear': int(input('Year Of Release: ')),
        'duration': int(input('Duration (minutes): ')),
        'rating': inputFromAvailible( 'rating' ),
        'genre': inputFromAvailible( 'genre' )
    }

    if confirmInsert( insertion.values() ):
        processInsert( insertion.values() )
    else:
        print('\n\nInsert cancelled...')

def confirmInsert( insertion ):
    title, year, duration, rating, genre = insertion
    record = ' | '.join([title, str(year), (str(duration) + ' mins'), rating, genre])
    inpRequest = f'Please confirm you would like to confirm the following insert (Y/N):\n-----------\n{ record }\n-----------\n---: '
    selector = getvalidatedOption( None, inpRequest )
    return isConfirmed( selector )

def processInsert( insertion ):
    title, year, duration, rating, genre = insertion
    dbCursor.execute('INSERT INTO tblFilms VALUES ( NULL, ?, ?, ?, ?, ? )', ( title, year, rating, duration, genre ))
    dbCon.commit()
    print('Movie has been inserted...')

if __name__ == '__main__':
    insertSong()