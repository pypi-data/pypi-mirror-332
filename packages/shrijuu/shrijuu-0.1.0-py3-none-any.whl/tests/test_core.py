import unittest
import datetime
from unittest.mock import patch
import sys
import os

# Add parent directory to path to import module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shrijuu.core import Shrijuu
from shrijuu.exceptions import LoveError, DateError

class TestShrijuu(unittest.TestCase):
    def setUp(self):
        """Set up a Shrijuu instance before each test"""
        self.shrijuu = Shrijuu(name="Test")
        
    def test_initialization(self):
        """Test that Shrijuu initializes with correct default values"""
        self.assertEqual(self.shrijuu.name, "Test")
        self.assertEqual(self.shrijuu.mood, "happy")
        self.assertEqual(self.shrijuu.love_level, 75)
        self.assertEqual(self.shrijuu.favorites["food"], "pasta")
        self.assertEqual(len(self.shrijuu.pet_names), 4)
        
    def test_express_love_default(self):
        """Test that express love returns a response without a message"""
        response = self.shrijuu.express_love()
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        
    def test_express_love_custom(self):
        """Test that express love works with custom message"""
        message = "I love you!"
        response = self.shrijuu.express_love(message)
        self.assertIn(message, response)
        self.assertEqual(self.shrijuu.love_level, 80)  # Should increase by 5
        
    def test_express_love_invalid(self):
        """Test that express love raises error with invalid message"""
        with self.assertRaises(LoveError):
            self.shrijuu.express_love(123)
            
    @patch('shrijuu.core.generate_date_ideas')  # Fix: Changed from 'shrijuu.utils.generate_date_ideas'
    def test_plan_date_no_params(self, mock_generate):
        """Test planning a date with no parameters"""
        mock_generate.return_value = ["dinner", "movie", "picnic"]
        response = self.shrijuu.plan_date()
        self.assertTrue(any(idea in response for idea in ["dinner", "movie", "picnic"]))
        self.assertIsNotNone(self.shrijuu.last_date)
        
    def test_plan_date_with_params(self):
        """Test planning a date with specified parameters"""
        response = self.shrijuu.plan_date("Restaurant", "7:00 PM")
        self.assertIn("Restaurant", response)
        self.assertIn("7:00 PM", response)
        self.assertEqual(self.shrijuu.love_level, 85)  # Should increase by 10
        
    def test_add_memory(self):
        """Test adding a memory"""
        memory = "Our first date"
        response = self.shrijuu.add_memory(memory)
        self.assertIn(memory, response)
        self.assertIn(memory, self.shrijuu.memories)
        
    def test_add_memory_invalid(self):
        """Test adding an invalid memory"""
        with self.assertRaises(TypeError):
            self.shrijuu.add_memory(123)
            
    def test_share_memories_empty(self):
        """Test sharing memories when none exist"""
        response = self.shrijuu.share_memories()
        self.assertEqual(response, "We have no memories together yet.")
        
    def test_share_memories_with_memories(self):
        """Test sharing memories when some exist"""
        self.shrijuu.memories = ["First date", "Anniversary"]
        response = self.shrijuu.share_memories()
        self.assertIn("First date", response)
        self.assertIn("Anniversary", response)
        
    def test_set_anniversary_valid(self):
        """Test setting anniversary with valid date"""
        response = self.shrijuu.set_anniversary("2023-05-15")
        self.assertEqual(self.shrijuu.anniversary, datetime.date(2023, 5, 15))
        self.assertIn("May 15, 2023", response)
        
    def test_set_anniversary_invalid(self):
        """Test setting anniversary with invalid date"""
        with self.assertRaises(DateError):
            self.shrijuu.set_anniversary("invalid date")
            
    def test_set_birthday_valid(self):
        """Test setting birthday with valid date"""
        response = self.shrijuu.set_birthday("1998-07-22")
        self.assertEqual(self.shrijuu.birthday, datetime.date(1998, 7, 22))
        self.assertIn("July 22, 1998", response)
        
    def test_set_birthday_invalid(self):
        """Test setting birthday with invalid date"""
        with self.assertRaises(DateError):
            self.shrijuu.set_birthday("invalid date")
            
    def test_get_mood(self):
        """Test getting mood"""
        self.shrijuu.love_level = 95  # Test high love level
        response = self.shrijuu.get_mood()
        self.assertIn(self.shrijuu.mood, response)
        
    def test_send_gift_favorite(self):
        """Test sending a favorite gift"""
        self.shrijuu.favorites["food"] = "chocolate cake"
        response = self.shrijuu.send_gift("chocolate cake")
        self.assertEqual(self.shrijuu.love_level, 95)  # Should increase by 20
        self.assertIn("favorite food", response)
        
    def test_send_gift_common(self):
        """Test sending a common gift"""
        response = self.shrijuu.send_gift("flowers")
        self.assertEqual(self.shrijuu.love_level, 90)  # Should increase by 15
        
    def test_send_gift_generic(self):
        """Test sending a generic gift"""
        response = self.shrijuu.send_gift("custom gift")
        self.assertEqual(self.shrijuu.love_level, 85)  # Should increase by 10
        
    def test_add_favorite(self):
        """Test adding a favorite"""
        response = self.shrijuu.add_favorite("drink", "lemonade")
        self.assertEqual(self.shrijuu.favorites["drink"], "lemonade")
        self.assertIn("lemonade", response)
        
    def test_recommend_gift(self):
        """Test gift recommendation"""
        response = self.shrijuu.recommend_gift()
        self.assertIsInstance(response, str)
        self.assertTrue(any(fav in response for fav in self.shrijuu.favorites.values()))
        
    def test_compliment_looks(self):
        """Test compliments about looks"""
        response = self.shrijuu.compliment("looks")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        
    def test_compliment_personality(self):
        """Test compliments about personality"""
        response = self.shrijuu.compliment("personality")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        
    def test_compliment_general(self):
        """Test general compliments"""
        response = self.shrijuu.compliment()
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        
    def test_inside_jokes(self):
        """Test inside jokes functionality"""
        joke = "That time at the restaurant"
        self.shrijuu.create_inside_joke(joke)
        self.assertIn(joke, self.shrijuu.inside_jokes)
        
        response = self.shrijuu.get_inside_joke()
        self.assertIn(joke, response)
        
    def test_inside_jokes_empty(self):
        """Test getting inside jokes when none exist"""
        self.shrijuu.inside_jokes = []
        response = self.shrijuu.get_inside_joke()
        self.assertEqual(response, "We don't have any inside jokes yet!")
        
    def test_wishlist(self):
        """Test wishlist functionality"""
        item = "New book"
        self.shrijuu.add_to_wishlist(item)
        self.assertIn(item, self.shrijuu.wish_list)
        
        response = self.shrijuu.get_wishlist()
        self.assertIn(item, response)
        
    def test_wishlist_empty(self):
        """Test getting wishlist when empty"""
        self.shrijuu.wish_list = []
        response = self.shrijuu.get_wishlist()
        self.assertEqual(response, "My wishlist is empty right now!")
        
    def test_add_milestone(self):
        """Test adding a relationship milestone"""
        response = self.shrijuu.add_milestone("First kiss", "2023-01-15")
        self.assertIn("First kiss", self.shrijuu.relationship_milestones)
        self.assertEqual(self.shrijuu.relationship_milestones["First kiss"], 
                         datetime.date(2023, 1, 15))
        
    def test_add_milestone_invalid(self):
        """Test adding an invalid milestone date"""
        with self.assertRaises(DateError):
            self.shrijuu.add_milestone("First kiss", "invalid date")
            
    def test_pet_name(self):
        """Test pet name functionality"""
        response = self.shrijuu.get_pet_name()
        self.assertIn(response, self.shrijuu.pet_names)
        
        new_name = "cupcake"
        self.shrijuu.add_pet_name(new_name)
        self.assertIn(new_name, self.shrijuu.pet_names)
        
    def test_virtual_affection(self):
        """Test virtual affection methods"""
        hug = self.shrijuu.virtual_hug()
        self.assertIsInstance(hug, str)
        self.assertIn("hug", hug.lower())
        
        kiss = self.shrijuu.virtual_kiss()
        self.assertIsInstance(kiss, str)
        self.assertIn("kiss", kiss.lower())
        
    def test_relationship_status(self):
        """Test relationship status at different love levels"""
        self.shrijuu.love_level = 95
        high_status = self.shrijuu.get_relationship_status()
        self.assertIn("amazing", high_status.lower())
        
        self.shrijuu.love_level = 75
        medium_status = self.shrijuu.get_relationship_status()
        self.assertIn("well", medium_status.lower())
        
        self.shrijuu.love_level = 55
        low_medium_status = self.shrijuu.get_relationship_status()
        self.assertIn("okay", low_medium_status.lower())
        
        self.shrijuu.love_level = 35
        low_status = self.shrijuu.get_relationship_status()
        self.assertIn("need", low_status.lower())
        
    def test_suggest_activity(self):
        """Test activity suggestion"""
        response = self.shrijuu.suggest_activity()
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        self.assertIn("Let's try", response)

if __name__ == "__main__":
    unittest.main()