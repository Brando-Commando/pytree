# pytree
pytree is a command line tool created in python for creating easy-to-read directory trees.

This project was created by following the tutorial created by Leodanis Pozo Ramos on Real Python.
The link to the tutorial is https://realpython.com/directory-tree-generator-python/

The current version of this project is 0.2.0 and is a completed and annotated version as shown through the tutorial.
I did not just want to copy and paste this project, and made steps to annotate and fully understand every piece 
of how it functions.

Commands:

  - To run the script you should make sure to download this entire package and ensure you have Python on your PATH. 
      The command to run the script is as follows without the quotations:
        -- "python3 <PATH to tree.py>"
      This will print out a directory tree of your current working directory. 
  
  - To print out only directories in the tree, you would add either "-d" or "--dir-only" to the end of the basic run command,
      it would appear as follows:
        -- "python3 <PATH to tree.py> -d" or "python3 <PATH to tree.py> --dir-only"
  
  - To save the output of the script to a user-suggested file, you would add either "-o" or "--output-file" to the end of the basic run command,
      it would appear as follows:
        -- "python3 <PATH to tree.py> -o" or "python3 <PATH to tree.py> --output-file"

  - There is also an additional command to check which version of the script the user is running. you would add either "-v" or "--version" to the end of
      the basic run command. It would appear as follows:
        -- "python3 <PATH to tree.py> -v" or "python3 <PATH to tree.py> --version"
  
  
  FUTURE FEATURES:

  I hope to add a "-c" or "--commands" feature in order to explain the above commands in more brief terms for the user as a quick refresh.
  
  Currently the program will output hidden files and directories, I will either edit this to no longer be default and include a command for the outputting of hidden files. Or vice versa, keep it default and add a command for outputting without hidden files and directories. Typically, I believe most people will not be reaching into hidden files on default so I will most likely proceed with the former.
  
  
  Thank you very much for reading, contributing to or using this project. 
  Any and all criticism is welcome once I have been able to make this project my own.
