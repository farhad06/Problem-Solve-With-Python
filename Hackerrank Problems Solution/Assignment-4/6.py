if __name__ == '__main__':
    string = input()
    print (any(s.isalnum() for s in string))
    print (any(s.isalpha() for s in string))
    print (any(s.isdigit() for s in string))
    print (any(s.islower() for s in string))
    print (any(s.isupper() for s in string))