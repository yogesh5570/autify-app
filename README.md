# Autify

A python script to scrape, clone websites and collect metadata containing number of images, total links and last fetch time in UTC. 

### Description

In this script we are cloning the complete webpage with images and getting all links. We are storing the complete webpage with images and other files in clone directory, all the metadata are storing in a metadata.json file with object key as the website url and there is one more html file with the same name as url which is saving the html code for the given url. To run the script, you can directly add websites separated by a blankspace right after calling app.py file and if you add --metadata before websites, it will fetch metadata of those websites.

### Getting Started

To run this script on docker-
1. Create a docker image
command - docker build -t image-name .

2. Run the docker image
command - docker run image-name

3. Go to Docker and open terminal for our running image

4. In terminal you can use the following commands to run our script
- python app.py https://www.google.com https://autify.com
This will fetch all metadata and clone websites

- python app.py --metadata https://www.google.com https://autify.com
This will fetch the metadata of the given websites.