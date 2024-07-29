
import json
import sys

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def fill_values(tests, values_map):
    if isinstance(tests, list):
        for test in tests:
            fill_values(test, values_map)
    elif isinstance(tests, dict):
        test_id = tests.get('id')
        if test_id in values_map:
            tests['value'] = values_map[test_id]
        if 'tests' in tests:
            fill_values(tests['tests'], values_map)

def main():
    if len(sys.argv) != 4:
        print("Usage: python 3.py <values.json> <tests.json> <report.json>")
        sys.exit(1)
    
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]
    
    values = load_json(values_file)
    tests = load_json(tests_file)
    
    values_map = {item['id']: item['value'] for item in values}
    
    fill_values(tests, values_map)
    
    save_json(tests, report_file)

if __name__ == "__main__":
    main()
