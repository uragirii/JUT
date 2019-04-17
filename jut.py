import click



@click.group(invoke_without_command = True)
def cli():
    click.clear()
    click.secho("="*25, fg="green")
    click.secho("\nThis is development version.Please bear for any mistakes", fg="red")
    click.secho("\nIf you find any error or bug please mail me at \n\t mldata.apoorv@gmail.com\n", fg="red")
    click.secho("="*25, fg="green")
    click.pause("(Press any key to continue)")
    click.clear()


@cli.command()
def init():
    """
    This initializes project and asks you the project parameters
    """
    click.echo("This utility will walk you through creating your `PROJECT.md` file.\n"
               "It only covers the basic data for the project and tries to guess sensible defaults")

    click.echo("\n\nPress ^C to quit")
    # todo: implement ^C to quit


@cli.command()
@click.option('--tag', '-t', help="Name of the tag to be shown", required = False)
def show(tag):
    """
    Displays the comments  or tags
    """
    # Search and use pager by click
    pass


@cli.command()
def add():
    """
    Adds new comments or tagged comment
    """
    pass
