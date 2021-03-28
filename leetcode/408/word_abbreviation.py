import re

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        substitute = re.sub('([1-9]\d*)', r'.{\1}', abbr)  + '$' # end of string to garanttee it covers the entire string
        # print(re.match(substitute, word).group(0))
        return bool(re.match(substitute, word))
