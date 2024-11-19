import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Example lexicon of caste-related terms (expand responsibly with context)
caste_keywords = {
    "general": ["brahmin", "kshatriya", "vaishya"],
    "scheduled_castes": ["dalit", "sc", "st"],
    "other_backward_classes": ["obc", "yadav", "kurmi"],
    "tribes": ["tribal", "adivasi"],
}

# Function to infer caste-related terms
def infer_caste(text):
    """
    Infers caste-related mentions in the text. 
    This should only be used for legitimate purposes with an unbiased approach.
    """
    tokens = word_tokenize(text.lower())  # Lowercase for normalization
    tagged_tokens = pos_tag(tokens)
    
    inferred_castes = set()  # Use a set to avoid duplicates
    for token, tag in tagged_tokens:
        for category, keywords in caste_keywords.items():
            if token in keywords:
                inferred_castes.add(category)  # Add category instead of keyword
    
    return list(inferred_castes) if inferred_castes else ["unknown"]

# Example usage
text = "He belongs to the Yadav community, which is categorized as OBC."
inferred_castes = infer_caste(text)
print(inferred_castes)  # Output: ['other_backward_classes']
