##
#author: Steve Keller
#This program reads a file from google
#drive, stores it in the t drive, unzips the
#file and stores it inside of mySQL
##

#https://drive.google.com/a/gsa.gov/file/d/18owini8HeiJGdrBaxwD_NXGcwVusmX-s/view?usp=drivesdk

#Import libraries for uploading
import requests

#download_file_from_google_drive
#Saves a file from google drive to a destination
#Input: two character drives
#Output: File saved to directory as a zip file
def download_file_from_google_drive(destination):
    #URL = "https://docs.google.com/uc?export=download"
    URL = "https://drive.google.com/a/gsa.gov/file/d/18owini8HeiJGdrBaxwD_NXGcwVusmX-s/view?usp=drivesdk"
    session = requests.Session()

    #response = session.get(URL, params = { 'id' : id }, stream = True)
    response = session.get(URL, stream = True)
    token = get_confirm_token(response)

    #if token:
    #    params = { 'id' : id, 'confirm' : token }
    #    response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

#get_confirm_token
#returns a value of a warning 
#input response 
#returns a download warning 
def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None
	
#save_response_content
#writes file from google drive to file destination
#input: file response and destination address
#output: write file to destination 
def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
				
				
#begin main program kick off				
if __name__ == "__main__":
	#set file id
    #file_id = 'TAKE ID FROM SHAREABLE LINK'
	
	#set or collect destination 
    destination = 'H:\Git\Raw Data'
	
	#download file from google drive 
    download_file_from_google_drive(destination)