import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000): # iter_content is a method that returns chunks of content. 100,000 bytes.
    playFile.write(chunk)

playFile.close()