from flask import Flask,request

app = Flask(__name__)
@app.route("/")
def hello():
    data = request.values
    print(data["USD"])
    return {}

@app.route("/home")
def query():
    html = """
    <form action="http://127.0.0.1:5000/api/to-usd">
    <label>UZS</label>
    <input type="number" name="amount" value="">
    <input type="submit" value="To-USD">
    </form>
    <form action="http://127.0.0.1:5000/api/to-uzs">
    <label>USD</label>
    <input type="number" name="amount" value="">
    <input type="submit" value="To-UZS">
    </form>
    """
    return html

@app.route('/api/to-usd', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    data=request.values
    db={
        "amount": data["amount"],
        "currency": "USZ",
        "converted": round(int(data["amount"])/11390.7,4),
        "convertedCurrency": "UZS"
    }
    return db

@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """
    data=request.values
    db={
        "amount": data["amount"],
        "currency": "USD",
        "converted": int(data["amount"])*11390.7,
        "convertedCurrency": "UZS"
    }
    return db

if __name__ == "__main__":
    app.run(debug=True)
