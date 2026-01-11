books = [ dict(book_id=1001, title="Harry Potter", genre="fantasy", pages=500),
          dict(book_id=1002, title="A song of Ice and Fire", genre="fantasy", pages=700),
          dict(book_id=1003, title="1984", genre="classic", pages=800)
        ]

readers = [ {"name": "gogo", "borrowed": [1001, 1003]},
            {"name": "momo", "borrowed": [1002]},
            {"name": "yoyo", "borrowed": [1001, 1002]},
            {"name": "dodo", "borrowed": [1002]}
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

def get_books_name_for_reader(books, readers, reader_name):
    res=[]
    ids = []
    for reader in readers:
        if reader_name in reader['name']:
            ids=reader["borrowed"]
            break
    for i in range (len(books)):
        for j in range(len(ids)):
            if ids[j] == books[i]["book_id"]:
                res.append(books[i]["title"])
    return res

def most_read_book(books, readers):
    ids=dict()
    for reader in readers:
        for id in reader['borrowed']:
            if id not in ids:
                ids[id] = 1
            else:
                ids[id] += 1

    if ids == {}:
        return set()
    maximum=max(ids.values())

    most_borrow_ids=[]
    for id,count in ids.items():
        if count==maximum:
            most_borrow_ids.append(id)

    result = set()
    for book in books:
        if book['book_id'] in most_borrow_ids:
            result.add(book['title'])
    return result

def loan_book(books, readers, reader_name, book_name):
    ids=0
    check=True
    for book in books:
        if book_name != book['title']:
            check=False
        else:
            ids=book['book_id']
            check=True
            break
    if check == False:
        return check

    reader_index=0
    for milon in readers:
        if reader_name != milon['name']:
            check=False
            reader_index +=1
        elif ids in milon['borrowed']:
            check=False
            reader_index += 1
        else:
            check=True
            break

    if check==False:
        return check
    else:
        readers[reader_index]['borrowed'].append(ids)
        return check

def return_book(books, readers, reader_name, book_name):
    ids = 0
    check = True
    for book in books:
        if book_name != book['title']:
            check = False
        else:
            ids = book['book_id']
            check = True
            break
    if check == False:
        return check

    reader_index = 0
    for milon in readers:
        if reader_name != milon['name']:
            check = False
            reader_index += 1
        elif ids in milon['borrowed']:
            check = True
            break
        else:
            check = False
            reader_index += 1


    if check == False:
        return check
    else:
        readers[reader_index]['borrowed'].remove(ids)
        return check

def readers_having_most_read_book(readers):
    ids = dict()
    for reader in readers:
        for id in reader['borrowed']:
            if id not in ids:
                ids[id] = 1
            else:
                ids[id] += 1

    maximum = max(ids.values())

    most_borrow_ids = []
    for id, count in ids.items():
        if count == maximum:
            most_borrow_ids.append(id)


    names = set()
    for milon in readers:
        for id in most_borrow_ids:
            if id in milon['borrowed']:
                names.add(milon['name'])

    return names

def main():
    print(books_by_genre(books,'fantasy'))
    print()
    print(get_books_name_for_reader(books, readers, 'gogo'))
    print()
    print(most_read_book(books,readers))
    print()
    print(loan_book(books,readers,"momo","1984"))
    print()
    print(return_book(books,readers,"momo","stam book"))
    print(readers_having_most_read_book(readers))

if __name__== "__main__":
    main()
    
            