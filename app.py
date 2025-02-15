{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b53216c0-cbde-4771-b498-55e4c1d28e07",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c1e3b62b-11da-401e-816e-f1aaad073030",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwriting app.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile app.py\n",
    "from flask import Flask, request, jsonify, render_template\n",
    "import numpy as np\n",
    "import joblib\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Load the trained model and label encoder\n",
    "model = joblib.load('iris_model.pkl')\n",
    "label_encoder = joblib.load('label_encoder.pkl')\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    # Render the homepage with the form\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    \"\"\"\n",
    "    Expects the following form or JSON data:\n",
    "    - sepal_length\n",
    "    - sepal_width\n",
    "    - petal_length\n",
    "    - petal_width\n",
    "    \"\"\"\n",
    "    # Get data from form or JSON body\n",
    "    data = request.form if request.form else request.json\n",
    "\n",
    "    try:\n",
    "        # Convert the input values to floats\n",
    "        sepal_length = float(data.get('sepal_length'))\n",
    "        sepal_width  = float(data.get('sepal_width'))\n",
    "        petal_length = float(data.get('petal_length'))\n",
    "        petal_width  = float(data.get('petal_width'))\n",
    "    except Exception as e:\n",
    "        return jsonify({'error': 'Invalid input. Ensure all values are provided and are numbers.'})\n",
    "    \n",
    "    # Prepare features for prediction\n",
    "    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])\n",
    "    prediction = model.predict(features)\n",
    "    # Convert encoded prediction back to original species label\n",
    "    species = label_encoder.inverse_transform(prediction)\n",
    "    \n",
    "    # Return the result as JSON\n",
    "    return jsonify({'predicted_species': species[0]})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    # When running in Jupyter, disable the reloader to avoid SystemExit exceptions.\n",
    "    app.run(debug=True, use_reloader=False)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
