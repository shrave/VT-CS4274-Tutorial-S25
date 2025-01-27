# VT CS4274 - Spring 2025: Hands-on Tutorial

Steps for for VT CS4274 (Spring 2025) hands-on tutorial and practical exercises.

## 1. Login to the Remote Server

To log into the remote server, use the `ssh` command from your terminal or SSH client.

### Install Visual Studio Code (VSCode)

We recommend using Visual Studio Code (VSCode) as your code editor for remote development. It’s lightweight, powerful, and supports remote server connections.

1. **Download and install VSCode**:  
   - Visit the [Visual Studio Code download page](https://code.visualstudio.com/) to download and install VSCode for your operating system.

2. **Install the Remote - SSH extension**:
   The Remote - SSH extension allows you to open a remote folder on your server directly in VSCode.

   - In VSCode, go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
   - Search for **Remote - SSH** and click **Install**.
   - Alternatively, you can directly access the extension [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh).

### Connect to the Remote Server

1. Once VSCode and the extension are installed, press **Ctrl+Shift+P** (Windows/Linux) or **Cmd+Shift+P** (macOS) to open the Command Palette in VSCode.

2. Type `Remote-SSH: Connect to Host...` and hit Enter.

3. Enter your remote server details in the format `username@glogin.vt.cs.edu` and press Enter.

   - Replace `username` with your hokie ID.
   - Replace `glogin.cs.vt.edu` with the server’s IP address.

   You may be prompted for a password or private key for authentication.

---

This will set up your VSCode environment to work directly with the remote server, enabling you to run code, install dependencies, and more.

## 2. Install Anaconda on the Remote Server

Follow these steps to install Anaconda on the remote server.

### 1. Download the Anaconda installer

Use the `wget` command to download the Anaconda installer script.

   ```bash
   wget https://repo.anaconda.com/archive/Anaconda3-2023.03-Linux-x86_64.sh
```

### 2. Run the Anaconda installer
  ```bash
chmod +x Anaconda3-2023.03-Linux-x86_64.sh
./Anaconda3-2023.03-Linux-x86_64.sh
```

### 3. Follow the Installation prompts
During the installation process, you’ll be prompted to review and accept the terms and conditions. Follow the instructions on the screen and press Enter to accept the default installation location.

### 4. Initialize Anaconda
After the installation is complete, initialize Anaconda to set up the environment and configure the shell:
```bash
source ~/.bashrc
```

### 5. Verify the Installation

```bash
conda --version
```
---

## 3. Create a new Conda environment for Huggingface

To create a new Conda environment, use the following command in your terminal or remote server:

### 1. Create the Conda environment

```bash
conda create --name huggingface_env python=3.8
```

### 2. Activate the Conda environment

```bash
source activate huggingface_env
```

### 3. Install the required packages

```bash
pip install torch diffusers transformers datasets accelerate
```
---

## 4. Tutorial 1: Foundation models to Generate Synthetic Images

[Prompting Stable Diffusion to Generate an Image](https://github.com/shrave/VT-CS4274-Tutorial-S25/blob/main/Text-to-Image.py)

## 5. Tutorial 2: Foundation models to Modify Images

[Prompting Stable Diffusion with an Image-Text pair to Edit Image](https://github.com/shrave/VT-CS4274-Tutorial-S25/blob/main/modify-Image.py)

## 6. Tutorial 3: Foundation models to Generate Synthetic Text

[Prompting GPT-2 to Generate Text](https://github.com/shrave/VT-CS4274-Tutorial-S25/blob/main/Text-to-Text.py)



## 7. Tutorial 4: Jailbreaking Large Language Models (LLMs)

[Try Any Foundation Model online](https://lmarena.ai) **(Demo)**

---

## 8. Using Other Models on Hugging Face

In order to use other models(ex. Llama-3, LLaVa, etc) available on Hugging Face, you will need to create an account, generate an access token, and add it to your console. Follow the steps below:

### 1. Create an Account on Hugging Face

- Go to [Hugging Face](https://huggingface.co) and click on **Sign Up** in the top-right corner.
- Fill out the required details to create your account.

### 2. Generate an Access Token

- After signing in, navigate to your **Account Settings** by clicking on your profile icon in the top-right corner.
- Select **Access Tokens** from the menu.
- Click on **New token**, provide a name, and select the desired permissions (e.g., read, write).
- Click **Generate**. Your new access token will appear.

### 3. Add the Token to Your Console

- Once you have your token, open your terminal or console.
- Run the following command to log in to Hugging Face:

  ```bash
  huggingface-cli login
  ```

