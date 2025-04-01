import json
import os

# Define input and output paths
input_folder = os.path.join(os.path.dirname(__file__), '..', 'input')
output_folder = os.path.join(os.path.dirname(__file__), '..', 'output')

aloof_file = os.path.join(input_folder, 'a.aloof')
meta_file = os.path.join(input_folder, 'a.meta')
# Update the output file name to match the input file name
output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(aloof_file))[0] + '.json')

def parse_aloof_line(line):
    """Parses a single ALOOF line into a dictionary."""
    return {
        "aloof_line": line.strip(),
        "metadata": None  # No metadata available for now
    }

def parse_meta_data(meta_content):
    """Parses the meta data content into a list of dictionaries."""
    try:
        return json.loads(meta_content)
    except json.JSONDecodeError:
        print("Error: Invalid JSON in meta file.")
        return []

def process_aloof_file():
    """Processes the ALOOF file and generates JSON output."""
    if not os.path.exists(aloof_file):
        print(f"Error: {aloof_file} not found.")
        return

    with open(aloof_file, 'r') as f:
        aloof_lines = f.readlines()

    # Parse each line in the ALOOF file
    form_elements = []
    for line in aloof_lines:
        if line.strip():
            form_elements.append(parse_aloof_line(line))

    # Parse meta data if available
    meta_data = []
    if os.path.exists(meta_file):
        with open(meta_file, 'r') as f:
            meta_content = f.read().strip()
            if meta_content:
                meta_data = parse_meta_data(meta_content)

    # Combine ALOOF lines with meta data
    for i, element in enumerate(form_elements):
        if i < len(meta_data):
            element["metadata"] = meta_data[i]

    # Generate JSON output
    output_data = {
        "form_elements": form_elements
    }

    # Write to output file
    os.makedirs(output_folder, exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=4)

    print(f"JSON output written to {output_file}")

if __name__ == "__main__":
    process_aloof_file()