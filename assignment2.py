from mediawiki import MediaWiki
from thefuzz import fuzz
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

def main():
    wikipedia = MediaWiki()
    babson = wikipedia.page("Babson College")
    bentley = wikipedia.page("Bentley University")


    babson_content = str(babson.content)
    bentley_content = str(bentley.content)
    print(fuzz.ratio(babson_content, bentley_content))
    # 4




if __name__ == "__main__":
    main()