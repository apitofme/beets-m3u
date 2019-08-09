##
# << File information
##

# << import modules from beets
from beets.plugins import BeetsPlugin
from beets import config


# << Define non-class functions


# << Define main plugin class
class PluginName(BeetsPlugin):
    # << __init__ function
    def __init__(self):
        # ?? is a call to the parent __init__ essential? (assuming YES!)
        super(PluginName, self).__init__()

        # << register default options in to config
        self.config.add()
        # ?? -- OR --
        config['pluginname'].add()

        # << any other initialisation actions
        # - e.g. register event handlers

    # << -- Begin to define CLass methods -- >>

    # create a file for the new playlist
    # > create_playlist_file()
        # ?? should this be a temporary file that gets copied/moved to a 'hard' file once content is complete?
        # !! when using `with open(file) as file` the file is closed when leaving the `with` block
        #    ...so this likely wouldn't work if passing the open file back to another function

    # generate the playlist file's contents
    # > generate_playlist()
        # ?? should this simply be written straight in to the file or compiled in a string-buffer?
        # ?? do both 'album' and 'item' query result objects provide the necessary file-paths as attributes?
        #    ...or will I need to query for each item within an album when receiving an album result object?

    # save the playlist file
    # > save_playlist()
        # !! if using a temporary file then this needs to be copied/moved to a normal file!
        # ?? do I need some kind of garbage collection, aside from making sure to `.close()` all files?
        # ?? what should I do if an operation is interrupted? (logging / recovery)

    # handle album imports
    # > event_handler()

    # add CLI functionality
    # > commands()
        # << create associated command functions
        # - e.g.:
        #   -- single album search
        #   -- multi-album search, creating a playlist per album
        #   -- multi-singleton search, creating a custom compilation playlist
        # ?? should the command functions be class methods or external functions?
