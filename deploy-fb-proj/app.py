from flask import Flask, render_template
from bs4 import BeautifulSoup
import plotly.express as px
import pandas as pd

app = Flask(__name__)
with open('data\\comments.html', 'r', encoding='utf-8') as file:
    html_data = file.read()

soup = BeautifulSoup(html_data, 'html.parser')

keywords_to_find = ['reacted', 'liked']
keyword_counts = {keyword: 0 for keyword in keywords_to_find}

for keyword in keywords_to_find:
    # Find all occurrences of the keyword in the HTML
    occurrences = soup.find_all(lambda tag: tag.get('class') and keyword in tag.get('class'))

    # Update the count in the dictionary
    keyword_counts[keyword] = len(occurrences)

# Print the counts and debug information
for keyword, count in keyword_counts.items():
    print(f'{keyword}: {count} occurrences')

# Create a simple Plotly figure (replace this with your actual data and chart)
data = {'Keyword': list(keyword_counts.keys()), 'Count': list(keyword_counts.values())}
df = pd.DataFrame(data)
fig = px.bar(df, x='Keyword', y='Count', title='Keyword Occurrences')

@app.route("/")
def dashboard():
    # Convert Plotly figure to HTML to embed in the template
    graph_html = fig.to_html(full_html=False)
    return render_template('index.html', graph_html=graph_html)

if __name__ == "__main__":
    app.run(debug=True)
