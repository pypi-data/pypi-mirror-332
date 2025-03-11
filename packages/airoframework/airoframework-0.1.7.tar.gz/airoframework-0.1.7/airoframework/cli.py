import os
import shutil
import sys
import subprocess

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "template")

REQUIRED_PACKAGES = ["aiogram", "alembic", "pyyaml", "sqlalchemy"]

DEFAULT_MODEL = """from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    username = Column(String, unique=True, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
"""

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
    env_content = "DATABASE_URL=sqlite:///database.db\nBOT_TOKEN=\n"

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

    # Create database directory and models file
    os.makedirs("database", exist_ok=True)

    model_path = "database/models.py"
    if not os.path.exists(model_path):
        print("🛠️  Creating default user model...")
        with open(model_path, "w") as f:
            f.write(DEFAULT_MODEL)

    # Create database/database.py
    db_path = "database/database.py"
    if not os.path.exists(db_path):
        print("🛠️  Creating database config file...")
        with open(db_path, "w") as f:
            f.write(
                'from sqlalchemy import create_engine\n'
                'from sqlalchemy.orm import sessionmaker\n'
                'from database.models import Base\n'
                'import os\n\n'
                'DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")\n'
                'engine = create_engine(DATABASE_URL)\n'
                'SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)\n\n'
                'def init_db():\n'
                '    Base.metadata.create_all(bind=engine)\n'
            )

    # Initialize Alembic
    print("⚙️  Initializing Alembic...")
    subprocess.run(["alembic", "init", "migrations"], check=True)

    # Modify alembic/env.py to import database models
    env_path = "migrations/env.py"
    with open(env_path, "r") as f:
        env_data = f.read()

    # Add `import database.database as db`
    env_data = env_data.replace(
        "from alembic import context",
        "from database.models import Base\nfrom alembic import context"
    )

    # Replace the `target_metadata` line with the correct metadata
    env_data = env_data.replace(
        "target_metadata = None",
        "target_metadata = Base.metadata"
    )

    with open(env_path, "w") as f:
        f.write(env_data)

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
