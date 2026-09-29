from operator import index
from tokenize import String


def print_dict(d1):
    if d1:
        print('{')
        for item in d1.items():
            print(f'\t\'{item[0]}\': {item[1]},')
        print('}')


def print_2d_list(l1):
    print('\n'.join(''.join([str(n) + ' ' for n in row]) for row in l1))


def max_couple(l1, size):

    if len(l1) % 2 == 0 and size * 2 == len(l1):
        return 0
    if len(l1) % 2 == 1 and size * 2 == len(l1) + 1:
        return l1[size - 1]

    maxi = l1[len(l1)-size]+l1[size-1]
    return max(max_couple(l1,size-1),maxi)





def q1():
    print('\nquestion 1')
    l1 = [6 ,5 ,2 ,6 ,18 ,1 ,3 ,8 ,2]
    print(f'Max couple in {l1} is {max_couple(l1, len(l1))}')


def is_valid_email(email):

    if "@" and "." not in email:
        return False, "1"
    if len(email)<8 or len(email)>30:
        return False,"2"
    if not email[:1].isalpha():
        return False,"3"

    name =email[:email.index("@")]
    has_upper = any(char.isupper() for char in name)
    has_lower = any(char.islower() for char in name)
    if not has_lower or has_upper :
        return False
    if not email[-2:].isalpha():
        return False,"5"
    return True





def q2():
    print('\nQuestion 2')
    emails = [
        "john@example.com",
        "JSmith@example.org",
        "alice.doe@example.net",
        "Bob@example",
        "Jane@invalid.1q",
        "Mike@mydomain.com",
    ]
    print("Valid email addresses:")
    for email in emails:
        if is_valid_email(email):
            print(email)


def find_sequence_numbers(l1, sq_size):
    l2 = []
    rows = len(l1)
    cols = len(l1[0])
    for i in range(rows):
        for j in range(cols):
            num = l1[i][j]
            counter = 1
            while counter < sq_size and j <= cols - sq_size and l1[i][j + counter] == num:
                counter += 1
            if counter == sq_size:
                l2.append([num, i, j])
            counter = 1
            while counter < sq_size and i <= rows - sq_size and l1[i + counter][j] == num:
                counter += 1
            if counter == sq_size:
                l2.append([num, i, j])

    return l2


def q3():
    print('\nquestion 3')
    l1 = [
        [1, 2, 3, 4, 1],
        [0, 2, 2, 2, 1],
        [1, 2, 9, 0, 1],
        [1, 0, 2, 4, 1],
        [4, 2, 1, 1, 1]
    ]
    print_2d_list(l1)
    sq_size = 2
    l2 = find_sequence_numbers(l1, sq_size)
    print(f'Sequence numbers for size {sq_size}')
    print(l2)
    sq_size = 3
    l2 = find_sequence_numbers(l1, sq_size)
    print(f'Sequence numbers for size {sq_size}')
    print(l2)
    sq_size = 4
    l2 = find_sequence_numbers(l1, sq_size)
    print(f'Sequence numbers for size {sq_size}')
    print(l2)


def create_dict1(songs):
    dict1=dict()
    for song in songs.values():
        for writer in song["writers"]:
            if writer not in dict1:
                dict1[writer] = [0,0]
            dict1[writer][0] +=1
            if writer in song["performer"]:
                dict1[writer][1] +=1
        for performers in song["performer"]:
            if performers not in dict1:
                dict1[performers] = [0,0]
                dict1[performers][1] +=1
    return dict1



def max_writer_and_performer(d1):
    l2=[0,0,0,0]
    for writer,values in d1.items():
        if l2[1]<values[0]:
            l2[1]=values[0]
            l2[0]=writer
        if l2[3]<values[1]:
            l2[3]=values[1]
            l2[2]=writer

    return l2




def q4():
    print('\nQuestion 4')
    songs = {
        "Rocket Man": {
            "writers": ["Elton John", "Bernie Taupin"],
            "performer": ["Elton John"]
        },
        "Someone Like You": {
            "writers": ["Adele"],
            "performer": ["Adele"]
        },
        "Hallelujah": {
            "writers": ["Leonard Cohen"],
            "performer": ["Leonard Cohen"]
        },
        "Imagine": {
            "writers": ["John Lennon"],
            "performer": ["John Lennon"]
        },
        "Your Song": {
            "writers": ["Elton John", "Bernie Taupin"],
            "performer": ["Celine Dion"]
        },
        "Happy": {
            "writers": ["Pharrell Williams"],
            "performer": ["Pharrell Williams"]
        },
        "Rolling in the Deep": {
            "writers": ["Adele"],
            "performer": ["Adele"]
        },
        "Bohemian Rhapsody": {
            "writers": ["Freddie Mercury"],
            "performer": ["Freddie Mercury"]
        },
        "Despacito": {
            "writers": ["Luis Fonsi", "Erika Ender", "Daddy Yankee"],
            "performer": ["Luis Fonsi"]
        },
        "Hello": {
            "writers": ["Adele"],
            "performer": ["Adele"]
        },
        "Thinking Out Loud": {
            "writers": ["Ed Sheeran"],
            "performer": ["Ed Sheeran"]
        },
    }
    print('q4a')
    d1 = create_dict1(songs)
    print_dict(d1)
    print('q4b')
    l1 = max_writer_and_performer(d1)
    print(l1)
    # print(f'max writer {l1[0]} with {l1[1]} songs')
    # print(f'max performer {l1[2]} with {l1[3]} songs')


def main():
    q1()
    q2()
    q3()
    q4()


if __name__ == '__main__':
    main()
