
# Welcome to the API!

Some projects just don't necessitate implementation of a user interface. in these cases, an API provides the perfect point if interaction between the user and some sweet sweet back end code.

Currently, my website only supports GET requests. For the uninitiated, you can learn all about GET requests here : https://learning.postman.com/docs/getting-started/sending-the-first-request/



# The backing track creator - BTC 
```
https://www.SheltonTolbert.com/api/btc?url='youtube-link'
```
The purpose of the backing track creator is to remove vocals and lead instruments from songs. This is perfect for karaoke parties or musicians wanting to create their own covers. 
The btc API call accepts a youtube url as an argument, passes the information to a local server for processing and returns an mp3 with the center channel removed. 
For more information on the process of center channel removal via phase manipulation, refer to : https://github.com/SheltonTolbert/backing-track-creator 

# PyFinder
```
https://www.SheltonTolbert.com/api/py-finder
```
pyFinder is a webscraper which collects the top 180 trending python libraries and sends you to a random PyPi page! The idea is to go to a random page and build an application using the randomly presented library.


