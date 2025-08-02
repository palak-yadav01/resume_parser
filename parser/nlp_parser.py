import spacy

nlp = spacy.load("en_core_web_sm")

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text, skills_list):
    text = text.lower()
    found = [skill for skill in skills_list if skill.lower() in text]
    return list(set(found))

def extract_education(text):
    education_keywords = ["B.Tech", "B.E", "M.Tech", "Bachelor", "Master", "PhD"]
    return [line for line in text.split('\n') if any(kw in line for kw in education_keywords)]
