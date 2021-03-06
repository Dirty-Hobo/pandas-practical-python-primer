##### [Previous](exercise-9.md) |  [Next](exercise-11.md)  

## Exercise 10: Oh My, Our Program Broke an Arm
[Code Files](../../training/level-2-command-line-interfaces/bfp-reference/exercise_10)

So, our program is great. It can copy files. **But, it's a little bit fragile.**
Let's demonstrate:

1. Attempt to copy an non-existent file:

    ```python
    >>> python stdlib_cli.py -f nonexistent_file -d /home/vagrant
    Traceback (most recent call last):
      File "exercise_10/stdlib_cli.py", line 36, in <module>
        destination=program_arguments.destination)
      File "/vagrant/training/level-2-command-line-interfaces/bfp-reference/exercise_10/file_ops.py", line 24, in copy_files
        stderr=subprocess.STDOUT)
      File "/home/vagrant/.pyenv/versions/3.4.3/lib/python3.4/subprocess.py", line 620, in check_output
        raise CalledProcessError(retcode, process.args, output=output)
    subprocess.CalledProcessError: Command '['cp', '-vp', 'nonexistent_file', '/home/vagrant']' returned non-zero exit status 1
    ```
    
2. How about specifying a non-existent destination?  Or perhaps a directory you
don't have access to?
    ```python
    >>> python stdlib_cli.py -f testfile_1 -d /home/non-existent
    Traceback (most recent call last):
      File "exercise_10/stdlib_cli.py", line 36, in <module>
        destination=program_arguments.destination)
      File "/vagrant/training/level-2-command-line-interfaces/bfp-reference/exercise_10/file_ops.py", line 24, in copy_files
        stderr=subprocess.STDOUT)
      File "/home/vagrant/.pyenv/versions/3.4.3/lib/python3.4/subprocess.py", line 620, in check_output
        raise CalledProcessError(retcode, process.args, output=output)
    subprocess.CalledProcessError: Command '['cp', '-vp', 'exercise_10/testfile_1', '/home/non-existent']' returned non-zero exit status 1
    ```
        
## Goal 6: Adding Conditional Logic and Exception Handling
In this step we are going to add somethings into our program that *can* make
it explode depending on the input we receive from the user.  We'll look at
a couple of different ways of dealing with this added complexity.

1. Add an if/else statement to check for the existence of non-empty new_names 
function parameter value.
    * Options for checking if for non-empty : `if new_names vs. if new_names is not None`
        * Objects that evaluate to `False` in if statements:
            * None
            * False
            * zero for numeric types
            * Empty sequences (tuples, lists, strings, etc)
            * Empty dictionaries
    * What is going on with `new_filenames[files.index(file)])`?
    * Review `str.format()`
    * So what is going to happen if there aren't enough names in `new_names`
    to match the number of files in `files`?
    
2. Add Exception handling to deal with the IndexError that we've discovered!
    * Talk about error handling in Python: `try...except...else...finally`
    ```
    try:
        1/0
    except ZeroDivisionError:
        print("You did something illegal.")
    else:
        print("What you did was fine.")
    finally:
        print("You did something and it doesn't matter to me what it was.")
    ```
    * What goes in each section?
    * How much should go into the `try` block?
    * Add exception handling for the `IndexError` that will occur if we attempt
    to reference an index that doesn't exist in `new_filenames`.
    * Run the program using a variety of inputs trying to exercise the 
    different code paths.


## Goal 7: Becoming a multi-purpose CLI
We've made great progress thus far.  Now let's take the next (and final) step
in this training level and turn our CLI into something that can handle more
than one type of task.  Specifically, let's add the ability for our 
program to move files as well as copy them.

1. Add subparsers to your argparse.Argument parser object.  Talk about what
this is doing to the object.  
    ```
    subcommand_parsers = parser.add_subparsers(
            title="Available Commands",
            description="The following sub-commands are available.",
            dest="command")
    subcommand_parsers.required = True
    ```
    
    * Objects have attributes which are themselves objects.
    * What does `self._subparsers` mean?  `self` and "private" attributes.
    
2. Create two subparsers for the `move` and `copy` commands.
    ```
    copy_parser = subcommand_parsers.add_parser(name='copy', help="Copy Files")
    move_parser = subcommand_parsers.add_parser(name='move', help="Move Files")
    ```
    
    * Temporarily comment out the all of the `parser.add_argument` calls
    and see how the program now looks from the command line.
    
3. Add the `parser` arguments to both `move_parser` and `copy_parser`.
    * See how this affects the program operation.
    * Pay attention to how code is being repeated here.  This is a bad
    thing.  Violation of DRY.  We'll come back to it later if we have time.

     