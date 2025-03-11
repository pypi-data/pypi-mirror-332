def generate_date_ideas():
    ideas = [
        "Picnic in the park",
        "Movie night at home",
        "Visit a local museum",
        "Cooking dinner together",
        "Hiking on a scenic trail",
        "Attend a concert or live show",
        "Explore a new restaurant",
        "Take a dance class together",
        "Go stargazing",
        "Plan a weekend getaway"
    ]
    return ideas

def send_message(message, recipient="Shrijuu"):
    return f"Message to {recipient}: {message}"

def remind_anniversary(date):
    from datetime import datetime
    today = datetime.now().date()
    anniversary_date = datetime.strptime(date, "%Y-%m-%d").date()
    days_until_anniversary = (anniversary_date - today).days
    if days_until_anniversary < 0:
        return "Your anniversary has already passed."
    elif days_until_anniversary == 0:
        return "Happy Anniversary!"
    else:
        return f"{days_until_anniversary} days until your anniversary!"