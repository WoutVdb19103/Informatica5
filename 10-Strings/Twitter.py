#invoer
tweet = str(input('Geef een tweet: '))

#bewerking
while '#' in tweet:

    #hashtag uitknippen, inkorten en terug op zoek naar #

    woord = tweet[tweet.find('#') + 1:tweet.find(' ')] + '\n'

    tweet = tweet[tweet.find(woord):]

    print(woord)

