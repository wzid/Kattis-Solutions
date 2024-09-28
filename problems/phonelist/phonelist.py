class Trie:
    def __init__(self, setMode = True):
        """
        :param setMode: Whether to act like a set or include duplicates
        """
        self.children = {}
        self.setMode = setMode

    def add(self, word):
        """
        Add a Word to the Trie
        O(wordlen)
        :param word: The word to add
        """
        current_dict = self.children
        for letter in word:
            current_dict = current_dict.setdefault(ord(letter), {})
        if not self.setMode:
            if ord('_') in current_dict:
                current_dict[ord('_')] += 1
            else:
                current_dict[ord('_')] = 1
        else:
            current_dict[ord('_')] = 1


    def starts_with(self, prefix, rev=False):
        """
        Returns a list of all words beginning with the given prefix
        O(n logn) where n is wordlen
        :param prefix: The prefix string to find matches
        :param rev: True if this is being used as a suffix tree 
        """
        words = list()
        current = self.children
        t = ""
        for char in prefix:
            if ord(char) not in current:
                return list()
            current = current[ord(char)]
            if rev:
                t = char + t
        if rev:
            self.__child_words_for(current, words, t, rev=True)
        else:
            self.__child_words_for(current, words, prefix)
        return words

    def __child_words_for(self, curr, words, stem, rev=False):
        """Helper function
        O(n logn) where n is wordlen
        :param curr: The current position in the Trie
        :param words: Found words
        :param stem: The prefix + letters in the current word
        :param rev: Whether it is running in suffix mode"""
        if ord('_') in curr:
            if curr[ord('_')] > 1:
                words.extend([stem]*curr[ord('_')])
            else:
                words.append(stem)
        for char in curr:
            if chr(char) != '_':
                if rev:
                    self.__child_words_for(curr[char], words, chr(char) + stem, rev=True)
                else:
                    self.__child_words_for(curr[char], words, stem+chr(char))


t = int(input())

for i in range(t):
    n = int(input())
    trie = Trie()
    l = []
    for j in range(n):
        phone_num = input()
        l.append((len(phone_num), phone_num))
    l.sort(reverse=True)
    works = True
    for x in l:
        length, phone_num = x[0], x[1]
        if trie.starts_with(phone_num):
            works = False
            print('NO')
            break
        trie.add(phone_num)
        
    if works:
        print('YES')
        