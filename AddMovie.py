from connect import *

def insertSong(): 
    movieTitle = input('Movie Title: ')
    releaseYear = int(input('Year Of Release: '))
    duration = int(input('Duration (minutes): '))
    
    # MULTI-CHOICE INPUTS -------

    # rating ----
    ratingInt = int(input('Content Rating:\n1. G - General Audiences\n2. PG - Parental Guidence Advised\n3. R - Restricted\n--:'))
    if ratingInt == 1:
        rating = 'G'
    elif ratingInt == 2:
        rating = 'PG'
    elif ratingInt == 3:
        rating = 'R'

    # genre ----
    genreInt = int(input('Genre:\n1. Action\n2. Animation\n3. Crime\n4. Comedy\n5. Fantasy\n6. Fighting\n7. Sci-Fi\n8. Adventure\n--:'))
    if genreInt == 1:
        genre = 'Action'
    elif genreInt == 2:
        genre = 'Animation'
    elif genreInt == 3:
        genre = 'Crime'
    elif genreInt == 4:
        genre = 'Comedy'
    elif genreInt == 5:
        genre = 'Fantasy'
    elif genreInt == 6:
        genre = 'Fighting'
    elif genreInt == 7:
        genre = 'Sci-Fi'
    elif genreInt == 8:
        genre = 'Adventure'

    dbCursor.execute('INSERT INTO tblFilms VALUES ( NULL, ?, ?, ?, ?, ? )', ( movieTitle, releaseYear, duration, rating, genre ))
    dbCon.commit()

if __name__ == '__main__':
    insertSong()