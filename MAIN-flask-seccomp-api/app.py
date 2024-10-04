# code written by Mélik Sevestre

from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()

    # Script input validation
    if not data or 'script' not in data:
        return jsonify({'error': 'You forgot the script !'}), 400

    script = data['script']
    local_vars = {}

    # Secure script exec
    try:
        exec(script, {}, local_vars)

        # Check if main() function is present
        if 'main' not in local_vars:
            return jsonify({'error': 'main() function missing'}), 400

        # execute the main() function and check if it returns a dictionary
        result = local_vars['main']()

        if not isinstance(result, dict):
            return jsonify({'error': 'main() function must return a JSON object'}), 400

        # Return JSON result
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080)) # variable env 'PORT' pour Google Cloud Run
    app.run(host='0.0.0.0', port=port)

