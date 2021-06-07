# ImSearch Image Search Engine

An implementation of image search engine.

# Front End Setup
Navigate to the client folder, then:

Make sure node.js is installed then fun the following commands:
```
npm install
npm start
```
Then copy all the images (make sure it is the VALIDATION dataset and of the Open Images dataset) to the ```public``` folder.
# Back end Setup
Navigate to the server folder, then:

Make sure ```virtualenv``` is installed, then
```
virtual venv
venv\Scripts\activate
```
After that, simply the following to install dependencies:

```
pip install -r requirements.txt
```
Then use the following script to run the server:
```
cd imsearch
python manage.py runserver
```

NOTE: 
- The current program runs on the validation set of the Open Images Dataset.
- This program relies on Google Cloud, possible VPN use may be needed/