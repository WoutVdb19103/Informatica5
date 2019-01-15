#invoer
tweet = str(input('Geef een tweet: '))

#bewerking
while '#' in tweet:
    woord = tweet[tweet.find('#') + 1:tweet.find(' ')] + '\n'
    tweet = tweet[tweet.find(woord):]

    print(woord)

