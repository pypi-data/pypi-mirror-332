import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import typer
from app.app import app
# if __name__ == "__main__":
#     app()