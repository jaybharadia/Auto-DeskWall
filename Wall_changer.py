#!/usr/bin/python3
import io,time,os,requests

# Search terms : Cool Background, FEATURED, Wallpapers, COVID-19, Travel Nature Textures & Patterns, Current Events, People, Business, & Work, Technology, Animals, # Interiors Architecture, Food & Drink, Athletics Spirituality, Health & Wellness Fashion Experimental Arts & Culture History
query_term = 'Nature' 		
access_key = 'YOUR ACCESS KEY PROVIDED FROM UNSPLASH API' # Register as a developer on Unsplash API Site for getting a Access key
path = 'YOUR PATH FOR IMAGE TO STORE' # keep it absolute path not relative

########## First we will Contact Unsplash API Service using requests module for query random photo, then fetching url from json response
   ####### Then downloading it using requests module, applying it to windows, Linux later

#  Function for Setting Wallpaper at interval of x from a directory
def set_wall(): 
    # We are requesting random photo related to nature with orientation landscape from unsplash api and storing the JSON respone in object r
    # This is strictly dependent on your requirements. you can request any image, any size, any format, any resolution, any quality, any category, etc
    # Read more on Unsplash API about Dynamic Image URL
    try:
    	r = requests.get('https://api.unsplash.com/photos/random?client_id=' + access_key + '&query=' + query_term + '&orientation=landscape' , timeout=3)
  
    	
    except requests.exceptions.RequestException as e:
    	time.sleep(120)
    	return
    	# After getting JSON response in object r, we will extract img url value from nested key array by using json(), storing in img_url object
    img_url = r.json()['urls']['full']

    # Now we will Download the Img from the extracted dynamic url and store it in img object
    img = requests.get(img_url , allow_redirects=True)

    # Now, we will write img content into a file whatever.jpg to a desired path
    open(path + 'whatever.jpg' , 'wb').write(img.content)

   
    os.system('gsettings set org.gnome.desktop.background picture-uri file:///root/Pictures/Wallpapers/whatever.jpg') # Linux Function for setting as Wallpaper
    return

while True:
    set_wall()
    time.sleep(1800)          # Change wallpaper every x seconds
    
