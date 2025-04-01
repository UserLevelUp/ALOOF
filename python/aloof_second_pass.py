import json
import os
import re

# Define input and output paths
input_folder = os.path.join(os.path.dirname(__file__), '..', 'output')
output_folder = os.path.join(os.path.dirname(__file__), '..', 'output')

input_file = os.path.join(input_folder, 'a.json')
output_file = os.path.join(output_folder, 'a_2.json')

def extract_label_list_and_input(aloof_line):
    """Extracts the list (e.g., [1]), label, and input type from an aloof_line."""
    match = re.match(r"\[(\d*)\] (.*?) \((.*?)\)\((.*?)\)", aloof_line)
    if match:
        list_number = match.group(1)  # Extract the list number
        label = match.group(2)        # Extract the label part
        input_type = match.group(4)   # Extract the input type
        return list_number, label, input_type
    return None, None, None

def process_labels_lists_and_inputs():
    """Processes the JSON file to extract lists, labels, inputs, and combine metadata."""
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r') as f:
        data = json.load(f)

    form_elements = data.get("form_elements", [])
    processed_elements = []

    for element in form_elements:
        aloof_line = element.get("aloof_line", "")
        list_number, label, input_type = extract_label_list_and_input(aloof_line)
        if label:
            label_object = {
                "text": label,
                "metadata": element.get("metadata", None)
            }
            processed_element = {
                "label": label_object
            }
            if list_number:
                processed_element["list"] = f"[{list_number}]"
            if input_type:
                processed_element["input"] = {
                    "type": input_type
                }
            processed_elements.append(processed_element)

    # Write the processed JSON output
    with open(output_file, 'w') as f:
        json.dump({"form_elements": processed_elements}, f, indent=4)

    print(f"Processed JSON with labels, lists, and inputs written to {output_file}")

if __name__ == "__main__":
    process_labels_lists_and_inputs()