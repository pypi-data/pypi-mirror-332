import sys
import time
import typer
from rich import print,prompt
from .server_interface import Server
from .local_handler import LocalHandler
from rich.progress import Progress, SpinnerColumn, TextColumn
from graph_construction.core.graph_builder import GraphConstructor
import os

local_handler = LocalHandler()

local_handler.get_modo_config()
config = local_handler.config
server = Server(token=config.get("token",None))


def init():
    projects = []
    if config["login"]:
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
                            task = progress.add_task("[cyan]Getting projects...",total=1)
                            status,result = server.projects()
                            if status:
                                projects = result["results"]
                            progress.update(task, visible=False)
    return projects




app = typer.Typer()




@app.command(name="login",help="login to modo code")
def login():
    username = prompt.Prompt.ask("Enter your username")
    password = prompt.Prompt.ask("Enter your password",password=True)

    if username and password:
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
            task = progress.add_task("[cyan]Logging in...",total=1)
            status,result = server.login(username=username,password=password)
            if status:
                print("[green]Login successful[/green]")
                config["login"] = True
                config["token"] = result["data"]["token"]
                local_handler.save_modo_config(config)
            else:
                print(f"[red]{result}[/red]")
            progress.update(task, visible=False)
    else:
        print("Please enter username and password")

@app.command(name="init",help="Init project")
def init_project():
    projects = init()
    if not config["login"]:
        print("Please login to modo code. Run 'modo login' to login")
        return
    for project in projects:
        if os.getcwd() == project["local_path"]:
            print("You are already init this project")
            return
    
    if prompt.Confirm.ask("Are you sure to init modo code on this project?"):
        project_name = prompt.Prompt.ask("What's you project name?")
        if project_name:
            project_language = prompt.Prompt.ask("What's your common project language?",choices=["python","typescript","javascript"],show_choices=True)
            if project_language:
                with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
                    task = progress.add_task("[cyan]Generating project...",total=1)
                    status,result = server.init_project(project_name,project_language,local_path=os.getcwd())
                    if status:
                        print("[green]Project generate successfully[/green]")
                    else:
                        print(f"[red]{result}[/red]")
                        return
                    progress.update(task, visible=False)


@app.command(name="build_graph",help="Build graph of current project")
def build_graph():
    projects = init()
    project = None
    for project in projects:
        if os.getcwd() == project["local_path"]:
            project = project
    if not project:
        print("[red]You should init project first[/red]")
        return
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:                    
                    task = progress.add_task("[cyan]Generating graphes...",total=1)
                    graph_constructor = GraphConstructor(entity_id=project["id"],root=".")
                    nodes, relationships = graph_constructor.build_graph(ignores=project["ignores"].split(","))
                    print("[green]Graphes generated successfully[/green]")
                    progress.update(task, visible=False)
                    print(f"\nNodes: {len(nodes)}",f"\nRelations: {len(relationships)}")

                    task = progress.add_task("[cyan]Saveing graphes on server...",total=1)
                    status,result = server.save_graph(relationships,nodes,project["id"])
                    if status:
                        print("[green]Graph saved.[/green]")
                    else:
                        print(f"[red]{result}[/red]")
                    progress.update(task, visible=False)
                         
@app.command(name="ask_question",help="Ask question")
def ask_question():
    projects = init()
    project = None
    for project in projects:
        if os.getcwd() == project["local_path"]:
            project = project
    if not project:
        print("[red]You should init project first[/red]")
        return
    while True:
        try:
            user_input = input(">>> ")
            if user_input.strip() == "exit()":
                break
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:                    
                    task = progress.add_task("[cyan]Asking...",total=1)

                    status,result = server.ask_question(user_input.strip(),project["id"])
                    progress.update(task, visible=False)
                    if status:
                        print(f"[blue]{result['data']['ai']}[/blue]")
                    else:
                        print(f"[red]{result}[/red]")
                    
        except (KeyboardInterrupt, EOFError):
            break
    

@app.command(name="logout",help="logout from modo code")
def logout():

    if not config["login"]:
        print("You are not logged in")
        return
    
    if prompt.Confirm.ask("Are you sure to logout from modo code?"):
        config["login"] = False
        config["token"] = None
        local_handler.save_modo_config(config)
        print("You are logged out successfully")
