import os
import openai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)

<<<<<<< HEAD
def check_missing_ingredients(user_ingredients):
    """Dynamically check what key ingredients might be missing for a realistic recipe."""
    essential_ingredients = set()  # Start with an empty list of required ingredients
    
    # Determine missing ingredients dynamically based on what was entered
    if "flour" in user_ingredients or "pasta" in user_ingredients:
        essential_ingredients.update(["salt", "water"])
    if "meat" in user_ingredients or "chicken" in user_ingredients:
        essential_ingredients.add("oil")
    if "vegetables" in user_ingredients:
        essential_ingredients.add("seasoning")

    # Find missing ingredients
    missing = [ingredient for ingredient in essential_ingredients if ingredient not in user_ingredients]

    return missing

def generate_recipe(ingredients):
    """Generate a recipe strictly using ONLY the ingredients provided by the user."""
    prompt = (
        f"I only have these ingredients: {', '.join(ingredients)}. "
        "Create a complete recipe using ONLY these ingredients, with no extra ingredients. "
        "If an ingredient is missing for a specific step, work around it creatively instead of adding new ingredients. "
        "Provide clear step-by-step instructions for preparing the dish."
=======
# Define essential ingredients for most recipes
essential_ingredients = ["salt", "pepper", "oil", "butter", "flour", "milk", "sugar", "eggs", 
                         "garlic", "onion", "cheese", "bread", "rice", "tomato", "chicken", 
                         "beef", "pasta", "potato", "water"]

def check_missing_ingredients(user_ingredients):
    """Check if the user is missing any essential ingredients."""
    missing = [ingredient for ingredient in essential_ingredients if ingredient not in user_ingredients]
    return missing

def generate_recipe(ingredients):
    """Generate a recipe using ONLY the user's ingredients."""
    prompt = (
        f"I only have these ingredients: {', '.join(ingredients)}. "
        "Generate a recipe using ONLY these ingredients. "
        "DO NOT include any extra ingredients. "
        "Provide clear instructions and avoid suggesting substitutions."
>>>>>>> 8b2833d (Initial Commit)
    )

    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
<<<<<<< HEAD
            {"role": "system", "content": "You are a helpful AI chef who only uses the provided ingredients."},
=======
            {"role": "system", "content": "You are a helpful AI chef."},
>>>>>>> 8b2833d (Initial Commit)
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

@app.route("/")
def index():
    """Render the homepage."""
    return render_template("index.html")

@app.route("/check_ingredients", methods=["POST"])
def check_ingredients():
<<<<<<< HEAD
    """Ask the user only about actually necessary missing ingredients."""
=======
    """Ask the user one-by-one about missing essential ingredients."""
>>>>>>> 8b2833d (Initial Commit)
    data = request.json
    ingredients = data.get("ingredients", [])

    missing = check_missing_ingredients(ingredients)

    return jsonify({"missing": missing})

@app.route("/get_recipe", methods=["POST"])
def get_recipe():
    """Generate a recipe only using the user's ingredients."""
    data = request.json
    ingredients = data.get("ingredients", [])

    if not ingredients:
        return jsonify({"error": "Please enter some ingredients"}), 400

    recipe = generate_recipe(ingredients)
    return jsonify({"recipe": recipe})

if __name__ == "__main__":
    app.run(debug=True)
