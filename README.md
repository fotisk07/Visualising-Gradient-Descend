# Visualising Gradient Descend

A 2d Visualisation of the Gradient Descend Algorithm, with and without momentum, frequently encountered in the field of Deep Learning

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
The Code is written in Python 3.6.5 . If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. 

To install pip run in the command Line
```
python -m ensurepip -- default-pip
``` 
to upgrade it 
```
python -m pip install -- upgrade pip setuptools wheel
```
to upgrade Python
```
pip install python -- upgrade
```
Additional Packages that are required are: 
- [Numpy](http://www.numpy.org/) 
- [MatplotLib](https://matplotlib.org/)

You can donwload them using [pip](https://pypi.org/project/pip/)
```
pip install numpy matplotlib
```
or using [conda](https://anaconda.org/anaconda/python)
```
conda install numpy matplotlib
```

## Usage
* Run the Visualisation with ```2d.py```
  * Basic Usage : ```python 2d.py```
  * Prints out a matplotlib figure 
  * Options:
    * Use a momentum enabled GD: ```python 2d.py momentum```
    * Set hyperparameters: ```python 2d.py momentum --lr 0.001 --gamma 120 --epochs 20 ```
    * Choose the size of the figure: ```python 2d.py --window 300```

## Using different functions

If you want to see how the algorithm behaves in different kinds of functions you have to modify the source code. More specifically in ```futils.py``` line 28 you need to specify the function you want to use and in line 15 to specify it's derivative. Also in line 44 you need to change the command np.square to np.function_you_are_using. Have fun!


## Contributing

Please read [CONTRIBUTING.md](https://github.com/fotisk07/Visualising-Gradient-Descend/blob/master/CONTRIBUTING) for the process for submitting pull requests. .g

## Authors

* **Fotios Kapotos** - *Initial work* 

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/fotisk07/Visualising-Gradient-Descend/blob/master/LICENSE) file for details

