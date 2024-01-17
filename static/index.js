const welcomeText = document.getElementById("welcomeText");
const chooseText = document.getElementById("choose");
const backgroundColorInput = document.getElementById("backgroundColor");


function updateColors() {
    const backgroundColor = backgroundColorInput.value;
    document.body.style.backgroundColor = backgroundColor;

   
    fetch('/predict_color', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `backgroundColor=${backgroundColor}`,
    })
    .then(response => response.json())
    .then(data => {
        const prediction = data.prediction;
        chooseText.style.color = prediction;
        welcomeText.style.color = prediction;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

backgroundColorInput.addEventListener("input", updateColors);


updateColors();