from connect import *

def insertSong(): 
    print('\n\n\n')
    movieTitle = input('Movie Title: ').title()
    releaseYear = int(input('Year Of Release: '))
    duration = int(input('Duration (minutes): '))
    rating = getContentRating()
    genre = getGenre().title()

    record = ' | '.join([movieTitle, str(releaseYear), (str(duration) + ' mins'), rating, genre])
    if confirmInsert( record ):
        dbCursor.execute('INSERT INTO tblFilms VALUES ( NULL, ?, ?, ?, ?, ? )', ( movieTitle, releaseYear, rating, duration, genre ))
        dbCon.commit()
        print('Movie has been inserted...')
    else:
        print('\n\nInsert cancelled...')

def getContentRating():
    print('\n\n\n')
    ratingInt = int(input('Content Rating:\n-----------\n1. G - General Audiences\n2. PG - Parental Guidence Advised\n3. R - Restricted\n--: '))
    ratingList = ['G','PG','R']
    rating = ratingList[ratingInt-1]
    return rating

def getGenre():
    print('\n\n\n')
    genreInt = int(input('Genre:\n1. Action\n2. Animation\n3. Crime\n4. Comedy\n5. Fantasy\n6. Fighting\n7. Sci-Fi\n8. Adventure\n--: '))
    genreList = ['Action','Animation','Crime','Comedy','Fantasy','Fighting','Sci-Fi','Adventure']
    genre = genreList[genreInt-1]
    return genre

def confirmInsert( entry ):
    optionList = ['Y','N']
    confirmation = input(f'Please confirm you would like to confirm the following insert (Y/N):\n-----------\n{ entry }\n-----------\n---: ')
    while confirmation.upper() not in optionList:
        print('\n\n--- Invalid Selection\n\n')
        confirmation = input(f'Please confirm you would like to confirm the following insert (Y/N):\n-----------\n{ entry }\n-----------\n---: ')
    if confirmation.upper() == 'Y':
        return  True
    if confirmation.upper() == 'N':
        return False

if __name__ == '__main__':
    insertSong()