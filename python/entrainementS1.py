non_trie = [4, 42, 13, 26, 27, 16, 32, 37, 43, 17, 49, 6, 25, 5, 38, 48, 35, 40, 7, 31, 10, 18,
41, 21, 19, 28, 30, 12, 33, 36, 47, 24, 29, 2, 0, 9, 15, 11, 14, 3, 23, 20, 8, 44, 39, 34, 46,
45, 22, 1]
trie= []

  


c=0
    

while len(non_trie)!= len(trie):
    for i in range(len(non_trie)):
        if non_trie[i]> c:
            g=non_trie[i]
    r=0
    for j in range(len(non_trie)):

            if non_trie[j]<c:
                c=non_trie[j]
                r=r+1


    trie.append(c)

    for h in range(len(non_trie)-r):
         if non_trie[h] == c :
               non_trie=non_trie[h]
          