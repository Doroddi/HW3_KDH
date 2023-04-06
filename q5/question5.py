def reverse_words(str):
    strlst = str.split()
    strlst.reverse()
    return ' '.join(strlst)

def main():
    str1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    print("Original String : {0}\n".format(str1))
    print("Reverse String : {0}\n".format(reverse_words(str1)))
    
    str2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    print("Original String : {0}\n".format(str2))
    print("Reverse String : {0}\n".format(reverse_words(str2)))

if __name__ == '__main__':
    main()
