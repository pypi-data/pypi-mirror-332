import random
import sys
import os
import requests
import json
import re
from importlib.resources import files
from SeerGPT.card_meanings import card_meanings

debug_flag = True if os.getenv("DEBUG") == "1" else False

def resource_path(relative_path):
    return files("SeerGPT.assets").joinpath(relative_path)

def get_config():
    try:
        with open(resource_path("config.json"), "r") as f:
            config = json.load(f)
        required_keys = ["provider", "api_key", "non_reasoning_model", "reasoning_model"]
        if not all(key in config and config[key] for key in required_keys):
            raise ValueError("Missing required config keys")
        return config
    except Exception as e:
        print("Error reading config.json:", e)
        return None

def get_api_key():
    config = get_config()
    if config:
        return config["api_key"]
    return None

def extract_after_last_think(text: str) -> str:
    tag = "</think>"
    last_index = text.rfind(tag)
    if last_index != -1:
        return text[last_index + len(tag):]
    else:
        return text

def clean_text(text: str) -> str:
    text = extract_after_last_think(text)
    # add possible future sanitizations here
    return text

def api_call(query, reasoning=False, system=None):
    config = get_config()
    if config is None:
        raise Exception("Configuration not set up. Please run the setup.")

    provider = config.get("provider", "OpenRouter")
    if provider == "OpenAI":
        url = "https://api.openai.com/v1/chat/completions"
    elif provider == "Anthropic":
        url = "https://api.anthropic.com/v1/complete"
    else:  # Default to OpenRouter
        url = "https://openrouter.ai/api/v1/chat/completions"
    
    model = config["reasoning_model"] if reasoning else config["non_reasoning_model"]
    
    messages = [{
        "role": "user",
        "content": query,
    }]
    if system:
        messages = [{"role": "system", "content": system}] + messages

    response = requests.post(
        url=url,
        headers={
            "Authorization": f"Bearer {get_api_key()}",
        },
        data=json.dumps({
            "model": model,
            "messages": messages
        })
    )
    if debug_flag:
        print("Response: ", response.json())
    response_str = response.json()['choices'][0]['message']['content']
    cleaned = clean_text(response_str)
    if debug_flag:
        print("Cleaned Response: ", cleaned)
    return cleaned

def meaning_of_card(filename):
    s = os.path.basename(filename)
    suits = ["Cups", "Swords", "Wands", "Pentacles"]
    
    if s and s[0].isdigit():
        try:
            start_idx = s.index("-") + 1
            end_idx = s.index(".")
            part = s[start_idx:end_idx]
        except ValueError:
            return "Invalid format"
        
        reversed_flag = False
        if "_REVERSED" in part:
            part = part.replace("_REVERSED", "")
            reversed_flag = True

        spaced = re.sub(r'(?<!^)(?=[A-Z])', ' ', part)
        if reversed_flag:
            spaced += " Reversed"
        return spaced

    else:
        found_suit = None
        for suit in suits:
            if suit in s:
                found_suit = suit
                break
        if not found_suit:
            return "Invalid suit"

        pattern = re.compile(rf"({found_suit})(\d{{2}})(?:_REVERSED)?\.png")
        match = pattern.search(s)
        if not match:
            return "Invalid format"
        
        card_number = match.group(2)
        reversed_suffix = " Reversed" if "_REVERSED" in s else ""

        card_mapping = {
            "01": "Ace",
            "02": "Two",
            "03": "Three",
            "04": "Four",
            "05": "Five",
            "06": "Six",
            "07": "Seven",
            "08": "Eight",
            "09": "Nine",
            "10": "Ten",
            "11": "Page",
            "12": "Knight",
            "13": "Queen",
            "14": "King"
        }
        
        card_name = card_mapping.get(card_number)
        if not card_name:
            return "Invalid card number"
        
        if debug_flag:
            print(f"{s}: {card_name} Of {found_suit}{reversed_suffix}")
        meaning = card_meanings[f"{card_name} Of {found_suit}{reversed_suffix}"]
        if debug_flag:
            print("Meaning: ", meaning)
        return meaning

def divine(query, spread_name, card_names):
    details_map = {
        "Employment": ["Outlook", "Strengths", "Weaknesses", "What to Seek", "What to Avoid", "Outcome"], 
        "Self Healing": ["What is blocking the user", "The past (how this block has affected relationships)", "The present", "Lessons learned (a warning)", "Positive influences", "Advice (what to strive for)"],
        "Straight shooter": ["Current Position", "Focus (What needs work)", "Hidden Influence (help or hinder)", "Advice", "Outcome"],
        "Lucky Horseshoe": ["You (the user)", "Past Finances", "Present Events", "Immediate Future", "Influences (positive or negative)", "Obstacles", "Outcome"],
        "Money Spread": ["Current Position", "Unseen Obstacles", "Positive Consequences", "Negative Consequences", "Success or Failure"],
        "Obstacle Spread": ["The Concern or Obstacle", "Direct Influences (person, situation or user's feelings)", "Hidden Influences (what the user does not know)", "Help (what may overcome the situation)", "Advice"],
        "The Blind Spot": ["What Everyone Knows", "What No One Knows", "What the User Knows", "What They Know"],
        "The Goodbye Spread": ["What the user needs", "What the user gets", "What they (the subject) need", "What they (the subject) get", "Outcome"],
        "True Love": ["The user", "Partner", "What brings them together", "What keeps them together", "What needs work", "Outcome"],
        "Love General": ["The User", "Strengths", "Weaknesses", "What to Seek", "What to Avoid", "Outcome"],
        "Overall Health Read": ["The Past", "The Present", "Improvement (what may help you get better)", "Guidance", "Outcome"],
    }
    details = details_map[spread_name]
    system = "Given the following cards with their positional significance in a Tarot reading, answer the user's query."
    for i, card in enumerate(card_names):
        system += f"\n{i}. {card} - Positional Significance in the Spread: {details[i]}.\nMeaning of the card:\n" + meaning_of_card(card)
    response = api_call(query, reasoning=True, system=system)
    return response

def further_query(previous_response, query):
    system = "Given this transcript of the current divination session, answer the user's query:\n"+previous_response
    response = api_call(query, reasoning=False, system=system)
    return response

image_files = []

def load_images():
    dir_path = files("SeerGPT.assets")
    for filepath in dir_path.iterdir():
        filename = os.path.basename(filepath)
        if filename.endswith(".png") and "backcover.png" not in filename:
            image_files.append(filepath)

def select_random_images(image_files, n):
    if n > len(image_files):
        raise ValueError(f"Not enough images. Requested {n}, but only {len(image_files)} available.")
    selected_images = random.sample(image_files, n)
    return selected_images

def find_last_spread(input_string, spread_string_map):
    return next((spread_string_map[key] for key in reversed(spread_string_map) if key in input_string), "The Blind Spot")

def get_spread(query):
    response = api_call(query,
                        reasoning=False,
                        system="""
The user will ask you a query, and you are tasked with finding the most suitable spread. Mention the code of the spread (ex. EMPLOY for Employment) without fail. Keep your response as short as possible.
Here are the available spreads:
Employment (EMPLOY): For employment related queries,
Self Healing (SELF): Mental or emotional,
Straight shooter (SHOOT): Career questions,
Lucky Horseshoe (LUCKY): General financial questions,
Money Spread (MONEY): For financial decisions,
Obstacle Spread (OBSTACLE): Insight to an event,
The Blind Spot (BLIND): General question with no query,
The Goodbye Spread (GOODBYE): Direction of an unestablished or new relationship,
True Love (TRUE): Establish relationships,
Love General (LOVE): General romance related questions,
Overall Health Read (HEALTH): With or without query
""")
    spread_string_map = {
        "EMPLOY": "Employment",
        "SELF": "Self Healing",
        "SHOOT": "Straight shooter",
        "LUCKY": "Lucky Horseshoe",
        "MONEY": "Money Spread",
        "OBSTACLE": "Obstacle Spread",
        "BLIND": "The Blind Spot",
        "GOODBYE": "The Goodbye Spread",
        "TRUE": "True Love",
        "LOVE": "Love General",
        "HEALTH": "Overall Health Read",
    }
    spread_name = find_last_spread(response, spread_string_map)
    spread_name = "The Blind Spot" if not spread_name in list(spread_string_map.values()) else spread_name
    # number of cards for each spread
    spread_map = {
        "Employment": 6,
        "Self Healing": 6,
        "Straight shooter": 5,
        "Lucky Horseshoe": 7,
        "Money Spread": 5,
        "Obstacle Spread": 5,
        "The Blind Spot": 4,
        "The Goodbye Spread": 5,
        "True Love": 6,
        "Love General": 6,
        "Overall Health Read": 5,
    }
    card_names = select_random_images(image_files, spread_map[spread_name])
    return (spread_name, card_names)
