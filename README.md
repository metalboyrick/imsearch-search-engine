# ImSearch Image Search Engine

An implementation of image search engine.

# Front End Setup
Make sure node.js is installed then fun the following commands:
```
npm install
npm start
```
Then copy all the images (make sure it is the VALIDATION dataset and of the Open Images dataset) to the ```public``` folder.
# Back end Setup

Make sure ```pipenv``` is installed, if not, use:
```
pip install pipenv
```
After that, simply the following to install dependencies:

```
pipenv install
```
Then use the following script to run the server:
```
pipenv shell
cd imsearch
python manage.py runserver
```

NOTE: the current program runs on the validation set of the Open Images Dataset.