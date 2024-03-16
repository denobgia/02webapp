function calc(operation) {
    event.preventDefault()
    console.log("calc() function called with operation:", operation); // Add this line
    var number1 = parseFloat(document.getElementById('number1').value);
    var number2 = parseFloat(document.getElementById('number2').value);

    var requestBody = {
        number1: number1,
        number2: number2,
        operation: operation
    };

    fetch('/calc', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
    })
    .then(response => response.json())
    .then(input => {
        document.getElementById('result').innerText = "Result: " + input.result;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}