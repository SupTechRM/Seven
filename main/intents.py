# Get Trending Searches using pytrends
import pytrends                    
from pytrends.request import TrendReq
pytrend = TrendReq()

class TrendingSearches:
    def __init__(self):
        
        # Define a Region
        self.region = ["india", "united_states", "canada"]
        
        # Define a list to store the Regions
        self.keywords = []
        
        # Define a list to store the trending searches
        self.trends = [] 

        self.intents()

    def intents(self):
        # Loop through each region and find the trending searches
        for region in self.region:
            # Get the trending searches
            trend = pytrend.trending_searches(pn=region)
            # Add the trending searches to self.trends as a list
            self.trends.append(trend.head())
        
        # Return self.trends
        return self.trends


TrendingsearchObj = TrendingSearches()
