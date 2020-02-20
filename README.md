# imageAI
We will look at an example of image processing with Convolutional Neural Network in this project.
This Neural Network may classify your images after training.
I used this package in this project :
* tensorflow
* keras
* matplotlib
* numpy
* cv2
* pickle
* random
* os

You can install with this code on your terminal:
```
pip install TheNameOfPackage
```

## Process Data
Firstly you should run dataOrganize.py
This process will organize your unprocessed images and will resize them.
When you creating a folder you need to classify the folders.

Example :

* DataFolder
  * classOne
  * classTwo
  * classThree
  * empty
  
You should create a empty class because when classifying if there is no detection the neural network will choose the this class.

After that you need to define path of your data folder.
Example:

```python
DATADIR = ".\DataFolder"

```

## Create Neural Network
When you run createModel.py the process will create a .model file and while you testing the test images you will use this file.
 
```python
history = model.fit(X, y, batch_size=64, epochs=40, validation_split=0.1)

```

In this line you can change the configs for your usage.

## Testing The Model With Images
If you want to test your model you should run the testWithImg.py

```python
CATEGORIES = ["categ1", "categ2","categ3","empty"] # categories you have. Should be in same order...
````

The CATEGORIES list item names should be in same order otherwise you can't see the true class name.
 
 ```python
 image = "path-to-sample-image" # image of sample
 ```

In this line you should define path of your test image.

## TIPS
If there is an error with file or folder you can use " \\ " instead " \ "

```
C:\\Users\\User\\Desktop\\File

```

When testing if you have an error with model file you should define name as you defined in createModel.py


this line
```python
model = tf.keras.models.load_model("MODEL_NAME.model")
```
should be same with :

```python
model.save('MODEL_NAME.model') # this line should be same with testWithImg.py
```


