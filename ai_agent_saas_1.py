class SpreadsheetSimulator:
    """Simulates a SaaS application that acts like a spreadsheet."""
    
    def __init__(self):
        self.data = {}
    
    def add_data(self, key, value):
        """Adds data to the 'spreadsheet'."""
        self.data[key] = value
        return f"Added {key}: {value}"
    
    def get_data(self, key):
        """Retrieves data from the 'spreadsheet'."""
        return self.data.get(key, "Key not found")
    
    def update_data(self, key, value):
        """Updates data in the 'spreadsheet'."""
        if key in self.data:
            self.data[key] = value
            return f"Updated {key}: {value}"
        return "Key not found"
    
    def delete_data(self, key):
        """Deletes data from the 'spreadsheet'."""
        if key in self.data:
            del self.data[key]
            return f"Deleted {key}"
        return "Key not found"


class AIAgent:
    """Simulates an AI agent that interacts with SaaS applications."""
    
    def __init__(self):
        self.spreadsheet = SpreadsheetSimulator()
    
    def handle_request(self, request):
        """Handles user requests and interacts with the SaaS application."""
        if "add" in request:
            key, value = request.split("add ")[1].split(" as ")
            return self.spreadsheet.add_data(key, value)
        
        elif "get" in request:
            key = request.split("get ")[1]
            return self.spreadsheet.get_data(key)
        
        elif "update" in request:
            key, value = request.split("update ")[1].split(" to ")
            return self.spreadsheet.update_data(key, value)
        
        elif "delete" in request:
            key = request.split("delete ")[1]
            return self.spreadsheet.delete_data(key)
        
        else:
            return "Sorry, I don't understand that request."


# Example usage
if __name__ == "__main__":
    ai_agent = AIAgent()
    
    # User interacts with the AI agent conversationally
    print(ai_agent.handle_request("add revenue as 10000"))  # Adds data
    print(ai_agent.handle_request("get revenue"))           # Retrieves data
    print(ai_agent.handle_request("update revenue to 15000"))  # Updates data
    print(ai_agent.handle_request("delete revenue"))        # Deletes data
    print(ai_agent.handle_request("get revenue"))           # Attempts to retrieve deleted data