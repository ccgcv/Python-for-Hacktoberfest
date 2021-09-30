#Created By Navneet Das
#Part 1A: Scraping Data Based on Specific Hashtags from Twitter

#config file contains all the tokens of Twitter Developer API and the ouptut file
#the contents of config file can be pasted here too but for cleaner code I have made a seperate file
from config import ACCESSTOKEN , ACCESSTOKENSECRET, APIKEY, APISECRETKEY, CSV_FILE_NAME, COLS, HASHTAGS, COUNT
from tweepy import OAuthHandler, API, Cursor
import pandas as pd
from csv import writer, DictReader
import os

#For connecting to Twitter API
auth = OAuthHandler(APIKEY, APISECRETKEY)   
auth.set_access_token(ACCESSTOKEN, ACCESSTOKENSECRET)
api = API(auth, wait_on_rate_limit=True)


#For checking if the output file exists 
def check_if_csv_exists(path_to_file):
    #path_to_file contains the file path and returns a boolean value based on if it exists
    return True if os.path.exists(path_to_file) else False


#To avoid duplicate texts in dataset
def check_if_text_exists(text,path):
    #takes in file path and returns a boolean value whether the tweet text exists in the CSV file
    if check_if_csv_exists(path):
        with open(CSV_FILE_NAME) as csv_file:
            csv_reader = DictReader(csv_file)
            for row in csv_reader:
                if row["Text"] == text:
                    return True
        return False
    else:
        return False


#Enters the new scraped tweet details into csv
def append_list_as_row(file_name, list_of_elem):
    #Takes in the path to CSV file, list containing the new row entry.
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)


#To get the recent tweet ID to avoid older tweets from showing up.
def get_recent_id():
    #Returns ID of recent Tweet
    with open(CSV_FILE_NAME) as csv_file:
        id_reader = DictReader(csv_file)
        lists = [row["ID"] for row in id_reader]
    return max(lists)


#API calls to Twitter
def tweepy_cursor(file_status):
    #Return List of Tweets
    last_id = get_recent_id() if file_status else None
    return [tweet for tweet in Cursor(api.search, q = HASHTAGS, lang = "en",since_id = last_id,  tweet_mode = 'extended').items(COUNT)]

def scrape_and_save():
    path_to_file = f"{os.getcwd()}/{CSV_FILE_NAME}" 
    flag = check_if_csv_exists(path_to_file)
    tweets = tweepy_cursor(flag)
    
    for tweet in tweets:
        tweet_id = tweet.id
        try:
            text = tweet.retweeted_status.full_text.encode('utf-8')
        except AttributeError:  # Not a Retweet
            text = tweet.full_text.encode('utf-8')
        
        if check_if_text_exists(text,path_to_file):
            continue
        
        user_name = tweet.user.screen_name.encode('utf-8')
        created_at = tweet.created_at
        user_followers = tweet.user.followers_count
        entry_rows = [tweet_id, text, created_at, user_name, user_followers]
        
        flag = check_if_csv_exists(path_to_file)
        if flag :
            append_list_as_row(path_to_file,entry_rows)
        else:
            #Create the CSV.
            first_entry = {"ID":tweet_id,"Text":text,"Created At":created_at,"Username":user_name,"Number of Followers":user_followers}
            CSV = pd.DataFrame(columns = COLS).append(first_entry,ignore_index=True)
            CSV.to_csv(path_to_file,index=False)

scrape_and_save()