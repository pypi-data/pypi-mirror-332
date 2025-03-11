import os
import subprocess
import yaml
from pathlib import Path
import shutil
import hvac

# Change the working directory to /root/algo
os.chdir("/root/algo")
print(f"Current working directory: {os.getcwd()}")

# Configuration Files and Secrets
config_file = "config.yaml"  # Update with your actual config path
secret_key_file = "secret.key"
project_private_key_file = "project_private.key"

# Step 1: Install Dependencies
def install_dependencies():
    dependencies = [
        "cryptography", "pyyaml", "azure-storage-blob", "auth0-python",
        "python-dateutil", "sseclient", "jupyter", "nbconvert", "pipreqs"
    ]

    wheel_url = "https://stusebkstoragesdk.blob.core.windows.net/escrowaisdk/dist/dev/EscrowAICI-0.1.5-py3-none-any.whl"
    wheel_file = "EscrowAICI-0.1.5-py3-none-any.whl"

    try:
        print("Installing dependencies...")
        subprocess.run(["pip", "install", "--upgrade", "pip"] + dependencies, check=True, stderr=subprocess.STDOUT)
        
        # Download the wheel file using curl
        print(f"Downloading wheel file from {wheel_url}...")
        subprocess.run(["curl", "-O", wheel_url], check=True, stderr=subprocess.STDOUT)
        
        # Install the wheel file
        print(f"Installing wheel file: {wheel_file}...")
        subprocess.run(["pip", "install", wheel_file], check=True, stderr=subprocess.STDOUT)
        
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies or wheel file: {e}")
        exit(1)
    
# Step 2: Convert Jupyter Notebooks in Root Directory to Python Scripts
def convert_notebooks_to_scripts():
    converted_scripts = []
    root_directory = Path('.')

    for notebook in root_directory.rglob("*.ipynb"):
        script_name = notebook.with_suffix(".py")  # Target .py script
        print(f"Converting {notebook} to {script_name}...")

        try:
            # Convert notebook to Python script
            subprocess.run(["jupyter", "nbconvert", "--to", "script", str(notebook)], check=True)
            converted_scripts.append(script_name)
        except subprocess.CalledProcessError as e:
            print(f"Error converting {notebook}: {e}")
            continue

    print("All notebooks converted.")
    return converted_scripts

# Step 3: Generate requirements.txt from Converted Scripts
def generate_requirements(converted_scripts, temp_folder="temp_py_files"):
    temp_folder = Path(temp_folder)

    # Step 4.1: Create temporary folder and copy scripts there
    if temp_folder.exists():
        shutil.rmtree(temp_folder)  # Clean up if folder exists
    temp_folder.mkdir(parents=True, exist_ok=True)

    print(f"Copying scripts to temporary folder: {temp_folder}")
    for script in Path('.').rglob("*.py"):
        destination = temp_folder / script.name
        if script.resolve() != destination.resolve():  # Check if source and destination are different
            shutil.copy(script, destination)

    # Step 4.2: Run pipreqs to generate requirements.txt
    print("Running pipreqs to generate requirements.txt...")
    subprocess.run(["pipreqs", str(temp_folder), "--force"], check=True)

    # Step 4.3: Move requirements.txt to root
    shutil.move(temp_folder / "requirements.txt", "./requirements.txt")

    # Step 4.4: Add ipython manually to requirements.txt
    requirements_path = Path("./requirements.txt")
    with open(requirements_path, "r") as f:
        requirements = f.read()

    with open(requirements_path, "w") as f:
        f.write(requirements)
        if "ipython" not in requirements:
            f.write("\nipython\n")

        # Add nbconvert if missing
        if "nbconvert" not in requirements:
            f.write("\nnbconvert\n")

    print("requirements.txt updated with ipython.")

    print("requirements.txt generated.")
    shutil.rmtree(temp_folder)
    print("Temporary folder cleaned up.")

# Step 4: Generate run.sh Script
def generate_run_script():
    print("Loading entrypoint from config.yaml...")
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
        entrypoint = config.get("entrypoint", "run.py")

    run_script = "run.sh"
    print("Generating run.sh script...")
    with open(run_script, "w") as f:
        f.write("#!/bin/sh\n\n")
        f.write(f"ipython {entrypoint}\n")
    os.chmod(run_script, 0o755)  # Make it executable
    print("run.sh script generated and made executable.")

# Step 5: Generate Dockerfile
def generate_dockerfile():
    dockerfile_content = """FROM python:3.12-slim as bkstart

WORKDIR /app

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt  .

RUN pip install -U pip setuptools uv && uv pip install -r requirements.txt --python `which python`

### BEEKEEPER START LOGIC ENDS HERE ###

############################################################################################

### YOUR DOCKERFILE STEPS BEGIN BELOW
FROM python:3.12-slim

WORKDIR /app

COPY --from=bkstart /opt/venv /opt/venv

COPY . .

ENV PATH="/opt/venv/bin:$PATH"

RUN echo $ENV

# Make the run.sh script executable
RUN chmod +x run.sh

# set the start command
ENTRYPOINT ["./run.sh"]
"""
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)
    print("Dockerfile generated.")

# Step 6: Add 'ipython' Import to Entrypoint File
def add_ipython_to_entrypoint():
    print("Ensuring 'ipython' is imported in the entrypoint file...")
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
        entrypoint = config.get("entrypoint", "run.py")

    # Check if the entrypoint file exists
    entrypoint_path = Path(entrypoint)
    if not entrypoint_path.exists():
        print(f"Entrypoint file '{entrypoint}' not found. Please verify the config.")
        exit(1)

    # Add 'import ipython' if not already present
    with open(entrypoint_path, "r") as f:
        lines = f.readlines()

    if not any("import IPython" in line for line in lines):
        print(f"'ipython' not found in {entrypoint}. Adding it now...")
        with open(entrypoint_path, "w") as f:
            f.write("import IPython\n")  # Add the import at the top
            f.writelines(lines)
    else:
        print(f"'ipython' is already imported in {entrypoint}.")

    print(f"'ipython' import ensured in {entrypoint}.")


# Step 7: Load Secrets and Configurations
def load_config_and_secrets():
    try:
        # Step 1: Load project and organization IDs from config.yaml
        print("Loading project and organization IDs from config.yaml...")
        with open(config_file, "r") as file:
            config = yaml.safe_load(file)
        project_id = config.get("BEEKEEPER_PROJECT_ID")
        organization_id = config.get("BEEKEEPER_ORGANIZATION_ID")

        if not project_id or not organization_id:
            raise ValueError("Missing BEEKEEPER_PROJECT_ID or BEEKEEPER_ORGANIZATION_ID in config.yaml.")

        # Step 2: Connect to Vault and fetch secrets
        print("Connecting to HashiCorp Vault...")
        client = hvac.Client(url='http://127.0.0.1:8200')

        # Authenticate with Vault (use token securely, e.g., from environment variable)
        #client.token = 'hvs.v1qcRGSufqpj3QQL9BRj6WY4'  # Replace with secure method
        client.token = os.getenv("VAULT_TOKEN")
        print(client.token)
        print(os.environ)

        print("Reading secrets from Vault...")
        secrets = client.secrets.kv.v2.read_secret_version(path='mysecrets')

        # Extract secrets
        secret_key = secrets['data']['data']['secret_key']
        project_private_key = secrets['data']['data']['project_private_key']

        print("Configuration and secrets successfully loaded.")

        # Return combined configuration and secrets
        return {
            "CONTENT_ENCRYPTION_KEY": secret_key,
            "PROJECT_PRIVATE_KEY": project_private_key,
            "BEEKEEPER_PROJECT_ID": project_id,
            "BEEKEEPER_ORGANIZATION_ID": organization_id,
            "BEEKEEPER_ENVIRONMENT": "tst"
        }

    except Exception as e:
        print(f"Error loading configuration or secrets: {e}")
        raise

# Step 8: Encrypt Files and Upload
def encrypt_and_upload(secrets):
    repo_name = "algocode"
    folder_path = f"files/{repo_name}"
    os.makedirs(folder_path, exist_ok=True)
    
    print("Preparing files for upload...")
    subprocess.run(["rsync", "-av", "--exclude", ".git", "--exclude", "files", ".", folder_path], check=True)
    
    print("Encrypting and uploading files...")
    subprocess.run([
        "escrowai", folder_path,
        "--algorithm_type", "training",
        "--algorithm_name", "Wine Model",
        "--algorithm_description", "Testing algo description",
        "--version_tag", "v-training-algo"
    ], env={
        **os.environ,  # Pass current environment variables
        "CONTENT_ENCRYPTION_KEY": secrets["CONTENT_ENCRYPTION_KEY"],
        "PROJECT_PRIVATE_KEY": secrets["PROJECT_PRIVATE_KEY"],
        "BEEKEEPER_PROJECT_ID": secrets["BEEKEEPER_PROJECT_ID"],
        "BEEKEEPER_ORGANIZATION_ID": secrets["BEEKEEPER_ORGANIZATION_ID"],
        "BEEKEEPER_ENVIRONMENT": secrets["BEEKEEPER_ENVIRONMENT"]
    }, check=True)
    print("Encryption and upload complete.")

# Step 9: Clean up
def cleanup():
    print("Cleaning up temporary files...")
    subprocess.run(["rm", "-rf", "files/"], check=True)
    print("Clean up complete.")

# Main Execution
if __name__ == "__main__":
    install_dependencies()
    converted_scripts = convert_notebooks_to_scripts()
    generate_requirements(converted_scripts)
    generate_run_script()
    generate_dockerfile()
    add_ipython_to_entrypoint ()
    secrets = load_config_and_secrets()
    encrypt_and_upload(secrets)
    cleanup()
