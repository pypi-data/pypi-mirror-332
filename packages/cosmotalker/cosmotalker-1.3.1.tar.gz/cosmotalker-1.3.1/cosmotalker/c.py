import os
import json

def c(query):
    # Dynamically find the ss.txt file in the same directory as this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    train_file = os.path.join(base_dir, "ss.txt")

    query = query.lower()
    matches = []
    
    common_words = {"the", "a", "an", "of", "in", "on", "for", "to", "with"}
    filtered_query = " ".join([word for word in query.split() if word not in common_words])

    if not os.path.exists(train_file):
        return json.dumps({"error": f"Data file not found at {train_file}. Ensure 'ss.txt' is available."})

    with open(train_file, "r", encoding="utf-8") as f:
        content = f.readlines()
        
        for line in content:
            line_lower = line.lower()
            if any(word in line_lower for word in filtered_query.split()):
                matches.append(line.strip())    
    
    if not matches:
        return json.dumps({"error": "No relevant information found. Try asking about a planet or space object."})
    
    # Extract the title from the first word (assuming it's the celestial body name)
    first_match = matches[0]
    title = first_match.split()[0].capitalize()  # Extract first word and capitalize
    description = f"Information about {title}."
    
    return json.dumps({"title": title, "description": description, "details": [first_match]}, indent=4)
