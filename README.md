# Bollywood-Person-Classifier

This is a python Classification project with backend as well as frontend, the backend was done in python while frontend was done in HTML, js and css, and was joined using Flask.
<br>The dataset was taken from kaggle, link is: https://www.kaggle.com/havingfun/100-bollywood-celebrity-faces which contains images of 100 bollywood actors and actresses and contains around 100 photos of each individual, 
<br>I then cropped out only the faces in those photos and chose only 1 photo of each individual for training, which was done in the file Facial Recognition.ipynb and the encoded the features of each individual in a list named encoded_list and then saved it as a pickle for further use.

<br> The Flask code is written in main.py and util.py contains the code for classifying the given image.
<br> Now the html code is saved in templates folder and it needs to be done in the same way for flask to render the html code and css and js code are saved in static folder and needs to be in those specific folders only,
<br> It can be more understandable after seeing the util.py file.

<br> Frontend_image.jpg is the screenshot of how the frontend looks and we can drag and drop images to specific area to classify that image.<br>
![alt text](https://github.com/hemangmonga/Bollywood-Person-Classifier/blob/main/frontend_image.JPG?raw=true)

<br> bollywood person classifier project recording.webm contains the screen recording of my device where i have showed how this project works.
