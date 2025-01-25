from flask import Flask, render_template, jsonify
import random
import joblib
import os

app = Flask(__name__)

# Define the path to the model file
MODEL_PATH = "difficulty_model.pkl"

# Check if the model file exists, and load it
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

# List of tasks
TASKS = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "How razorback-jumping frogs can level six piqued gymnasts!",
    "Jinxed wizards pluck ivy from the big quilt.",
    "Crazy Fredrick bought many very exquisite opal jewels.",
    "We promptly judged antique ivory buckles for the next prize.",
    "A mad boxer shot a quick, gloved jab to the jaw of his dizzy opponent.",
    "The five boxing wizards jump quickly.",
    "Jackdaws love my big sphinx of quartz.",
    "Mr. Jock, TV quiz PhD, bags few lynx.",
    "My faxed joke won a pager in the cable TV quiz show.",
    "Brawny gods just flocked up to quiz and vex him.",
    "Bright vixens jump; dozy fowl quack.",
    "Sphinx of black quartz, judge my vow.",
    "The job requires extra pluck and zeal from every young wage earner.",
]

# Function to shuffle tasks for each session
def get_shuffled_tasks():
    shuffled_tasks = TASKS[:]
    random.shuffle(shuffled_tasks)
    return shuffled_tasks

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks')
def tasks():
    shuffled_tasks = get_shuffled_tasks()
    return jsonify(shuffled_tasks)

if __name__ == '__main__':
    app.run(debug=True)
