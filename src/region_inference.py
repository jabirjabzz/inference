from nltk.tokenize import word_tokenize

# Dictionary mapping regions and districts to keywords
# Add regions
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

def infer_region(text, region_keywords):
    tokens = word_tokenize(text.lower())  # Normalize text
    for region, districts in region_keywords.items():
        for district, keywords in districts.items():
            for token in tokens:
                if token in keywords:
                    return {"region": region, "district": district}  # Return matched region and district
    return {"region": "unknown", "district": "unknown"}  # Default if no match is found

# Example usage
text = "I recently visited Munnar for a holiday."
detected_region = infer_region(text, region_keywords)
print(detected_region)  # Output: {'region': 'southern_kerala', 'district': 'idukki'}
