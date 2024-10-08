from flask import Flask, request, jsonify
import json, os
import sys
import io

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()

    # Validate the script input
    if not data or 'script' not in data:
        return jsonify({'error': 'No script provided'}), 400

    script = data['script']
    local_vars = {}

    # Capture the stdout
    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    sys.stdout = redirected_output

    try:
        exec(script, {}, local_vars)

        # Check if main() function is present
        if 'main' not in local_vars:
            sys.stdout = old_stdout
            return jsonify({'error': 'main() function not found'}), 400

        # Execute the main() function and check if it returns a dictionary (JSON-like)
        result = local_vars['main']()

        if not isinstance(result, dict):
            sys.stdout = old_stdout
            return jsonify({'error': 'main() must return a JSON object'}), 400

        # Get the output from the redirected stdout
        stdout_output = redirected_output.getvalue()

        # Reset stdout to original before returning
        sys.stdout = old_stdout

        # Return the result and the stdout output as JSON
        return jsonify({"result": result, "stdout": stdout_output}), 200

    except Exception as e:
        # Reset stdout to original in case of exception
        sys.stdout = old_stdout
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

