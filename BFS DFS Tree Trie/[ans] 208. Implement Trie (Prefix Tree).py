

# solution (accepted)
class Trie:

	def __init__(self):
			"""
			Initialize your data structure here.
			"""
			self.trie = {}
			

	def insert(self, word: str) -> None:
			"""
			Inserts a word into the trie.
			"""
			t = self.trie
			for char in word:
					if char not in t:
							t[char] = {}
					t = t[char]
			t['#'] = '#'
			

	def search(self, word: str) -> bool:
			"""
			Returns if the word is in the trie.
			"""
			t = self.trie
			for char in word:
					if char not in t:
							return False
					t = t[char]
			if '#' not in t:
					return False
			return True
			

	def startsWith(self, prefix: str) -> bool:
			"""
			Returns if there is any word in the trie that starts with the given prefix.
			"""
			t = self.trie
			for char in prefix:
					if char not in t:
							return False
					t = t[char]
			return True
