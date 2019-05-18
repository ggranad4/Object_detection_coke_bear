#
import jpgConverter
import os
from google_images_download import google_images_download   #importing the library
def googleImageConverter(arguments):
    
    response = google_images_download.googleimagesdownload() 
    paths = response.download(arguments)   #passing the arguments to the function
    path = str(paths)
    pathv2 = os.path.dirname(path)

    pathv3 = pathv2.split("/")
    length = len(pathv3) - 2
    directory = '/'
    final_directory = []
    final_directory.append('/')

    count = 0

    for x in range(len(pathv3)):
        if (x == 0 or x == length):
            print('')
        elif(pathv3[x] =='downloads' and count == 0):
            count+=1
            final_directory[0].replace(''    , '')
            final_directory.append(pathv3[x])
            
        elif(count == 0):
                directory += pathv3[x] + '/'
                final_directory.append(pathv3[x]+ '/')
        
        
    jpgConverter.converter(''.join(final_directory),0)       




count = 0
ans=True
cat = [] 
limit1 = []
while ans:
    print ("""
    1.Enter a category for google to download
    2.Exit/Quit
    """)
    option = input ('Select an option: ')
    if option == "1": 
      print(count)
      option = input ('Enter a category: ')
      cat.append(option)
      limit = input('Enter the limit for this category:')
      limit1.append(limit)
      count = count + 1

    elif option == "2":
      for x in range(count):
        
        arguments = {"keywords":cat[x],"limit":limit1[x],"print_urls":False}
        print(arguments)
        googleImageConverter(arguments)    
      
       
      ans = False    
    elif option !="":
      print("\n Not Valid Choice Try again") 


