# imageAI
This repository contains basic and understandable level of a neural network example. You can understand the fundamental working mechanism of machine learning concept.
Packages used in this project:
* tensorflow
* keras
* matplotlib
* numpy
* cv2
* pickle
* random
* os

You can install packages by using the requirements text file:
```
pip install -r requirements.txt
```

## Process Data
dataOrganize.py will check your data and extract the essential data from them.

You need to create and classify your folders by considering your class names.

Example :

* DataFolder
  * classOne
  * classTwo
  * classThree
  * empty
  
empty folder will contain unclassified elements.

Insert your data folder.
Example:

```python
DATADIR = ".\DataFolder"

```

## Create Neural Network
This chunk of code optimizes your model. Different kind of settings can be performed by changing arguments.
 
```python
history = model.fit(X, y, batch_size=64, epochs=40, validation_split=0.1)

```

In this line you can change the configs according your usage.

## Testing The Model With Images
testWithImg.py used to test images. 

```python
CATEGORIES = ["classOne", "classTwo", "classThree", "empty"] # categories you have. Should be in same order...
````

The CATEGORIES list item names should be in same order otherwise you can't see the true class name.
 
 ```python
 image = "path-to-sample-image" # image of sample
 ```

In this line you should define path of your test image.

## TIPS
Windows uses the backslash "\" for seperating path elements in Python it may escape the next character so you need to use double backslash "\\"

```
C:\\Users\\User\\Folder\\File

```
or
```
\home\user\folder\file

```
Note: Different kind of solutions for path problem can be used.

Don't forget the use same model number on your operations

the name that defined in this line
```python
model = tf.keras.models.load_model("MODEL_NAME.model")
```
should be same with :

```python
model.save('MODEL_NAME.model') # this line should be same with testWithImg.py
```


