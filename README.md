# Getting Started

## Initialising and Startup

**1. Install OpenCOR**

Download and install OpenCOR version 0.8.1 from this [link](https://opencor.ws/downloads/index.html). I recommend installing with zip/tarball in a directory where you have access and edit rights, such as ~/Desktop.

    Note: If you are not familiar with OpenCOR, you should go 
    through the OpenCOR Tutorial before starting this

    Download the OpenCOR tutorial, which is a comprehensive 
    tutorial including many examples: [OpenCOR Tutorial](https://tutorial-on-cellml-opencor-and-pmr.readthedocs.io/en/latest/_downloads/d271cfcef7e288704c61320e64d77e2d/OpenCOR-Tutorial-v17.pdf).

**2. Clone the project**

Clone the tutorial from the [GitHub repository](https://github.com/FinbarArgus/OpenCOR_python_tutorial).

    If you have not worked with git and GitHub, firstly download and 
    install git, and then open the terminal and navigate (with terminal 
    in Linux/Mac or gitbash in Windows) to a directory where you want the 
    repository to be. Then write these commands to clone the project on your pc:

    - `git clone https://github.com/FinbarArgus/circulatory_autogen`


## Directory Definition

In this tutorial, we define the **working_dir** as the directory where the Github Circulatory Autogen project has been cloned. For example, on our computer, this directory is as below:

`[working_dir]: ~/Documents/git_projects/Circulatory_autogen`

Also, the OpenCOR directory is needed for installing the necessary python libraries, which we defined as the **OpenCOR_dir**, e.g.:

`[OpenCOR_dir]: ~/Desktop/OpenCOR-0-8-1-Linux/`

## Setting up your python path

Open `[working_dir]/opencor_pythonshell_path.sh` file and change the `opencor_pythonshell_path` to the directory of pythonshell in the **OpenCOR_dir**: 

#"Linux and Mac"
        ```
        opencor_pythonshell_path=`<OpenCOR_dir>/pythonshell`.
        ```

# "Windows"
        ```
        opencor_pythonshell_path=`C:\<OpenCOR_dir>\pythonshell.bat`.
        
        Note that the windows path conventions need to be used with C: and "\ rather than "/".
        ```

#Note: 

  If you want to use an ide, you have to set your python path to the same as the opencor_pythonshell_path above
  If you're on Windows, you should download gitbash from [here](https://git-scm.com/downloads) so that you can run the bash scripts. 

