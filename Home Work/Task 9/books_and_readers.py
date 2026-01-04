books = [ dict(book_id=1001, title="Harry Potter", genre="fantasy", pages=500),
          dict(book_id=1002, title="A song of Ice and Fire", genre="fantasy", pages=700),
          dict(book_id=1003, title="1984", genre="classic", pages=800)
        ]

readers = [ {"name": "gogo", "borrowed": [1001, 1003]},
            {"name": "momo", "borrowed": [1002]},
            {"name": "yoyo", "borrowed": [1001, 1002]}
          ]

def books_by_genre(books, the_genre):
    res =[]
    avg=0
    counter=0
    temp=0
    for i in range(len(books)):
        if the_genre == books[i]['genre']:
            res.append(books[i]['title'])
            counter+=1
            temp+=books[i]['pages']
    if counter>0:
        avg=temp/counter
    return(res,avg)

def main():
    print(books_by_genre(books,'fantasy'))
    print(books_by_genre(books,'classic'))
    print(books_by_genre(books,"h"))

    
if __name__== "__main__":
    main()
    
            