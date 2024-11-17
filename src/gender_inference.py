import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

def infer_gender(text):
    # Tokenize and POS tagging
    tokens = word_tokenize(text.lower())  # Lowercase for normalization
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    tagged_tokens = pos_tag(lemmatized_tokens)

    # Neutral keywords for gender detection
    gender_keywords = {
        "male": ["he", "him", "man", "boy", "gentleman", "sir"],
        "female": ["she", "her", "woman", "girl", "lady", "madam"],
        "neutral": ["they", "person", "individual", "child", "friend"]
    }

    # Gender inference logic
    for token, tag in tagged_tokens:
        for gender, keywords in gender_keywords.items():
            if token in keywords:
                return gender

    return "unknown"  # Default for undetected gender

# Example usage
if __name__ == "__main__":
    text = "They are a skilled artist."
    gender = infer_gender(text)
    print(f"Detected Gender: {gender}")
