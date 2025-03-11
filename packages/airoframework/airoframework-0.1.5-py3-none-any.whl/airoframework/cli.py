import os
import shutil
import sys
import subprocess

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "template")

REQUIRED_PACKAGES = ["aiogram", "alembic", "pyyaml"]

def create_project():
    if len(sys.argv) < 3 or sys.argv[1] != "new":
        print("❌ Usage: airoframework new <project_name>")
        sys.exit(1)

    project_name = sys.argv[2]
    if os.path.exists(project_name):
        print(f"❌ Project '{project_name}' already exists.")
        sys.exit(1)

    print(f"📂 Creating project '{project_name}'...")
    shutil.copytree(TEMPLATE_DIR, project_name)

    # Navigate to the project directory
    os.chdir(project_name)

    # Install dependencies
    print("📦 Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install"] + REQUIRED_PACKAGES, check=True)

    # Generate requirements.txt
    print("📝 Generating requirements.txt...")
    with open("requirements.txt", "w") as f:
        for package in REQUIRED_PACKAGES:
            f.write(f"{package}\n")

    # Create .env and .env-example files
    print("🌍 Creating environment files...")
    env_content = "BOT_TOKEN=\nDATABASE_URL=\n"
    
    with open(".env", "w") as f:
        f.write(env_content)

    with open(".env-example", "w") as f:
        f.write(env_content)

    # Create .gitignore
    print("📄 Creating .gitignore...")
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*.sqlite3

# Virtual environment
.venv/
.env

# Alembic
migrations/

# OS-specific
.DS_Store
Thumbs.db
"""

    with open(".gitignore", "w") as f:
        f.write(gitignore_content)

    # Initialize Alembic
    print("⚙️  Initializing Alembic...")
    subprocess.run(["alembic", "init", "migrations"], check=True)

    # Generate initial migration
    print("📜 Generating initial migration...")
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", "Initial migration"], check=True)

    # Apply migrations
    print("🚀 Applying migrations...")
    subprocess.run(["alembic", "upgrade", "head"], check=True)

    print("✅ Done! Navigate to your project and start coding.")
    print(f"👉 cd {project_name} && python main.py")

if __name__ == "__main__":
    create_project()
