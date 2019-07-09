import requests

url = 'https://drive.google.com/a/gsa.gov/file/d/18owini8HeiJGdrBaxwD_NXGcwVusmX-s/view?usp=drivesdk'
dest = 'H:/Git/Raw Data'

print('Beginning file download with requests')  
r = requests.get(url)

with open('H:/Git/Raw Data/FPDS.zip', 'wb') as f:  
    f.write(r.content)
 
