# `pyenv` and `Python Virtual Environments`

## Link: https://k0nze.dev/posts/install-pyenv-venv-vscode

## Debian and Ubuntu

__Instructions to setup your virtual environment using pyenv on Debian/Ubuntu:__

1. Install the necessary changes with this command:
    ```sh
    sudo apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
    git
    ```

3. Install pyenv:
    ```sh
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    ```

4. Add the pyenv to your $PATH (if you use a different shell than bash you have to change ~/.bashrc accordingly):
   ```sh
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
    ```

5. Install Python Version 3.10.9:
    ```sh
    pyenv install 3.10.9
    ```

7. Clone this repository:
    ```sh
    git clone https://github.com/GeorgiosIoannouCoder/fervi.git
    ```

8. Navigate to the cloned repository folder:
    ```sh
    cd fervi
    ```

10. Use the installed Python version in the cloned repository folder:
    ```sh
    pyenv local 3.10.9
    ```

11. Create virtual environment in the cloned repository folder:
    ```sh
    python -m venv .fervi-venv
    ```

12. Activate the virtual environment:
    ```sh
    source .fervi-venv/bin/activate
    ```

13. Install the dependencies listed in the requirements.txt file:
    ```sh
    pip install -r requirements.txt
    ```

14. Install ipykernel:
    ```sh
    pip install ipykernel
    ```

15. Install Jupyter Notebook:
    ```sh
    pip install jupyter notebook
    ```

16. Add the kernel of the virtual environment in the Jupyter Notebook:
    ```sh
    ipython kernel install --user --name=.fervi-venv
    ```

17. Run the Jupyter Notebook:
    ```sh
    jupyter notebook
    ```

18. Select the `.fervi-venv` kernel to run the Jupyter Notebook.

19. Run Flask app:
    ```sh
    python app.py
    ```

## Windows

__Instructions to setup your virtual environment using pyenv on Microsoft Windows:__

1. Install pyenv:
    
    1.1 Download the zip file of the following GitHub repository:
          https://github.com/pyenv-win/pyenv-win
    
    1.2 Create a new folder .pyenv in your user folder with the name .pyenv by typing the following command in the Windows PowerShell:
    ```sh
    mkdir $HOME/.pyenv
    ```

    1.3 Extract the ZIP-archive in your downloads folder and copy the pyenv-win folder and the .version file from the pyenv-win-master folder into the newly created .pyenv folder in your user folder.
    
    1.4 Set the environment variables PYENV and PYENV_HOME that point to the installation folder:
    ```sh
    [System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
    [System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
    ```
    
    1.5 Add the bin folder to the PATH variable such that pyenv can be found when using the command line:
    ```sh
    [System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
    ```
    
    1.6 Close the current Windows PowerShell.
    
    1.7 Start a new Windows PowerShell with __admin__ privileges by right-clicking on the Windows PowerShell icon in the start menu and choose Run as administrator.
    
    1.8 Enter the following command into the PowerShell to enable the execution of scripts (press __A__ to choose Yes to ALL):
    ```sh
    Set-ExecutionPolicy unrestricted
    ```
    
    1.9 Close the current Windows PowerShell.
    
    1.10 Start a new Windows PowerShell.
    
    1.11 Type the following command to make sure that pyenv has been installed successfully:
    ```sh
    pyenv
    ```
    
    1.12 If you encounter a security warning from where you have to choose if you want to run pyenv you can disable this warning by “unblocking” the pyenv script with the following command:
    ```sh
    Unblock-File $HOME/.pyenv/pyenv-win/bin/pyenv.ps1
    ```

2. Open a new command line/terminal.

3. Install Python Version 3.10.9:
    ```sh
    pyenv install 3.10.9
    ```

4. Clone this repository:
    ```sh
    git clone https://github.com/GeorgiosIoannouCoder/fervi.git
    ```

5. Navigate to the cloned repository folder:
    ```sh
    cd fervi
    ```

6. Use the installed Python version in the cloned repository folder:
    ```sh
    pyenv local 3.10.9
    ```

7. Create virtual environment in the cloned repository folder:
    ```sh
    python -m venv .fervi-venv
    ```

8. Activate the virtual environment:
    ```sh
    .\.fervi-venv\Scripts\activate
    ```

9.  Install the dependencies listed in the requirements.txt file:
    ```sh
    pip install -r requirements.txt
    ```

10. Install ipykernel:
    ```sh
    pip install ipykernel
    ```

11. Install Jupyter Notebook:
    ```sh
    pip install jupyter notebook
    ```

12. Add the kernel of the virtual environment in the Jupyter Notebook:
    ```sh
    ipython kernel install --user --name=.fervi-venv
    ```

13. Run the Jupyter Notebook:
    ```sh
    jupyter notebook
    ```

14. Select the `.fervi-venv` kernel to run the Jupyter Notebook.

15. Run Flask app:
    ```sh
    python app.py
    ```

## macOS

__Instructions to setup your virtual environment using pyenv on macOS:__

1. Install Homebrew:
    Documentation found at: https://brew.sh/

2. Install pyenv:
    ```sh
    xcode-select --install
    brew install openssl readline sqlite3 xz zlib
    brew update
    brew install pyenv
    ```

3. Add the pyenv to your $PATH (if you are not using zsh as a shell, you have to change ~/.zshrc accordingly):
    ```
    echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
    ```

4. Install Python Version 3.10.9:
    ```sh
    pyenv install 3.10.9
    ```

5. Clone this repository:
    ```sh
    git clone https://github.com/GeorgiosIoannouCoder/fervi.git
    ```

6. Navigate to the cloned repository folder:
    ```sh
    cd fervi
    ```

7. Use the installed Python version in the cloned repository folder:
    ```sh
    pyenv local 3.10.9
    ```

8. Create virtual environment in the cloned repository folder:
    ```sh
    python -m venv .fervi-venv
    ```

9.  Activate the virtual environment:
    ```sh
    source .fervi-venv/bin/activate
    ```

10. Install the dependencies listed in the requirements.txt file:
    ```sh
    pip install -r requirements.txt
    ```

11. Install ipykernel:
    ```sh
    pip install ipykernel
    ```

12. Install Jupyter Notebook:
    ```sh
    pip install jupyter notebook
    ```

13. Add the kernel of the virtual environment in the Jupyter Notebook:
    ```sh
    ipython kernel install --user --name=.fervi-venv
    ```

14. Run the Jupyter Notebook:
    ```sh
    jupyter notebook
    ```

15. Select the .fervi-venv kernel to run the Jupyter Notebook.

16. Run Flask app:
    ```sh
    python app.py
    ```
