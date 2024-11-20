from nltk.tokenize import word_tokenize

# Dictionary mapping regions and districts to keywords
region_keywords = {
    "northern_kerala": {
        "kasaragod": ["bekal", "chandragiri", "kanhangad"],
        "kannur": ["thalassery", "payyanur", "mattannur"],
        "wayanad": ["kalpetta", "sultan bathery", "mananthavady"],
        "kozhikode": ["calicut", "vadakara", "kappad"],
        "malappuram": ["ponnani", "tirur", "kondotty"]
    },
    "central_kerala": {
        "palakkad": ["ottapalam", "chittur", "malampuzha"],
        "thrissur": ["guruvayur", "kodungallur", "chalakudy"],
        "ernakulam": ["kochi", "aluva", "muvattupuzha"]
    },
    "southern_kerala": {
        "idukki": ["munnar", "thekkady", "vagamon"],
        "kottayam": ["kumarakom", "pala", "changanassery"],
        "alappuzha": ["alappuzha", "cherthala", "kuttanad"],
        "pathanamthitta": ["aranmula", "pandalam", "ranni"],
        "kollam": ["ashtamudi", "paravur", "punalur"],
        "thiruvananthapuram": ["trivandrum", "neyyattinkara", "attingal"]
    }
}

def infer_region_with_workflow(text, region_keywords):
    print(f"Input Text: {text}")

    # Step 1: Normalize text
    normalized_text = text.lower()
    print(f"Normalization: {normalized_text}")

    # Step 2: Tokenize text
    tokens = word_tokenize(normalized_text)
    print(f"Tokenization: {tokens}")

    # Step 3: Keyword Matching
    for region, districts in region_keywords.items():
        for district, keywords in districts.items():
            for token in tokens:
                if token in keywords:
                    print(f"Keyword Matching: '{token}' matches with district '{district}' in region '{region}'.")
                    return {"region": region, "district": district}  # Return matched region and district
    
    print("Keyword Matching: No matches found.")
    return {"region": "unknown", "district": "unknown"}  # Default if no match is found

# Example usage
text = "I visited MUNNAR last summer."
detected_region = infer_region_with_workflow(text, region_keywords)
print(f"Detected Region: {detected_region}")
