![Python 3.9.5](https://img.shields.io/badge/Python-3.9.5-blue.svg)
![NumpyMatplotlib](https://img.shields.io/badge/Dependencie-Numpy|Matplotlib-green.svg)


# M2 DLAD Mathematics Project


## Hodgkin_Huxley_Model project

* This project aims to implement the Hodgkin Huxley-Model
* The programming language used is python.


## Hodgkin_Huxley_Model

    *The Hodgkin-Huxley model is a mathematical model describing action potentials of neurons. 
     It is composed of nonlinear differential equations that approximate the electrical characteristics of excitable cells. 
     
    *The Hodgkin Huxley Model tracks conductances of 3 channels, depending on time and voltage,while keeping electrical potential of the membrane at a fixed value.
    
    * The 3 channels are : Potassium channel, Sodium channel and Leak channel
    
### Dependencies 

* This project uses python3, if your python version is not update please write the following command in your terminal.

```{}
sudo apt update
sudo apt -y upgrade
python3 -V
```

* The project uses matplotlib and numpy, if you don't have these packages, you can download them with the following commands.
```{}
sudo apt-get install python3-matplotlib
sudo apt install python3-numpy
```

### Files content

* HH_EF_KH_model.py : contains the classes of the model 
* HH_EF_KH_controller.py : contains the simulations 

### Launch the program (Command line)
* clone the repository Hodgkin_Huxley_Model, and move to the directory Hodgkin_Huxley_Model. 
```{}
git clone https://github.com/Elise-11/Hodgkin_Huxley_Model.git
cd Algo_project_final/Algo_project
```
* To launch the program write the following command

```{}
python3 HH_EF_KH_controller.py
```

### Simulations Examples 

### Equilibrium 

### Limits 

###Fitzhugh-Nagumo Model


