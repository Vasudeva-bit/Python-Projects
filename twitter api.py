import tweepy
auth = tweepy.OAuthHandler('KbrrVhiI2P4a2ynG4wI8Hbkf7', 
'8wsToXVxJbROFEneryYnb7tdNCEbnBp4QFYfyeKxsGxq0RkYi1')
auth.set_access_token('1299398711781408770-
0bB0vYkgahHambA4LHLwQBsFPgfvwW','MqYiEQcSgHOAeG1ZWJbrUOjFWro2cq161BwQfD2sEBr
Lf('api = tweepy.API(auth):
print(api.me().name)