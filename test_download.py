#use request libraries
#import requests

#url for the
#url = 'https://drive.google.com/a/gsa.gov/file/d/18owini8HeiJGdrBaxwD_NXGcwVusmX-s/view?usp=drivesdk'
#dest = 'H:/Git/Raw Data'

#print('Beginning file download with requests')  
#r = requests.get(url)

#with open('H:/Git/Raw Data/FPDS.zip', 'wb') as f:  
#    f.write(r.content)

#test url 
#https://drive.google.com/open?id=1hcFY_DzKT4rL2RA-tkUm2ptvqGp16rUK

import requests

def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    


if __name__ == "__main__":
    
    import sys
    # TAKE ID FROM SHAREABLE LINK
    #file_id = sys.argv[1]
    file_id = '1hcFY_DzKT4rL2RA-tkUm2ptvqGp16rUK'
    # DESTINATION FILE ON YOUR DISK
    #destination = sys.argv[2]
    destination = 'H:/Git/Raw Data/FPDS.txt'
    download_file_from_google_drive(file_id, destination)
 
