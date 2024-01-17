from flask import Flask, render_template, request, jsonify
import torch
import numpy as np
from ColorClassifier import ColorClassifier

app = Flask(__name__)

def processing(hex_color):
    hex_color = hex_color.lstrip('#')
    hex_color = np.array([int(hex_color[i:i+2], 16) for i in (0, 2, 4)])/ 255.0
    return torch.FloatTensor(hex_color)


def predict(color):
    shades = {0:'#FFFFFF', 1:'#F5F5F5', 2:"#F0F8FF", 3:'#EDEDED', 4:'#FAFAFA',5:'#000000', 6:'#111111', 7:"#1A1A1A", 8:'#333333', 9:'#2C3E50'};

    colorRGB = processing(color)
    model = ColorClassifier() 
    model.load_state_dict(torch.load('ColorMatching.pth'))
    model.eval()  

    predicted = torch.argmax(model(colorRGB)) 
    num = predicted.item() 

    List_color = [0,1,2,3,4,5,6,7,8,9]
    if (num in List_color ): return shades[num]
    else: return "#000000"




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict_color', methods=['POST'])
def predict_color():
    try:
        background_color = request.form['backgroundColor']
        print('Received color:', background_color)
        prediction = predict(background_color)
        print(prediction)
        return jsonify({'prediction': prediction})
    except Exception as e:
        print('Error:', str(e))
        return jsonify({'error': 'Internal Server Error'}), 500





if __name__ == '__main__':
    app.run(debug=True)
