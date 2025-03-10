import os
import importlib
import importlib.util
import unicodedata
import json
import random
import re
def deep(query, train_file="ss.txt"):
    query = query.lower()
    matches = []
    common_words = {"tell", "about", "me", "what", "is", "the", "a", "an", "of", "in", "on", "and", "for", "to", "with","and"}  # Common English words to filter out
    filtered_query = " ".join([word for word in query.split() if word not in common_words])    
    if not os.path.exists(train_file):
        return json.dumps({"error": "CosmoTalker v1.0 currently focuses on the Solar System. The project is continuously improving, and future updates will expand its capabilities to explore galaxies and beyond!"})    
    with open(train_file, "r", encoding="utf-8") as f:
        content = f.readlines()
        for line in content:
            line_lower = line.lower()
            if all(word in line_lower for word in filtered_query.split()):
                matches.append(line.strip())    
    if not matches:
        return json.dumps({"response": "I'm not sure about that. Could you ask in a different way?"})    
    # Dynamically extract key topics and generate structured response
    keywords = set()
    organized_data = {}
    numerical_data = {}
    special_topics = {}    
    for match in matches:
        words = match.split()
        key_topic = words[0].rstrip(':') if len(words) > 1 else "General"
        keywords.add(key_topic)
        organized_data.setdefault(key_topic, []).append(match)        
        # Extract numerical data specific to planets with moons
        if "moon" in match.lower() or "moons" in match.lower():
            numbers = [int(num) for num in re.findall(r'\b\d+\b', match)]
            if numbers:
                numerical_data[key_topic] = numbers[0]  # Assume first number relates to moon count
        # Store relevant information dynamically
        special_topics[key_topic] = special_topics.get(key_topic, []) + [match]    
    # Handle specific cases dynamically
    for topic in special_topics:
        if topic.lower() in filtered_query:
            response_data = {
                "title": topic.capitalize(),
                "description": f"Information about {topic}.",
                "details": special_topics[topic]
            }
            return json.dumps(response_data, indent=4)    
    # General response formatting
    response_data = {
        "summary": f"Here's what I found about {', '.join(keywords)}:",
        "details": {topic: details[:2] for topic, details in organized_data.items()}  # Limit to 2 details for brevity
    }    
    # Handle numerical queries (e.g., "which planet has more moons?")
    if "moons" in filtered_query and numerical_data:
        max_topic = max(numerical_data, key=numerical_data.get)
        response_data = {
            "title": "Most Moons",
            "description": f"As per my knowledge, {max_topic} has the most moons in our solar system, with approximately {numerical_data[max_topic]} moons."
        }
    
    return json.dumps(response_data, indent=4)
def get(key: str):
    if not key:
        return "Invalid key."

    key = unicodedata.normalize("NFC", key.strip().lower())  # Normalize the key
    first_letter = key[0]
    module_path = f"cosmotalker.data.{first_letter}"

    try:
        module = importlib.import_module(module_path)
        importlib.reload(module)  # Force reload

        if hasattr(module, "data"):
            info = module.data.get(key, None)
            if info:
                return f"{info}\n\nCosmoTalker v1.1 currently covers celestial objects within our solar system, whether natural or synthetic. For more data, check the latest version."
            else:
                return "No information found.\n\nCosmoTalker v1.1 currently covers celestial objects within our solar system, whether natural or synthetic. For more data, check the latest version."

        return "Error: 'data' dictionary not found in module."

    except ModuleNotFoundError:
        return deep(key)
        #return f"No information available for this key. (Missing {module_path})\n\nCosmoTalker v1.1 currently covers celestial objects within our solar system, whether natural or synthetic. For more data, check the latest version."
    except AttributeError:
        return deep(key)
        #return "Data format error in the module.\n\nCosmoTalker v1.1 currently covers celestial objects within our solar system, whether natural or synthetic. For more data, check the latest version."

def get_data():
    # Load data dynamically from 'data' directory
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    all_keys = {}
    
    if os.path.exists(data_dir):
        for filename in os.listdir(data_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]  # Remove .py extension
                file_path = os.path.join(data_dir, filename)
                
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                if hasattr(module, "data") and isinstance(module.data, dict):
                    all_keys[module_name] = list(module.data.keys())
    
    # Print the keys from each module neatly using JSON formatting
    print(json.dumps(all_keys, indent=4))
