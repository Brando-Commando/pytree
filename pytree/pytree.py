# This file handles the constructors of the directory tree.

import os
import pathlib
from statistics import mode
import sys

PIPE = "|"
ELBOW = "|__"
TEE = "|--"
PIPE_PREFIX = "|    " 
SPACE_PREFIX = "    "


######################################
# DirectoryTree class
###################################### 

class DirectoryTree:
    def __init__(self, root_dir, dir_only=False, output_file=sys.stdout):
        # The leading _ indicates that the class is private/nonpublic and
        # will not be used outside of this file.
        # Adding the dir_only attribute here we can process the proper
        # flags at the command line
        # sys.stdout is standard output and stores the argument into the 
        # called output file
        self._output_file = output_file
        self._generator = _TreeGenerator(root_dir, dir_only)
        

    # this function creates a tree variable that builds the directory tree and 
    # loops for every entry.
    def generate(self):
        tree = self._generator.build_tree()
        # this checks to see if an output file was selected
        if self._output_file != sys.stdout:
            # These two statements will move outputs into a commented out section of a file
            # It moves the items one section to the right to fit in the start of the ''' comment
            tree.insert(0, "```")
            tree.append("```")
            # This opens and writes to the selected output file by the user
            self._output_file = open(
                self._output_file, mode="w", encoding="UTF-8"
            )
        # starts a for loop to print the diagram tree to the output tree
        with self._output_file as stream:
            for entry in tree:
                print(entry, file=stream)

######################################
# _TreeGenerator class
######################################

class _TreeGenerator:
    # This function uses the trees root directory as a nonpublic instance attribute
    # root_dir is also turned into a PATH object.
    # dir_only is an attribute to display only directory objects in the path when selected
    def __init__(self,root_dir, dir_only=False):
        self._root_dir = pathlib.Path(root_dir)
        self._dir_only = dir_only
        # This is an empty list that stores the entries shaping the diagram
        self._tree = []

    # This function creates the tree head and body. 
    def build_tree(self):
        self._tree_head()
        # This argument facilitates the entries with the root directory.
        self._tree_body(self._root_dir)
        return self._tree

    # Adds name of root directory to ._tree, then uses a PIPE to connect 
    # the root directory to the rest of the tree.
    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)


    # This function takes two arguments;
    # directory holds the path to the directory we are opening, directory
    # is a PATH object. 

    # prefix holds a prefix string that draws the tree diagram in the terminal.
    def _tree_body(self, directory, prefix=""):
        entries = self._prepare_entries(directory)
        # assigns results to entries, iterates files and subdirectories
       # entries = directory.iterdir()
        # A lambda function that checks if an entry is a file, and returns true or false
       # entries = sorted(entries, key=lambda entry: entry.is_file())
        # returns the number of entries of an object/directory
        entries_count = len(entries)
        # This is a for loop that iterates over all entries in the directory
        # enumerate() associates an index with each entry
        for index, entry in enumerate(entries):
            # defines the symbols used for connecting the diagram
            connector = ELBOW if index == entries_count - 1 else TEE
            # defines the statement that checks if an entry is a directory
            # if it is, it then used the ._add_directory path to add it
            # if not, it uses the else ._add_file path to create a file entry
            if entry.is_dir():
                if directory.name.startswith('.'):
                    return
                self._add_directory(
                    entry, index, entries_count, prefix, connector
                )
            else:
                self._add_file(entry, prefix, connector)

    def _add_directory(
        # takes five arguments
        self, directory, index, entries_count, prefix, connector
    ):
        # appends a new directroy to ._tree. each is represented with a string
        # containing a prefix, connector, name and a final seperator
        # (os.sep) means that the separator is using the OS specific separator 

        # This function will not print hidden directories yet files within will print
        if not directory.name.startswith('.'):
            self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")
        
      #  if directory.name.startswith('.'):
            
        # this updates prefix according to the index of the entry
        if index != entries_count - 1:
            prefix += PIPE_PREFIX 
        else:
            prefix += SPACE_PREFIX
        # calls ._tree_body with a new set of arguments
        self._tree_body(
            directory=directory,
            prefix=prefix,
        )
        # appends a new prefix separate of the content in current directory from the next one
        self._tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector):
    #    self._tree.append(f"{prefix}{connector} {file.name}")

        # This if function will ignore all hidden files that start with .
       if not file.name.startswith('.'):
            self._tree.append(f"{prefix}{connector} {file.name}") 

    def _prepare_entries(self, directory):
        entries = directory.iterdir()
        # checks if we are generating a directory only tree and 
        # selects only dir entries
        if self._dir_only:
            entries = [entry for entry in entries if entry.is_dir()]
            return entries
        entries = sorted(entries, key=lambda entry: entry.is_file())
        return entries