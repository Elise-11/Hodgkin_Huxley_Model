![Python 3.9.5](https://img.shields.io/badge/Python-3.9.5-blue.svg)
![NumpyMatplotlib](https://img.shields.io/badge/Dependencie-Numpy|Matplotlib-green.svg)
![Tk](https://img.shields.io/badge/Interface-Tkinter-green.svg)

# M2 DLAD Mathematics Project


## Hodgkin_Huxley_Model project

* This project aims to implement the Hodgkin Huxley-Model.
* The programming language used is python.
* the visualization of the plots of the model are done under an interactive Tkinter interface.


## Hodgkin_Huxley_Model

   * The Hodgkin-Huxley model is a mathematical model describing action potentials of neurons. 
     It is composed of nonlinear differential equations that approximate the electrical characteristics of excitable cells. 
     
   * The Hodgkin Huxley Model tracks conductances of 3 channels, depending on time and voltage,while keeping electrical potential of the membrane at a fixed value.
    
   * The 3 channels are : Potassium channel, Sodium channel and Leak channel
    
### Dependencies 

* This project uses python3.9.5, if your python version is not updated please write the following command in your terminal.

```{}
sudo apt update
sudo apt -y upgrade
python3 -V
```

* The project uses matplotlib and numpy, you can download them with the following commands.
```{}
sudo apt-get install python3-matplotlib
sudo apt install python3-numpy
```
* For the proper functioning of the GUI we need Tkinter, you can install it with the following commands.
```{}
sudo apt-get install python3-tk
```

### Files contents

* HH_EF_KH_model.py : Model' classes
* HH_EF_KH_controller.py : Model' simulation
* HH_EF_KH_view.py : interface operation

### Launch the program (Command line)
* clone the repository Hodgkin_Huxley_Model, and move to the directory Hodgkin_Huxley_Model. 
```{}
git clone https://github.com/Elise-11/Hodgkin_Huxley_Model.git
cd Hodgkin_Huxley_Model/
```
* To launch the program write the following command

```{}
python3 HH_EF_KH_view.py
```

### Simulations Examples 
Here is a typical example of a plot obtained by the interface, which represents the triggering of action potentials according to the Hodgkin Huxley model, with parameter values from Hodgkin-Huxley original paper : 

![plot](https://github.com/Elise-11/Hodgkin_Huxley_Model/blob/main/HHModel0.png)

