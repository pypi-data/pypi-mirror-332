import click
import inquirer
import json
import os


TODO_FILE = 'todo.json'

def load_tasks() -> list[dict[str, str | bool]]:
    if not os.path.exists(TODO_FILE):
        return []
    
    with open(TODO_FILE, 'r') as file:
        return json.load(file)


def save_tasks(tasks: list[dict[str, str| bool]]):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


@click.group()
def cli():
    """A simple task manager"""
    pass



@click.command()
def add():
    """Add new task"""

    task: str = click.prompt("Task")
    tasks = load_tasks()
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)
    click.echo(f"Task added: {task}")


@click.command()
def list():
    """List all tasks"""

    tasks = load_tasks()

    if len(tasks) == 0:
        click.echo("No task found!")
        return
    
    for i, task in enumerate(tasks):
        status = '✅' if task.get('completed', False) else '❌'
        click.echo(f"{i}. {task.get('task')} [{status}]")


@click.command()
def complete():
    """Mark task as complete"""
    
    tasks = load_tasks()
    choices = [str(task.get('task', '')) for task in tasks if not task.get('completed')]

    if len(choices) == 0:
        click.echo("All task completed!")
        return

    questions = inquirer.List('task',
        message="Select task to mark as completed",
        choices=choices,
    )
    answers: dict[str, str] = inquirer.prompt([questions]) or {}
    
    for task in tasks:
        if task['task'] == answers['task']:
            task['completed'] = True
            break
    
    save_tasks(tasks)
    click.echo(f"""Task: "{answers['task']}" marked as completed.""")


@click.command()
def remove():
    """Remove a task"""

    tasks = load_tasks()
    choices = []
    
    for i, task in enumerate(tasks):
        status = '✅' if task.get('completed', False) else '❌'
        choices.append(f"{i}. {task.get('task')} [{status}]")

    if len(choices) == 0:
        click.echo("No task to show")
        return

    questions = inquirer.List('task',
        message="Select task to remove",
        choices=choices,
    )
    answers: dict[str, str] = inquirer.prompt([questions]) or {}


    for i, task in enumerate(choices):
        if task == answers['task']:
            removed_task = tasks.pop(i)
            click.echo(f"""Task: "{removed_task['task']}" removed.""")
            break
    
    save_tasks(tasks)



cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

if __name__ == "__main__":
    cli()
