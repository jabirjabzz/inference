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
        "idukki": ["ഇടുക്കി ഡാം", "മു​ന്നാർ", "തേക്കടി", "പെരിയാർ നാഷണൽ പാർക്ക്", "ആനമുടി കൊടുമുടി", "മാട്ടുപ്പെട്ടി ഡാം", "എക്കോ പോയിന്റ്", "ടോപ് സ്റ്റേഷൻ", "രാജമല", "മറയൂർ", "കട്ടപ്പന", "അടിമാലി", "നെടുങ്കണ്ടം", "പീരുമേട്", "ഇടുക്കി ടൗൺ", "തൊടുപുഴ", "മൂലമറ്റം", "വാഴത്തോപ്പ്", "കട്ടപ്പന ടൗൺ", "അണക്കര", "ചെട്ടുകുഴി", "ഇടുക്കി ആർച്ച് ഡാം", "ചെറുതോണി ഡാം", "കുളമാവ് ഡാം", "ഇടുക്കി വന്യജീവി സങ്കേതം", "പെരിയാർ വന്യജീവി സങ്കേതം", "മു​ന്നാർ ടീ പ്ലാന്റേഷൻ", "ഏലം തോട്ടങ്ങൾ", "ആനമുടി ചോല നാഷണൽ പാർക്ക്", "പാമ്പാടും ചോല നാഷണൽ പാർക്ക്", "ഇടുക്കി ജില്ലാ കോടതി", "ഇടുക്കി കളക്ടറേറ്റ്", "മു​ന്നാർ മുനിസിപ്പൽ ഓഫീസ്", "തേക്കടി ബോട്ട് ലാൻഡിംഗ്", "പെരിയാർ തടാകം", "മു​ന്നാർ ബസ് സ്റ്റേഷൻ", "തൊടുപുഴ ബസ് സ്റ്റേഷൻ", "കട്ടപ്പന ബസ് സ്റ്റേഷൻ", "ഇടുക്കി റെയിൽവേ സ്റ്റേഷൻ", "കോട്ടയം-ഇടുക്കി റോഡ്", "മു​ന്നാർ-തേക്കടി റോഡ്", "ഇടുക്കി ഡാം പവർ ഹൗസ്", "മൂലമറ്റം പവർ ഹൗസ്", "ഇടുക്കി മെഡിക്കൽ കോളേജ്", "മാർ ബസേലിയോസ് മെഡിക്കൽ കോളേജ്", "ഇടുക്കി എഞ്ചിനീയറിംഗ് കോളേജ്", "മു​ന്നാർ കാറ്ററിംഗ് കോളേജ്", "ഗവൺമെൻ്റ് കോളേജ്, ഇടുക്കി", "സെൻ്റ് തോമസ് കോളേജ്, പാല", "മരിയൻ കോളേജ്, കുറ്റിക്കാനം"],
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
