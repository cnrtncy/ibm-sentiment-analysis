''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO

app = Flask("Sentiment Analyzer")
#Initiate the flask app : TODO

@app.route("/sentimentAnalyzer", methods = ["GET"])
def sent_analyzer() -> str:
    """ This function gets the argument from website and post requests to Sentiment
    Analysis Library and gets the score and label of the resposne 
    """

    text_to_analyze = request.args.get("textToAnalyze")
    response = sentiment_analyzer(text_to_analyze)
    label = response["label"]
    score = response["score"]

    if label is None:
        return "Invalid input! Try again."
    label = label.split("_")[1]
    return f"The given text has been identified as {label} with a score of {score}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''

    return render_template('index.html')


if __name__ == "__main__":

    app.run(debug=True)
