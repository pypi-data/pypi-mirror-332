import random
import datetime
from .exceptions import LoveError, DateError
from .utils import generate_date_ideas, send_message, remind_anniversary

class Shrijuu:
    def __init__(self, name="Shrijuu"):
        self.name = name
        self.memories = []
        self.mood = "happy"  # default mood
        self.love_level = 75  # scale of 0-100
        self.favorites = {
            "food": "pasta",
            "color": "purple",
            "movie": "The Notebook",
            "song": "Your favorite song",
            "flower": "roses"
        }
        self.birthday = None
        self.anniversary = None
        self.personality = {
            "extroversion": 60,
            "sensitivity": 70,
            "creativity": 85,
            "patience": 65
        }
        self.pet_names = ["sweetie", "honey", "darling", "love"]
        self.last_date = None
        self.inside_jokes = []
        self.wish_list = []
        self.relationship_milestones = {}
        
    def express_love(self, message=None):
        """Express love with optional custom message"""
        if message and not isinstance(message, str):
            raise LoveError("Love message must be a string!")
            
        if not message:
            responses = [
                f"I love you, {self.name}!",
                f"You mean the world to me, {self.name}!",
                f"Every day with you is a blessing, {self.name}!",
                f"You make my heart skip a beat, {self.name}!",
                f"I'm so lucky to have you in my life, {self.name}!"
            ]
            return random.choice(responses)
        
        self.love_level = min(100, self.love_level + 5)
        return f"Message delivered: {message}"
        
    def plan_date(self, location=None, time=None):
        """Plan a date with optional location and time"""
        if location is None or time is None:
            date_ideas = generate_date_ideas()
            selected_idea = random.choice(date_ideas)
            suggested_time = f"{random.randint(5, 9)}:00 PM"
            self.last_date = datetime.datetime.now()
            return f"How about {selected_idea} at {suggested_time}?"
        
        self.last_date = datetime.datetime.now()
        self.love_level = min(100, self.love_level + 10)
        return f"Let's plan a date at {location} at {time}."
        
    def share_memories(self, new_memory=None):
        """Share existing memories or add a new one"""
        if new_memory:
            self.memories.append(new_memory)
            self.love_level = min(100, self.love_level + 5)
            return f"Memory added: {new_memory}"
            
        if not self.memories:
            return "We have no memories together yet."
        return "Our memories: " + ", ".join(self.memories)
        
    def add_memory(self, memory):
        """Add a new memory"""
        if not isinstance(memory, str):
            raise TypeError("Memory must be a string")
        
        self.memories.append(memory)
        return f"Memory added: {memory}"
        
    def set_anniversary(self, date_string):
        """Set your anniversary date"""
        try:
            self.anniversary = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
            return f"Anniversary set to {self.anniversary.strftime('%B %d, %Y')}"
        except ValueError:
            raise DateError("Invalid date format. Please use YYYY-MM-DD")
            
    def set_birthday(self, date_string):
        """Set birthday date"""
        try:
            self.birthday = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
            return f"Birthday set to {self.birthday.strftime('%B %d, %Y')}"
        except ValueError:
            raise DateError("Invalid date format. Please use YYYY-MM-DD")
            
    def get_mood(self):
        """Get current mood"""
        moods = ["happy", "excited", "content", "sad", "annoyed", "romantic", "playful"]
        weights = [0.3, 0.2, 0.2, 0.1, 0.1, 0.05, 0.05]
        
        # Influence mood based on love level
        if self.love_level > 90:
            weights = [0.4, 0.3, 0.2, 0.02, 0.02, 0.05, 0.01]
        elif self.love_level < 40:
            weights = [0.1, 0.05, 0.2, 0.3, 0.2, 0.05, 0.1]
            
        self.mood = random.choices(moods, weights=weights)[0]
        return f"Shrijuu is feeling {self.mood} right now."
        
    def send_gift(self, gift):
        """Send a gift to Shrijuu"""
        gift_reactions = {
            "flowers": f"I love these! Especially {self.favorites['flower']}!",
            "chocolate": "Mmm, my favorite treat!",
            "jewelry": "It's beautiful! I'll wear it every day!",
            "teddy bear": "Aww, it's so cute! I'll cuddle with it when I miss you.",
            "book": "I can't wait to read this!",
            "clothes": "I love it! You know my style so well!"
        }
        
        if gift.lower() in gift_reactions:
            self.love_level = min(100, self.love_level + 15)
            return gift_reactions[gift.lower()]
        elif gift.lower() == self.favorites["food"].lower():
            self.love_level = min(100, self.love_level + 20)
            return f"You remembered my favorite food! Best. Gift. Ever!"
        else:
            self.love_level = min(100, self.love_level + 10)
            return "Thank you so much for the gift! You're so thoughtful."
            
    def add_favorite(self, category, item):
        """Add or update a favorite item"""
        self.favorites[category.lower()] = item
        return f"I'll remember that my favorite {category} is {item}!"
        
    def recommend_gift(self):
        """Get gift recommendations based on favorites"""
        gift_ideas = [
            f"A bouquet of {self.favorites.get('flower', 'roses')}",
            f"Tickets to see {self.favorites.get('movie', 'a movie')}",
            f"{self.favorites.get('food', 'A special dinner')}",
            f"Something {self.favorites.get('color', 'purple')}"
        ]
        return random.choice(gift_ideas)
        
    def compliment(self, about=None):
        """Get a compliment"""
        if about == "looks":
            compliments = [
                "You look absolutely amazing today!",
                "Your smile brightens my day!",
                "You're the most handsome person I've ever seen.",
                "I can't take my eyes off you!"
            ]
        elif about == "personality":
            compliments = [
                "You have such a kind heart.",
                "Your sense of humor always makes me laugh.",
                "I admire your determination and drive.",
                "You're the most caring person I know."
            ]
        else:
            compliments = [
                "You're my favorite person in the whole world!",
                "I'm so lucky to have you in my life.",
                "You make me a better person.",
                "You're everything I've ever wanted.",
                "Being with you is the highlight of my day."
            ]
        
        return random.choice(compliments)
        
    def create_inside_joke(self, joke):
        """Create a new inside joke"""
        self.inside_jokes.append(joke)
        return "Haha! That's our little secret now. ;)"
        
    def get_inside_joke(self):
        """Recall a random inside joke"""
        if not self.inside_jokes:
            return "We don't have any inside jokes yet!"
        return f"Remember this? {random.choice(self.inside_jokes)} *giggles*"
        
    def add_to_wishlist(self, item):
        """Add an item to wishlist"""
        self.wish_list.append(item)
        return f"I've added {item} to my wishlist! *wink wink*"
        
    def get_wishlist(self):
        """Get current wishlist items"""
        if not self.wish_list:
            return "My wishlist is empty right now!"
        return "My wishlist: " + ", ".join(self.wish_list)
        
    def add_milestone(self, event, date_string):
        """Add a relationship milestone"""
        try:
            date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
            self.relationship_milestones[event] = date
            return f"Added milestone: {event} on {date.strftime('%B %d, %Y')}"
        except ValueError:
            raise DateError("Invalid date format. Please use YYYY-MM-DD")
            
    def get_pet_name(self):
        """Get a random pet name"""
        return random.choice(self.pet_names)
        
    def add_pet_name(self, name):
        """Add a new pet name"""
        self.pet_names.append(name)
        return f"I'll call you {name} sometimes. *blushes*"
        
    def virtual_hug(self):
        """Send a virtual hug"""
        hugs = [
            "(っ◕‿◕)っ",
            "⊂(・﹏・⊂)",
            "⊂(・▽・⊂)",
            "⊂(◉‿◉)つ",
            "༼ つ ◕_◕ ༽つ"
        ]
        return f"{random.choice(hugs)} *hugs you tight*"
        
    def virtual_kiss(self):
        """Send a virtual kiss"""
        kisses = [
            "😘",
            "💋",
            "(づ￣ ³￣)づ",
            "( ˘ ³˘)♥",
            "ʕ•́ᴥ•̀ʔっ♡"
        ]
        return f"{random.choice(kisses)} *kisses you softly*"
        
    def get_relationship_status(self):
        """Get current relationship status"""
        if self.love_level >= 90:
            return "Our relationship is amazing! I've never been happier!"
        elif self.love_level >= 70:
            return "Things are going really well between us!"
        elif self.love_level >= 50:
            return "We're doing okay, but I'd love more quality time together."
        else:
            return "I feel like we need to work on our relationship..."
            
    def suggest_activity(self):
        """Suggest an activity to do together"""
        activities = [
            "watching a movie together",
            "cooking a romantic dinner",
            "going for a walk in the park",
            "having a game night",
            "stargazing",
            "having a picnic",
            "going dancing",
            "taking a weekend trip",
            "trying a new restaurant",
            "visiting a museum"
        ]
        return f"Let's try {random.choice(activities)} soon! It would be so much fun!"
        
    def reminisce(self):
        """Reminisce about a memory"""
        if not self.memories:
            return "We should make some memories together!"
        return f"I was just thinking about when {random.choice(self.memories)}. That was so special."