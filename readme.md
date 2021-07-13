# Setting Up The Project

## Installation
There are several ways to run your own instance of the project depending on your OS:

### Dependencies:
1. Python 3.6^: [Refer to install on linux](https://docs.python.org/3/using/unix.html) || [Refer to install on Windows](https://docs.python.org/3/using/windows.html)
2. Pip
3. Streamlit

 ### Windows:

- Install Streamlit on Windows, Streamlit’s officially-supported environment manager on Windows is [Anaconda Navigator.](https://docs.anaconda.com/anaconda/navigator/)
    * Install Anaconda, if you don’t have Anaconda install yet, follow the steps provided on the [Anaconda installation page.](https://docs.anaconda.com/anaconda/install/windows/)
    * Create a new environment with Streamlit:
        - Next you’ll need to set up your environment
            1. Follow the steps provided by Anaconda to set up and manage your environment using the Anaconda Navigator.
            2. Select the “▶” icon next to your new environment. Then select “Open terminal”:
                      ![](https://i.stack.imgur.com/EiiFc.png)
            3. In the terminal that appears, type:
                      `pip install streamlit`
            4. Test that the installation worked:
                      `streamlit hello`
            5. Streamlit’s Hello app should appear in a new tab in your web browser!
            6. Run  `pip install nltk`
            7. Run  `pip install scikit-learn`(depends)
            8. Finally `streamlit run app.py`
           
 ### Linux / macOS:
 
 - Install pip. 
     * On a macOS: `sudo easy_install pip` On Ubuntu with Python 3: `sudo apt-get install python3-pip`
     * Install pipenv. `pip3 install pipenv`
     * Create a new virtual environment for python:
         - Next you’ll need to set up your environment
             1. the recommended way to create a virtual environment is to use the venv module.
                      `sudo apt install python3-venv`
             2. Switch to the directory where you would like to store your Python 3 virtual environments. Within the directory run the following command to create your new virtual environment: `python3 -m venv my-project-env`
             3. To start using this virtual environment, you need to activate it by running the activate script: `source my-project-env/bin/activate`
             4. Once activated, the virtual environment’s bin directory will be added at the beginning of the $PATH variable. Also your shell’s prompt will change and it will show the name of the virtual environment you’re currently using. In our case that is my-project-env:
             ``` 
             $ source my-project-env/bin/activate
             (my-project-env) $ 
             
             ```
             5. Now that the virtual environment is activated, we can start installing, upgrading, and removing packages using pip.
             6. In the terminal that appears, type:
                      `pip install streamlit`
             7. Test that the installation worked:
                      `streamlit hello`
             8. Streamlit’s Hello app should appear in a new tab in your web browser!
             9. Run  `pip install nltk`
             10. Run  `pip install scikit-learn`(depends)
             11. Finally `streamlit run app.py`


