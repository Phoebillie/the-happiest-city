import json

def grid_match(tweet_coords):
    """
    Locate coords by longitude and latitude.
    """
    tweets_lon = tweet_coords[0]
    tweets_lat = tweet_coords[1]

    if 144.70 <= tweets_lon <= 144.85:
        if -37.65 < tweets_lat <= -37.50:
            return 'A1'
        elif -37.80 < tweets_lat <= -37.65:
            return 'B1'
        elif -37.95 <= tweets_lat <= -37.80:
            return 'C1'
    elif 144.85 < tweets_lon <= 145.00:
        if -37.65 < tweets_lat <= -37.50:
            return 'A2'
        elif -37.80 < tweets_lat <= -37.65:
            return 'B2'
        elif -37.95 <= tweets_lat <= -37.80:
            return 'C2'
    elif 145.00 < tweets_lon <= 145.15:
        if -37.65 < tweets_lat <= -37.50:
            return 'A3'
        elif -37.80 < tweets_lat <= -37.65:
            return 'B3'
        elif -37.95 < tweets_lat <= -37.80:
            return 'C3'
        elif -38.10 <= tweets_lat <= -37.95:
            return 'D3'
    # elif tweets_lon == 145.00 and -38.10 <= tweets_lat <= -37.95:
    #     return 'D3'
    elif 145.15 < tweets_lon <= 145.30:
        if -37.65 < tweets_lat <= -37.50:
            return 'A4'
        elif -37.80 < tweets_lat <= -37.65:
            return 'B4'
        elif -37.95 <= tweets_lat <= -37.80:
            return 'C4'
        elif -38.10 <= tweets_lat <= -37.95:
            return 'D4'
    elif 145.30 < tweets_lon <= 145.45:
        if -37.95 < tweets_lat <= -37.80:
            return 'C5'
        elif -38.10 <= tweets_lat <= -37.95:
            return 'D5'

if __name__ == '__main__':
    filename = './files/tinyTwitter.json'
    with open(filename, 'r', encoding='utf-8') as f:
        fin = json.load(f)
        f.close()
    twitter_datas = fin['rows']
    datas = []
    for data in twitter_datas:
        tweet_coords = data['value']['geometry']['coordinates']
        result = grid_match(tweet_coords)
        print(result)
        data['value']['geometry']['coordinates'] = result
    
    # with open("./files/tinyTwitter_handle.json", "w") as fp:
    #     fp.write(json.dumps(twitter_datas))