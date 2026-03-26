class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        unique_elements = set()
        for char in s:
            unique_elements.add(char)

        for char in t:
            if char in unique_elements:
                continue
            else:
                return False
        return True    

va = ValidAnagram()
va.isAnagram("jar", "jam")             