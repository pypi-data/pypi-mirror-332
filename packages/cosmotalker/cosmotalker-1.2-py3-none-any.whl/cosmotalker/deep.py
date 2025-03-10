import os
import random
import re
import json

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
