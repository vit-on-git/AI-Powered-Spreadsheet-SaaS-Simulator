import streamlit as st
import pandas as pd

class SpreadsheetSimulator:
    """Simulates a SaaS application that acts like a spreadsheet."""
    
    def __init__(self):
        if "data" not in st.session_state:
            st.session_state.data = {}
        if "history" not in st.session_state:
            st.session_state.history = []
    
    def add_data(self, key, value):
        try:
            st.session_state.data[key] = float(value)
        except ValueError:
            st.session_state.data[key] = value
        result = f"Added {key}: {st.session_state.data[key]}"
        st.session_state.history.append(result)
        return result
    
    def get_data(self, key):
        result = st.session_state.data.get(key, "Key not found")
        st.session_state.history.append(f"Retrieved {key}: {result}")
        return result
    
    def update_data(self, key, value):
        if key in st.session_state.data:
            try:
                st.session_state.data[key] = float(value)
            except ValueError:
                st.session_state.data[key] = value
            result = f"Updated {key}: {st.session_state.data[key]}"
            st.session_state.history.append(result)
            return result
        return "Key not found"
    
    def delete_data(self, key):
        if key in st.session_state.data:
            del st.session_state.data[key]
            result = f"Deleted {key}"
            st.session_state.history.append(result)
            return result
        return "Key not found"
    
    def sum_data(self, keys):
        try:
            total = sum(st.session_state.data[key] for key in keys if isinstance(st.session_state.data.get(key), (int, float)))
            result = f"Sum: {total}"
            st.session_state.history.append(result)
            return result
        except KeyError:
            return "One or more keys not found"
    
    def multiply_data(self, keys):
        try:
            result = 1
            for key in keys:
                if isinstance(st.session_state.data.get(key), (int, float)):
                    result *= st.session_state.data[key]
                else:
                    return f"Key '{key}' is not a number"
            result_text = f"Multiplication result: {result}"
            st.session_state.history.append(result_text)
            return result_text
        except KeyError:
            return "One or more keys not found"
    
    def evaluate_formula(self, formula):
        try:
            for key in st.session_state.data:
                if isinstance(st.session_state.data[key], (int, float)):
                    formula = formula.replace(key, str(st.session_state.data[key]))
            result = f"Formula result: {eval(formula)}"
            st.session_state.history.append(result)
            return result
        except Exception as e:
            return f"Error evaluating formula: {str(e)}"
    
    def list_all(self):
        return st.session_state.data if st.session_state.data else "No data stored"
    
    def get_history(self):
        return st.session_state.history
    
    def save_to_csv(self, filename="spreadsheet_data.csv"):
        df = pd.DataFrame(st.session_state.data.items(), columns=["Key", "Value"])
        df.to_csv(filename, index=False)
        return f"Data saved to {filename}"

st.title("AI-Powered Spreadsheet Simulator")

agent = SpreadsheetSimulator()

commands = [
    "add revenue as 10000",
    "get revenue",
    "update revenue to 12000",
    "delete revenue",
    "sum revenue and expenses",
    "multiply revenue and profit",
    "formula revenue - expenses",
    "list all",
    "save csv"
]

selected_command = st.selectbox("Choose a command:", commands)
custom_command = st.text_input("Or enter a custom command:")

final_command = custom_command if custom_command else selected_command

if st.button("Submit"):
    if "add" in final_command:
        key, value = final_command.split("add ")[1].split(" as ")
        st.write(agent.add_data(key, value))
    elif "get" in final_command:
        key = final_command.split("get ")[1]
        st.write(agent.get_data(key))
    elif "update" in final_command:
        key, value = final_command.split("update ")[1].split(" to ")
        st.write(agent.update_data(key, value))
    elif "delete" in final_command:
        key = final_command.split("delete ")[1]
        st.write(agent.delete_data(key))
    elif "sum" in final_command:
        keys = final_command.split("sum ")[1].split(" and ")
        st.write(agent.sum_data(keys))
    elif "multiply" in final_command:
        keys = final_command.split("multiply ")[1].split(" and ")
        st.write(agent.multiply_data(keys))
    elif "formula" in final_command:
        formula = final_command.split("formula ")[1]
        st.write(agent.evaluate_formula(formula))
    elif "list all" in final_command:
        st.write(agent.list_all())
    elif "save csv" in final_command:
        st.write(agent.save_to_csv())
    else:
        st.write("Sorry, I don't understand that request.")

st.subheader("Command History")
st.write(agent.get_history())
