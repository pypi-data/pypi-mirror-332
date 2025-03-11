import os
import shutil
import sys

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "template")

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
    print("✅ Done! Navigate to your project and start coding.")
    print(f"👉 cd {project_name} && python main.py")

if __name__ == "__main__":
    create_project()
