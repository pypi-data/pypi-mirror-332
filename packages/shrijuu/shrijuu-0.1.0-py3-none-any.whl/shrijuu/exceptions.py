class LoveError(Exception):
    """Exception raised for errors in the love expressions."""
    def __init__(self, message="An error occurred while expressing love."):
        self.message = message
        super().__init__(self.message)

class DateError(Exception):
    """Exception raised for errors in date planning."""
    def __init__(self, message="An error occurred while planning a date."):
        self.message = message
        super().__init__(self.message)