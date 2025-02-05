import streamlit as st

class SpreadsheetSimulator:
    """Simulates a SaaS application that acts like a spreadsheet."""
    
    def __init__(self):
        self.data = {}
    
    def add_data(self, key, value):
        try:
            self.data[key] = float(value)  # Store as numeric value if possible
        except ValueError:
            self.data[key] = value  # Store as string if not numeric
        return f"Added {key}: {self.data[key]}"
    
    def get_data(self, key):
        return self.data.get(key, "Key not found")
    
    def update_data(self, key, value):
        if key in self.data:
            try:
                self.data[key] = float(value)
            except ValueError:
                self.data[key] = value
            return f"Updated {key}: {self.data[key]}"
        return "Key not found"
    
    def delete_data(self, key):
        if key in self.data:
            del self.data[key]
            return f"Deleted {key}"
        return "Key not found"
    
    def sum_data(self, keys):
        try:
            total = sum(self.data[key] for key in keys if isinstance(self.data.get(key), (int, float)))
            return f"Sum: {total}"
        except KeyError:
            return "One or more keys not found"
    
    def multiply_data(self, keys):
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
        try:
            for key in self.data:
                if isinstance(self.data[key], (int, float)):
                    formula = formula.replace(key, str(self.data[key]))
            return f"Formula result: {eval(formula)}"
        except Exception as e:
            return f"Error evaluating formula: {str(e)}"
    
    def list_all(self):
        return self.data if self.data else "No data stored"

st.title("AI-Powered Spreadsheet Simulator")

agent = SpreadsheetSimulator()

command = st.text_input("Enter your command:")

if st.button("Submit"):
    if "add" in command:
        key, value = command.split("add ")[1].split(" as ")
        st.write(agent.add_data(key, value))
    elif "get" in command:
        key = command.split("get ")[1]
        st.write(agent.get_data(key))
    elif "update" in command:
        key, value = command.split("update ")[1].split(" to ")
        st.write(agent.update_data(key, value))
    elif "delete" in command:
        key = command.split("delete ")[1]
        st.write(agent.delete_data(key))
    elif "sum" in command:
        keys = command.split("sum ")[1].split(" and ")
        st.write(agent.sum_data(keys))
    elif "multiply" in command:
        keys = command.split("multiply ")[1].split(" and ")
        st.write(agent.multiply_data(keys))
    elif "formula" in command:
        formula = command.split("formula ")[1]
        st.write(agent.evaluate_formula(formula))
    elif "list all" in command:
        st.write(agent.list_all())
    else:
        st.write("Sorry, I don't understand that request.")
