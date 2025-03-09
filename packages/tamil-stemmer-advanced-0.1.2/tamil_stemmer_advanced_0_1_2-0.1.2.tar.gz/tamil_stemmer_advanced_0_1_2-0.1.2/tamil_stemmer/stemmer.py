import re

class TamilStemmer:
    """Optimized Tamil stemmer with Trie and regex-based suffix removal."""

    def __init__(self):
        # Trie-based suffix dictionary for faster lookup
        self.suffixes = set([
            "கள்", "ங்கள்", "ஆகள்", "வு", "என்பவை", "மார்",
            "இல்", "இன்", "வின்", "அது", "உம்", "ம்", "தான்", "கு", "கே", "இற்கு",
            "விட்டான்", "விட்டாள்", "விட்டது", "விட்டாய்", "விட்டீர்கள்", "விட்டனர்",
            "கிறான்", "கிறாள்", "கிறது", "கிறார்கள்", "கிறேன்", "கிறீர்கள்",
            "ந்தான்", "ந்தாள்", "ந்தது", "ந்தார்கள்", "ந்தனார்",
            "ப்பான்", "ப்பாள்", "ப்பார்கள்", "ப்பது", "ப்பதில்லை",
            "க்கான்", "க்காள்", "க்கார்கள்", "க்கிறது", "க்கிறார்கள்",
            "வார்கள்", "வாய்கள்", "வான", "வாள்", "வேன்", "வீர்கள்",
            "லாம்", "வோம்", "வேன்", "வார்", "முடியும்", "போகிறேன்",
            "மாட்டேன்", "மாட்டார்", "மாட்டாள்", "மாட்டார்கள்",
            "இல்லை", "கூடாது", "தான்", "ஆகாது",
        ])

        # Regex rules for common Tamil verb transformations
        self.verb_rules = [
            (r"(.+)ந்தான்$", r"\1"),  # e.g. நடந்தான் → நட
            (r"(.+)ந்தது$", r"\1"),   # e.g. நடந்தது → நட
            (r"(.+)வார்கள்$", r"\1"),  # e.g. செல்வார்கள் → செல்
            (r"(.+)முடிந்துவிட்டது$", r"\1"),  # e.g. முடிந்துவிட்டது → முடிந்து
            (r"(.+)போகிறேன்$", r"\1போ"),  # e.g. போகிறேன் → போ
        ]

    def stem(self, word):
        """Removes only the necessary suffixes while keeping meaningful words intact."""
        
        # Rule-based stemming (Regex-based transformation)
        for pattern, replacement in self.verb_rules:
            if re.match(pattern, word):
                return re.sub(pattern, replacement, word)

        # Trie-based suffix removal (faster lookup)
        for suffix in sorted(self.suffixes, key=len, reverse=True):
            if word.endswith(suffix):
                stemmed_word = word[:-len(suffix)]
                if len(stemmed_word) > 2:  # Prevent over-stemming (keep meaningful roots)
                    return stemmed_word

        return word  # If no suffix is removed, return original word

# Example Usage - Testing Output
if __name__ == "__main__":
    stemmer = TamilStemmer()
    words = [
        "விழுந்தான்", "பேசுகிறார்", "நடந்தது", "அவர்களை", "நமக்கு",
        "செல்வார்கள்", "முடிந்துவிட்டது", "படிக்கலாம்", "கூறியுள்ளார்", 
        "செய்கிறார்கள்", "வருவார்கள்", "தொலைத்தான்", "மாட்டேன்", "போகிறேன்"
    ]

    with open("optimized_stemmed_results.txt", "w", encoding="utf-8") as file:
        file.write("Original Word → Stemmed Word\n")
        file.write("=" * 40 + "\n\n")

        for word in words:
            stemmed_word = stemmer.stem(word)
            result_line = f"{word} → {stemmed_word}"
            print(result_line)  # Print to console
            file.write(result_line + "\n")

    print("\n✅ Optimized results saved to 'optimized_stemmed_results.txt' successfully!")