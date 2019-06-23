from selenium import webdriver
import requests
from bs4 import BeautifulSoup


#see_what_u_are_downloading is the function that is automating the Firefox browser to fetch the url results . This is optional to use to see images tab in real time.
    
def see_what_u_are_downloading(url):
    driver = webdriver.Firefox(executable_path=r"E:\geckodriver-v0.24.0-win64\geckodriver.exe")
    driver.get(url)
    images = driver.find_elements_by_tag_name('img')
    for image in images:
        image_url = image.get_attribute('src')
    driver.close()

def get_my_image(url):
    
    response = requests.get(url)                       #captured the return value of get(), which is an instance of Response, and stored it in a variable called response

    soup = BeautifulSoup(response.text, 'html.parser') #Create a BeautifulSoup object and define the parser.
    
    img_tags = soup.find_all('img')                    #Extracting img tag

    #print(img_tags)
    
    urls = [img['src'] for img in img_tags]            #Extracting source of the images from the img tag 
    
    
    image_url=urls[0]                                  #Taking the first URL from urls ... Your choice u can take any url between zero and len(urls)-1

    img_data = requests.get(image_url).content         #Getting the image from the url and storing it inside img_data
    
    with open(keyword[0]+'.jpg', 'wb') as handler:     #Creating a file with the KEYWORD name in the default directory where the script is located as handler
        handler.write(img_data)                        #writing the file to handler




#main function
if __name__ == "__main__":
    
                                                        #Keyword Entered By User For Searching

    keyword = list(input("Enter Keyword for search:\n").split())

                                                        #URL formation using that keyword

    if len(keyword)==1:
    
        url ="https://www.google.com/search?tbm=isch&q="+keyword[0]
    
    else:   
                                                        #If keyword is more than one than concatenation will take place
        url ="https://www.google.com/search?tbm=isch&q="
        for i in keyword:
            url+=i+"+"
        url=url.rstrip("+")
    
        #print(url)
    see_what_u_are_downloading(url)                     #Comment It out if you don't want to see the images in browser. 
    get_my_image(url)                                   #calling the get_my_image function
