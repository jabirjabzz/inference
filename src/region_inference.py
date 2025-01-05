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
        "kottayam": ["കോട്ടയം ടൗൺ", "കുമരകം", "ഏറ്റുമാനൂർ", "ചങ്ങനാശ്ശേരി", "പാലാ", "കാഞ്ഞിരപ്പള്ളി", "വൈക്കം", "ഈരാറ്റുപേട്ട", "പൊൻകുന്നം", "കോട്ടയം റെയിൽവേ സ്റ്റേഷൻ", "കുമരകം പക്ഷി സങ്കേതം", "വേമ്പനാട് കായൽ", "മീനച്ചിലാറ്", "കോട്ടയം ബസ് സ്റ്റേഷൻ", "ഏറ്റുമാനൂർ ബസ് സ്റ്റേഷൻ", "ചങ്ങനാശ്ശേരി ബസ് സ്റ്റേഷൻ", "പാലാ ബസ് സ്റ്റേഷൻ", "കാഞ്ഞിരപ്പള്ളി ബസ് സ്റ്റേഷൻ", "വൈക്കം ബസ് സ്റ്റേഷൻ", "ഈരാറ്റുപേട്ട ബസ് സ്റ്റേഷൻ", "പൊൻകുന്നം ബസ് സ്റ്റേഷൻ", "കോട്ടയം ജില്ലാ കോടതി", "കോട്ടയം കളക്ടറേറ്റ്", "കോട്ടയം മുനിസിപ്പൽ സ്റ്റേഡിയം", "സി.എം.എസ്. കോളേജ്", "മഹാത്മാ ഗാന്ധി സർവ്വകലാശാല", "കോട്ടയം മെഡിക്കൽ കോളേജ്", "ഗവൺമെൻ്റ് മെഡിക്കൽ കോളേജ്, കോട്ടയം", "റബ്ബർ ബോർഡ്", "കോട്ടയം തുറമുഖം", "കുമരകം തുറമുഖം", "ഏറ്റുമാനൂർ മഹാദേവ ക്ഷേത്രം", "വൈക്കം മഹാദേവ ക്ഷേത്രം", "ചങ്ങനാശ്ശേരി മഹാദേവ ക്ഷേത്രം", "കോട്ടയം നാഗമ്പടം സ്റ്റേഡിയം", "കുമരകം ലേക്ക് റിസോർട്ട്", "വാഗമൺ", "ഇലവീഴാപൂഞ്ചിറ (ഇല്ലിക്കൽ കല്ല് എന്ന് തെറ്റായി നൽകിയിരിക്കുന്നു)", "വാഗമൺ മേടുകൾ", "തങ്ങൾപ്പാറ", "കോട്ടയം പ്രസ് ക്ലബ്", "കോട്ടയം പബ്ലിക് ലൈബ്രറി", "ഏറ്റുമാനൂർ പബ്ലിക് ലൈബ്രറി", "ചങ്ങനാശ്ശേരി പബ്ലിക് ലൈബ്രറി", "പാലാ പബ്ലിക് ലൈബ്രറി", "കാഞ്ഞിരപ്പള്ളി പബ്ലിക് ലൈബ്രറി", "വൈക്കം പബ്ലിക് ലൈബ്രറി", "ഈരാറ്റുപേട്ട പബ്ലിക് ലൈബ്രറി", "പൊൻകുന്നം പബ്ലിക് ലൈബ്രറി", "കോട്ടയം ക്ലബ്"],
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
