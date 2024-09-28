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
        '''
        Returns a list of all words beginning with the given prefix, or
        an empty list if no words begin with that prefix.
        O(n logn) where n is wordlen
        :param prefix: The prefix string to find matches
        :param rev: True if this is being used as a suffix tree and the prefix should be reversed optimally
        '''
        words = list()
        current = self.children
        t = ""
        for char in prefix:
            if ord(char) not in current:
                # Could also just return words since it's empty by default
                return list()
            current = current[ord(char)]
            if rev:
                t = char + t

        # print(prefix, t)

        # Step 2
        if rev:
            self.__child_words_for(current, words, t, rev=True)
        else:
            self.__child_words_for(current, words, prefix)
        return words

    def __child_words_for(self, curr, words, stem, rev=False):
        """
        Helper function
        O(n logn) where n is wordlen
        :param curr: The current position in the Trie
        :param words: Found words
        :param stem: The prefix + letters in the current word
        :param rev: Whether it is running in suffix mode
        """
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


n = int(input())
t = Trie(setMode=False)
for i in range(n):
    x = input()
    t.add(x)
    print(len(t.starts_with(x)) - 1)

    