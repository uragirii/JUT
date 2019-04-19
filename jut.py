import click
import json
import os
import datetime

class Project:

    def __init__(self, init_called = False):
        # check whether the file exits or not
        if init_called:
            click.echo("Init called")
        elif os.path.exists('jut.json'):
            # Read the data from json file.
            with open('jut.json') as proj_file:
                data = json.load(proj_file)
                # Read all the data.
                self.jver = data['jver']
                self.name = data['name']
                # todo: make a function to read the tags
                self.tags = data['tags']
                self.comments = data['comments']
                self.desc = data['desc']
                self.start_date = data['startDate']
        else:
            # This ensures that whenever command runs, the `jut.json` file exits.
            click.secho("\nThe project file does not exists, run  `jut init` command to create new project file"
                        "\nClosing.", fg="red")

    def __str__(self):
        return self.name

    def new_proj(self):
        if os.path.exists('jut.json'):
            click.secho("\nThe `jut.json` file already exists. see `jut --help` for more."
                        "\nClosing", fg="red")
        else:
            self.name = click.prompt("\nProject Name")
            self.desc = click.prompt("\nDescription")
            # Todo: make a license prompt and .gitignore prompt also
            click.echo("\nDefault TAG values are :"
                       "\n`TODO`, `REM`(remember), `IMP`, `FEAT`(feature), `ADV`(advanced feature")
            # todo: implement basic todo dict
            tag_choice = click.prompt("Do you want to add new tags?(yes/no)")
            taglist = ['TODO', 'REM', 'IMP', 'FEAT', 'ADV']
            if tag_choice.lower() == 'yes':
                # Add a new tag for the user.
                click.echo("\nEnter the name of tags you want to add. Enter 0 to skip.")
                while True:
                    new_tag = click.prompt("New tag name")
                    if new_tag == "0":
                        break
                    else:
                        taglist.append(new_tag.upper())
            self.tags ={}
            for tag in taglist:
                # initialize every tag as empty
                self.tags[tag] = []
            self.start_date = datetime.datetime.now().replace(microsecond=0).isoformat()
            click.echo("\nStart Date: {0}".format(self.start_date))
            self.comments = []
            self.jver = 'K'
            # now dump to json file.
            self._dump_json()
            click.secho('The `jut.json` has been successfully created', fg='green')
            # todo: after start a git prompt.

    def _dump_json(self):
        with open('jut.json','w') as jfile:
            json.dump(self.__dict__,jfile)


@click.group(invoke_without_command = True)
def cli():
    click.clear()
    click.secho("="*25, fg="green")
    click.secho("\nThis is development version.Please bear for any mistakes", fg="red")
    click.secho("\nIf you find any error or bug please mail me at \n\t mldata.apoorv@gmail.com\n", fg="red")
    click.secho("="*25, fg="green")
    click.pause("(Press any key to continue)")
    click.clear()
    # todo: !IMP call the instance of project and check whether file exists or not
    # project = Project()


@cli.command()
def init():
    """
    This initializes project and asks you the project parameters
    """
    click.echo("This utility will walk you through creating your `PROJECT.md` file.\n"
               "It only covers the basic data for the project and tries to guess sensible defaults")

    click.echo("\n\nPress ^C to quit")
    # todo: implement ^C to quit
    new_proj = Project(init_called=True)
    new_proj.new_proj()


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
