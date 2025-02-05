class SpreadsheetSimulator:
    """Simulates a SaaS application that acts like a spreadsheet."""
    
    def __init__(self):
        self.data = {}
    
    def add_data(self, key, value):
        """Adds data to the 'spreadsheet'."""
        try:
            self.data[key] = float(value)  # Store as numeric value if possible
        except ValueError:
            self.data[key] = value  # Store as string if not numeric
        return f"Added {key}: {self.data[key]}"
    
    def get_data(self, key):
        """Retrieves data from the 'spreadsheet'."""
        return self.data.get(key, "Key not found")
    
    def update_data(self, key, value):
        """Updates data in the 'spreadsheet'."""
        if key in self.data:
            try:
                self.data[key] = float(value)  # Convert to number if possible
            except ValueError:
                self.data[key] = value
            return f"Updated {key}: {self.data[key]}"
        return "Key not found"
    
    def delete_data(self, key):
        """Deletes data from the 'spreadsheet'."""
        if key in self.data:
            del self.data[key]
            return f"Deleted {key}"
        return "Key not found"
    
    def sum_data(self, keys):
        """Calculates the sum of multiple numerical values."""
        try:
            total = sum(self.data[key] for key in keys if isinstance(self.data.get(key), (int, float)))
            return f"Sum: {total}"
        except KeyError:
            return "One or more keys not found"
    
    def multiply_data(self, keys):
        """Multiplies multiple numerical values."""
        try:
            result = 1
            for key in keys:
                if isinstance(self.data.get(key), (int, float)):
                    result *= self.data[key]
                else:
                    return f"Key '{key}' is not a number"
            return f"Multiplication result: {result}"
        except KeyError:
            return "One or more keys not found"
    
    def evaluate_formula(self, formula):
        """Evaluates a basic arithmetic formula using stored data."""
        try:
            for key in self.data:
                if isinstance(self.data[key], (int, float)):
                    formula = formula.replace(key, str(self.data[key]))
            return f"Formula result: {eval(formula)}"
        except Exception as e:
            return f"Error evaluating formula: {str(e)}"
    
    def list_all(self):
        """Lists all stored key-value pairs."""
        return self.data if self.data else "No data stored"


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
        
        elif "sum" in request:
            keys = request.split("sum ")[1].split(" and ")
            return self.spreadsheet.sum_data(keys)
        
        elif "multiply" in request:
            keys = request.split("multiply ")[1].split(" and ")
            return self.spreadsheet.multiply_data(keys)
        
        elif "formula" in request:
            formula = request.split("formula ")[1]
            return self.spreadsheet.evaluate_formula(formula)
        
        elif "list all" in request:
            return self.spreadsheet.list_all()
        
        else:
            return "Sorry, I don't understand that request."


# Example usage
if __name__ == "__main__":
    ai_agent = AIAgent()
    
    # Adding data
    print(ai_agent.handle_request("add revenue as 10000"))
    print(ai_agent.handle_request("add expenses as 5000"))
    print(ai_agent.handle_request("add profit as 2000"))
    
    # Retrieving and updating
    print(ai_agent.handle_request("get revenue"))
    print(ai_agent.handle_request("update revenue to 15000"))
    
    # Performing calculations
    print(ai_agent.handle_request("sum revenue and expenses"))
    print(ai_agent.handle_request("multiply revenue and profit"))
    print(ai_agent.handle_request("formula revenue - expenses"))
    
    # Listing all data
    print(ai_agent.handle_request("list all"))
