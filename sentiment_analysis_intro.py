# sentiment analysis algorithm suing python without NLP

# - sentiment analysis- analyse the reviews- whether its +ve,-ve,etc
#  analyse the gold design review, making charge review, etc
#  data from social platform can be collected using API
#  for eg, the API for collecting public data is Graph API

# Step 1: Tokenisation
# - split data by word, output is called 'Tokens'

# Step 2: Create 2 dictionaries - +ve and -ve
# - +ve dict for +ve words, and -ve for -ve words
# - these dictionaries can either be created or can be downloaded

# Step 3: Comparison
# - compare tokens with dictionaries, if the token is in +ve dict word assign value as 1,
#  if it is in -ve dict assign -1, and if it is a neutral word(words not in both) assign 0
#  very, not such words are considered incremental word, if very is followed by
#  good, the value of very will be +0.5, very good = .5+1= 1.5
#  not good: not= -0.5, good = 1 , count = -.5+1 =.5

# Step 4: Count the value:
#  - if the count is +ve value, the comment is considered as +ve
#  eg, comment is "good company"
#     good - +1
#     company - 0
#     count = 1+0 =1 ==> +ve comment