import unittest
from numpy import source
import pandas as pd
import sys, os
 
sys.path.append(os.path.abspath(os.path.join('../..')))

from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor

_, tweet_list = read_json("tests/Economic_Twitter_Data.json")

columns = ['created_at', 'source', 'original_text','clean_text', 'sentiment','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count', 
    'original_author', 'screen_count', 'followers_count','friends_count','possibly_sensitive', 'hashtags', 'user_mentions', 'place', 'place_coord_boundaries']


class TestTweetDfExtractor(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:5])
        # tweet_df = self.df.get_tweet_df() 
                


    def test_find_statuses_count(self):
        self.assertEqual(self.df.find_statuses_count(), [40, 40, 40, 40, 40])

    def test_find_full_text(self):

        self.assertEqual(self.df.find_full_text(),test)
        test = ['RT @nikitheblogger: Irre: Annalena Baerbock s[92 chars]t e�','RT @[32 chars]aerbock sagt, es bricht ihr das[25 chars]t e\ufffd']

    def test_find_sentiments(self):
        sentiment_values = ([0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0])
        self.assertEqual(self.df.find_sentiments(self.df.find_full_text()),
                                                 sentiment_values)
    def test_find_created_time(self):
        created_at = ['Fri Apr 22 22:20:18 +0000 2022','Fri Apr 22 22:19:16 +0000 2022','Fri Apr 22 22:17:28 +0000 2022','Fri Apr 22 22:17:20 +0000 2022','Fri Apr 22 22:13:15 +0000 2022']

        self.assertEqual(self.df.find_created_time(), created_at)

    def test_find_source(self):
        self.assertEqual(self.df.find_source(), source)
        sourcen = ['<a h[18 chars]r.com/download/android" rel="nofollow">Twitter for Android</a>','<a h[18 chars]r.com/download/android" rel="nofollow">Twitter for ']

    def test_find_screen_name(self):
        name = ['McMc74078966', 'McMc74078966', 'McMc74078966', 'McMc74078966', 'McMc74078966']
        self.assertEqual(self.df.find_screen_name(), name)

    def test_find_followers_count(self):
        f_count = [3, 3, 3, 3, 3]
        self.assertEqual(self.df.find_followers_count(), f_count)

    def test_find_friends_count(self):
        friends_count = [12, 12, 12, 12, 12]
        self.assertEqual(self.df.find_friends_count(), friends_count)

    def test_find_is_sensitive(self):
        self.assertEqual(self.df.is_sensitive(), [None, None, None, None, None])

    def test_find_favourite_count(self):
        self.assertEqual(self.df.find_favourite_count(), [0, 0, 0, 0, 0])

    def test_find_retweet_count(self):
        self.assertEqual(self.df.find_retweet_count(), [355, 505, 4, 332, 386])
    # def test_find_hashtags(self):
    #     self.assertEqual(self.df.find_hashtags(), )

    # def test_find_mentions(self):
    #     self.assertEqual(self.df.find_mentions(), )

    def test_find_location(self):
        self.assertEqual(self.df.find_location(), ['', '', '', '', ''])

if __name__ == '__main__':
	unittest.main()

    