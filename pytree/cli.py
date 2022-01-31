# Standard library imports
import argparse
from email.policy import default
import pathlib
import sys

# allows us to set a version
from . import __version__
# takes our DirectoryTree package from pytree
from .pytree import DirectoryTree

def main():
    args = parse_cmd_line_arguments()
    # turns the root directory into a path object
    root_dir = pathlib.Path(args.root_dir)
    # checks to see if root directory path object is valid
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist.")
        sys.exit()
    # creates the DirectoryTree object with the root directory root_dir
    # then generates the tree from our import into the command line
    # the dir_only arguement will be passed if -d or --dir-only is provided
    # at the CLI argument
    # also added the output file as an argument that could be taken
    tree = DirectoryTree(
        root_dir, dir_only=args.dir_only, output_file=args.output_file
        )
    tree.generate()

def parse_cmd_line_arguments():
    # ArgumentParser handles the command name, a description and an epilog phrase
    # to be used when the help function is used in this program.
    parser = argparse.ArgumentParser(
        prog="pytree",
        description="PyTree, a command line directory tree generator built in Python",
        epilog="Thank you for using PyTree!"
    )
    # assigns the __version__ variable to be used with the parsers version attribute
    parser.version = f"PyTree v{__version__}"
    # this is an optional argument, handling -v and --version to display the version attribute
    parser.add_argument("-v", "--version", action="version")
    # This argument is for if the user wants to generate a directory tree
    # that only displays other directories
    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="Generate a directory-only tree",
    )

    parser.add_argument(
        # root_dir is a positional argument, it holds the directory path as the starting point
        # for this argument, we have four arguments
        "root_dir",
        # metavar is the name of the argument in usage messages
        metavar="ROOT_DIR",
        # nargs defines the number of values that can be taken as arguments
        # the tree generator can only take one directroy path, so we use ? as the value
        nargs="?",
        # default provides a default valiue for the argument, . sets the current directory
        # as the default root directory
        default=".",
        # this explains the above argument
        help="Generate a full directory tree starting at ROOT_DIR",
    )

    parser.add_argument(
        # these arguments are to create or provide an output file
        # if you want an alternative output file you must specify after 
        # using one of the two following tags
        "-o",
        "--output-file",
        metavar="OUTPUT_FILE",
        nargs="?",
        default=sys.stdout,
        help="Generates a full directory tree and saves it to a file. For alternative output files, specify the path in the command.",
    )
#
#   parser.add_argument(
 #       "-a",
  #      "--add-hidden",
   #     action="store_true",
    #    help="Generates directory tree with hidden files included.",
    #)
    # this parses the above arguments using .parse_args()
    # this returns a Namespace object with all arguments and can be accessed with .
    return parser.parse_args()