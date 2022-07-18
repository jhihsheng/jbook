# jupyter-book python package
We use the python package "jupyter-book" to create the source materials. The source materials include the .md and .ipynb files.

In a linux terminal, create a conda environment and install the package

## Installation
```
conda create -n env_name python=3.8
pip install jupyter-book=0.13.0
```
```{note}
I specify these versions because currently I have tested that these versions work well in my machine.
If you want to use newer versions later for new features, you will have to do a further test. 
```
## Build a JB book
First, go to the "env_name" environment by
```
conda activate env_name
```
To create a book of the name "mybook", use
```
jupyter-book create mybook
```
, which will create a folder of the name "mybook". The source materials of the book are all in the folder.
You can use these materials to generate HTML output by
```
jupyter-book build mybook
```
Now, go into the folder, and you will find a folder "html"  at
```
mybook/_build/html
```
Click the index.html and you will see the web pages.


````{warning}
Sometimes, errors occur due to missing of some python packages.  
In this case, you can check the compiled report to see the missed packaages.
For example, I have to install matplotlib
  ``` 
  pip install matplotlib
  ```
````
