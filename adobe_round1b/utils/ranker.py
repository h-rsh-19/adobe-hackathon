import re

def clean(text):
    if isinstance(text, dict):
        # Flatten dictionary to a string
        flat_text = " ".join(str(v) for v in text.values())
        return re.sub(r'[^\w\s]', '', flat_text.lower())
    elif isinstance(text, str):
        return re.sub(r'[^\w\s]', '', text.lower())
    else:
        return ''

def rank_sections_by_persona(sections, persona):
    keywords = set()
    for key in ["persona", "job_to_be_done", "task"]:
        value = persona.get(key, "")
        keywords.update(clean(value).split())

    def relevance(section):
        section_words = set(clean(section["text"]).split())
        return len(section_words & keywords)

    ranked = sorted(sections, key=relevance, reverse=True)
    return ranked[:10]
