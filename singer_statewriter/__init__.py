import io
import json
import sys
import argparse

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A simple script to capture Singer.io state messages and write them to a state file.')
    parser.add_argument('state', type=str, help='Path to state JSON file')
    args = parser.parse_args()

    input_messages = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    for message in input_messages:
        try:
            message = json.loads(message)

            if message['type'] == 'STATE':
                with open(args.state, 'w') as f:
                    json.dump(message['value'], f, indent=2)
        except:
            pass

if __name__ == "__main__":
    main()
