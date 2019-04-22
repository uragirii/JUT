import click
import json
import os
import datetime


class Project:

    def __init__(self, init_called=False):
        # check whether the file exits or not
        if os.path.exists('jut.json'):
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
                self.startDate = data['startDate']
        elif init_called:
            pass
        else:
            # This ensures that whenever command runs, the `jut.json` file exits.
            click.secho("\nThe project file does not exists, run  `jut init` command to create new project file"
                        "\nClosing.", fg="red")
            raise click.Abort

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
            self.tags = {}
            for tag in taglist:
                # initialize every tag as empty
                self.tags[tag] = []
            self.startDate = datetime.datetime.now().replace(microsecond=0).isoformat()
            click.echo("\nStart Date: {0}".format(self.startDate))
            self.comments = []
            self.jver = 'K'
            # now dump to json file.
            self._dump_json()
            click.secho('The `jut.json` has been successfully created', fg='green')
            # todo: after start a git prompt.

    def _dump_json(self):
        with open('jut.json', 'w') as jfile:
            json.dump(self.__dict__, jfile)

    def add_comment(self, comment):
        # Check is comment is None.
        if comment is None:
            return None

        comment_data = (str(datetime.datetime.now().replace(microsecond=0).isoformat()), comment)
        self.comments.insert(0, comment_data)
        # Now write data again.
        self._dump_json()
        click.secho("Successfully added comment {} at time {}".format(comment, comment_data[0]), fg="green")

    def add_tag(self, tag):
        # Check if tag is none, meaning value is not passed.
        if tag is None:
            return None

        tag_name, tag_msg = tag

        if not tag_name.upper() in self.tags.keys():
            # check is tag name does not exists
            choice = click.confirm("Tag Name you have entered could not be found, do you want to add the tag name?")

            if not choice:
                raise click.Abort

        tag_data = (str(datetime.datetime.now().replace(microsecond=0).isoformat()), tag_msg)
        self.tags[tag_name.upper()] = tag_data
        click.secho("Successfully added '{}' to tag '{}' at time {}".format(tag_msg, tag_name.upper(), tag_data[0]),
                    fg="green")
        self._dump_json()

    def print_proj(self):
        print(self.__dict__)


@click.group(invoke_without_command = True)
def cli():
    # click.clear()
    click.secho("="*25, fg="green")
    click.secho("\nThis is development version.Please bear for any mistakes", fg="red")
    click.secho("\nIf you find any error or bug please mail me at \n\t mldata.apoorv@gmail.com\n", fg="red")
    click.secho("="*25, fg="green")
    click.pause("(Press any key to continue)")
    # click.clear()


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
@click.option('-c', '--comment', nargs=1)
@click.option('-t', '--tag', nargs=2)
# @click.option('-tag', '--t', default="", nargs=2)
def add(comment, tag):
    """
    Adds new comments or tagged comment
    """
    new_proj = Project()
    # The initialization of class checks whether the file is present or not
    # todo: implement a faster way to write to json file. rn I'm just reading and "writing" not altering the file.
    if comment is None and tag is None:
        raise click.Abort
    else:
        # If comment is None, it will be checked by the class.
        new_proj.add_comment(comment)
        if all(tag):
            new_proj.add_tag(tag)

