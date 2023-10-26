from Connect import *
from tabulate import tabulate

def printAllRecords():
    dbCursor.execute('SELECT title, yearReleased, duration, rating, genre FROM tblFilms')
    filmsTable = dbCursor.fetchall()
    headers = ['Title', 'Year Released', 'Duration(mins)', 'Rating', 'Genre']
    print('\n\n\n', tabulate(filmsTable, headers=headers, tablefmt='presto', numalign='left'), '\n\n\n')
    if input('\nEnter any key to continue...'): return

if __name__ == '__main__':
    printAllRecords()