import re

pattern = re.compile(r'(?i)T480(?!S)', re.IGNORECASE)

# Example strings for testing
test_strings = ["T480", "T480s", "t480S", "T480S", "T480 followed by text", "T480S followed by text"]

# Find matches
for test_string in test_strings:
    match = pattern.search(test_string)
    if match:
        print(f"Match found: {test_string}")
    else:
        print(f"No match: {test_string}")
