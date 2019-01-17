#invoer
tweet = str(input('Geef een tweet: '))

#bewerking
while '#' in tweet:

    #hashtag uitknippen, inkorten en terug op zoek naar #

    woord = tweet[tweet.find('#') + 1:tweet.find(' ')] + '\n'

    tweet = tweet[tweet.find(woord):]

    print(woord)

#tweet = input('geef tweet: ')
#
#i_hashtag = tweet.find('#')
#
#while i_hashtag != -1:
#    # tweet afknippen na het #-teken
#    tweet = tweet[i_hashtag + 1:]
#    i_spatie = tweet.find(' ')
#
#    # hashtag uiknippen en printen
#    print(tweet[:i_spatie])
#
#    # terug op zoek naar een hashtag
#    i_hashtag = tweet.find('#')