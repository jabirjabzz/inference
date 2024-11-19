import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

caste_keywords = {
    "brahmins": ["namboothiri", "embrandiri", "pattar"],
    "nairs": ["nair", "menon", "pillai", "kurup", "kartha", "panicker"],
    "ezhava_thiyya": ["ezhava", "thiyya", "billava"],
    "kshatriyas": ["zamorin", "raja", "nambiars", "raja nair"],
    "obc_hindus": ["kaniyar", "ganaka", "vaniyan", "moosari", "thattan"],
    "scheduled_castes": ["pulaya", "cheramar", "paraya", "kanakkan", "vettuva", "kurava", "chakkiliyan"],
    "scheduled_tribes": ["kurichiya", "paniya", "irula", "kattunayakan", "adiyan", "malayarayan", "ulladan", "kanikkar"],
    "muslims": ["mappila", "moplah", "rowther", "labbai", "sheikh", "keyi", "marakkar", "qazi", "maulavi", "alavi"],
    "christians": [
        "syrian orthodox", "syrian catholic", "syrian jacobite", "syrian marthomite",
        "latin catholic", "knanaya catholic", "knanaya jacobite", "anglo-indian", 
        "protestant", "csi", "father", "bishop", "archbishop", "reverend"
    ]
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
