from flask import Flask, jsonify, request
text_to_morse  = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

# text = input("Enter text to convert to Morse: ").upper()
# morse_code = ''
# for char in text:
#     morse_code += text_to_morse[char] + ' '
app = Flask(__name__)


@app.route('/get-morse')
def morse_code():
    string = request.args.get('text')
    morse_code = ''
    for char in string.upper():
        morse_code += text_to_morse[char] + ' '
    return jsonify(
        code = {
            'message': 'Success',
            'English': string,
            'Morse Code': morse_code,
        }
    ), 200


@app.route('/read-morse')
def english():
    morse = request.args.get('morse')
    morse_to_eng = {}
    for k,v in text_to_morse.items():
        morse_to_eng[v]=k

    morse_text_split = morse.split()
    eng_text = ''
    for char in morse_text_split:
        eng_text += morse_to_eng[char]
    return jsonify(
        code={
            'message': 'Success',
            'Morse Code': morse,
            'English': eng_text,
        }
    ), 200


if __name__ == "__main__":
    app.run(debug=True)