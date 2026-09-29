def like_fibo(nth):


    if nth == 1:
        return 1
    if nth == 2:
        return 2
    if nth == 3:
        return 3


    if nth % 2 == 0:
        return like_fibo(nth - 1) + like_fibo(nth - 2) + like_fibo(nth - 3)

    else:
        return abs(like_fibo(nth - 1) - like_fibo(nth - 3))

def main():
    print(like_fibo(8))

if __name__=="__main__":
    main()
