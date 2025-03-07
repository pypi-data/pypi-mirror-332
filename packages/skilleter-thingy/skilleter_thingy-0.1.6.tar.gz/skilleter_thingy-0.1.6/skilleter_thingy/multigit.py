#!/usr/bin/env python3

"""mg - MultiGit - utility for managing multiple Git working trees in a hierarchical directory tree"""

import os
import sys
import fnmatch
import configparser

from dataclasses import dataclass, field

import thingy.git2 as git
import thingy.colour as colour

################################################################################

# DONE: ***MUST use relative paths in config file, or we can't store in git and clone and use somewhere else!***
# DONE: / Output name of each working tree as it is processed as command sits there seeming to do nothing otherwise.
# DONE: Better error-handling - e.g. continue/abort option after failure in one working tree
# DONE: Currently doesn't handle single letter options in concatenated form - e.g. -dv
# DONE: Don't save the configuration on exit if it hasn't changed
# DONE: Don't use a fixed list of default branch names
# DONE: If the config file isn't in the current directory then search up the directory tree for it but run in the current directory
# DONE: Use the configuration file
# DONE: When specifying list of working trees, if name doesn't contain '/' prefix it with '*'?
# DONE: command to categorise working trees then command line filter to only act on working trees in category (in addition to other filtering options) - +tag <TAG> command tags all selected working trees and updates the configuration, +untag <TAG> command to remove tags in the same way
# DONE: init function
# NOPE: Clone to have option to update - as discussed, should be part of init
# NOPE: Dry-run option - just pass the option to the Git command
# NOPE: Is it going to be a problem if the same repo is checked out twice or more in the same workspace - user problem
# NOPE: Pull/fetch - only output after running command and only if something updated
# NOPE: Switch to tomlkit
# TODO: 2 .init option '--update' to update the configuration file with new working trees and remove ones that are no longer there
# TODO: 2. +run command to do things other than git commands
# TODO: 2. If run in a subdirectory, only process working trees in that tree (or have an option to do so, or an option _not_ to do so; --all)
# TODO: 2. select_git_repos() and +dir should use consist way of selecting repos if possible
# TODO: 3 .init option '--set-default' to update the default branch to the current one for specified working trees
# TODO: 3. Ability to read default configuration options from ~/.config/thingy/multigit.rc - these are insert before argv[1] before argparse called
# TODO: 3. Command that takes partial working tree name and either returns full path or pops up window to autocomplete until single match found
# TODO: 3. Verbose option
# TODO: 3. When filtering by tag or by repo name, if name starts with '!' only match if tag isn't present or repo name doesn't match (and don't allow '!' at start of tag otherwise)
# TODO: 4. Option to +dir to return all matches so that caller can select one they want
# TODO: 4. Shell autocomplete for +dir
# TODO: 5. -j option to run in parallel - yes, but it will only work with non-interactive Git commands
# TODO: 5. Consistent colours in output
# TODO: 6. Use PathLib
# TODO: 6. When we have something with multiple matches display a menu for user to select the one that they one - make it a library routine so can be used, for instance, for branch selection
# TODO: 7. Use pygit2 directly
################################################################################

DEFAULT_CONFIG_FILE = 'multigit.toml'

# If a branch name is specified as 'DEFAULT' then the default branch for the
# repo is used instead.

DEFAULT_BRANCH = 'DEFAULT'

################################################################################
# Command line help - we aren't using argparse since it isn't flexible enough to handle arbtirary git
# commands are parameters so we have to manually create the help and parse the command line

HELP_INFO = """usage: multigit [-h] [--verbose] [--quiet] [--config CONFIG] [--repos REPOS] [--modified] [--branched] [--sub] [--tag TAGS]
                {+clone, +init, +config, +dir, GIT_COMMAND} ...

Run git commands in multiple Git repos. DISCLAIMER: This is beta-quality software, with missing features and liable to fail with a stack trace, but shouldn't eat your data

options:
  -h, --help            show this help message and exit
  --verbose, -v         Verbosity to the maximum
  --quiet, -q           Minimal console output
  --config CONFIG, -c CONFIG
                        The configuration file (defaults to multigit.toml)
  --repos REPOS, -r REPOS
                        The repo names to work on (defaults to all repos and can contain shell wildcards and can be issued multiple times on the command line)
  --modified, -m        Select repos that have local modifications
  --branched, -b        Select repos that do not have the default branch checked out
  --tag TAG, -t TAG     Select repos that have the specified tag (can be issued multiple times on the command line)
  --sub, -s             Select only the repos in the current directory and subdirectories
  --continue, -C        Continue if a git command returns an error (by default, executation terminates when a command fails)

Sub-commands:
  {+clone, +init,+dir,+config, GIT_COMMAND}
    +clone REPO {BRANCH} Clone a repo containing a multigit configuration file, then clone all the child repos and check out the default branch in each
    +init                Build or update the configuration file using the current branch in each repo as the default branch
    +config              Return the name and location of the configuration file
    +dir                 Return the location of a working tree, given the repo name, or if no parameter specified, the root directory of the multigit tree
    +tag TAG             Apply a configuration tag to repos filtered by the command line options (list configuration tags if no parameter specified)
    +untag TAG           Remove a configuration tag to repos filtered by the command line options
    GIT_COMMAND          Any git command, including options and parameters - this is then run in all specified working trees

"""

################################################################################

@dataclass
class Arguments():
    """Data class to contain command line options and parameters"""

    # Command line options for output noise

    quiet: bool = False
    verbose: bool = False

    # True if we continue after a git command returns an error

    error_continue: bool = False

    # Default and current configuration file

    default_configuration_file: str = DEFAULT_CONFIG_FILE
    configuration_file: str = None

    # Command line filter options

    repos: list[str] = field(default_factory=list)
    tag: list[str] = field(default_factory=list)
    modified: bool = False
    branched: bool = False
    subdirectories: bool = False

    # Command to run with parameters

    command: str = None
    parameters: list[str] = field(default_factory=list)

    # True if running an internal command

    internal_command: bool = False

    # True if the configuration data needs to be written back on completion

    config_modified: bool = False

################################################################################

def error(msg, status=1):
    """Quit with an error"""

    colour.write(f'[RED:ERROR:] {msg}\n', stream=sys.stderr)
    sys.exit(status)

################################################################################

def absolute_repo_path(args, relative_path=''):
    """Given a path relative to the multigit configuration file, return
       the absolute path thereto"""

    return os.path.join(os.path.dirname(args.configuration_file), relative_path)

################################################################################

def find_configuration(default_config_file):
    """If the configuration file name has path elements, try and read it, otherwise
       search up the directory tree looking for the configuration file.
       Returns configuration file path or None if the configuration file
       could not be found."""

    if '/' in default_config_file:
        config_file = default_config_file
    else:
        config_path = os.getcwd()
        config_file = os.path.join(config_path, default_config_file)

        while not os.path.isfile(config_file) and config_path != '/':
            config_path = os.path.dirname(config_path)
            config_file = os.path.join(config_path, default_config_file)

    return config_file if os.path.isfile(config_file) else None

################################################################################

def show_progress(width, msg):
    """Show a single line progress message without moving the cursor to the next
       line."""

    colour.write(msg[:width-1], newline=False, cleareol=True, cr=True)

################################################################################

def find_working_trees(args):
    """Locate and return a list of '.git' directory parent directories in the
       specified path.

       If wildcard is not None then it is treated as a list of wildcards and
       only repos matching at least one of the wildcards are returned.

       If the same repo matches multiple times it will only be returned once. """

    repos = set()

    for root, dirs, _ in os.walk(os.path.dirname(args.configuration_file), topdown=True):
        if '.git' in dirs:
            relative_path = os.path.relpath(root)

            if args.repos:
                for card in args.repos:
                    if fnmatch.fnmatch(relative_path, card):
                        if relative_path not in repos:
                            yield relative_path
                            repos.add(relative_path)
                        break
            else:
                if relative_path not in repos:
                    yield relative_path
                    repos.add(relative_path)

        # Don't recurse down into hidden directories

        dirs[:] = [d for d in dirs if d[0] != '.']

################################################################################

def select_git_repos(args, config):
    """Return git repos from the configuration that match the criteria on the
       multigit command line (the --repos, --tag, --modified, --sub and --branched options)
       or, return them all if no relevant options specified"""

    for repo_path in config.sections():
        # If repos are specified, then only match according to exact name match,
        # exact path match or wildcard match

        repo_abs_path = absolute_repo_path(args, repo_path)

        if args.repos:
            for entry in args.repos:
                if config[repo_path]['repo name'] == entry:
                    matching = True
                    break

                if repo_path == entry:
                    matching = True
                    break

                if '?' in entry or '*' in entry:
                    if fnmatch.fnmatch(repo_path, entry) or fnmatch.fnmatch(config[repo_path]['repo name'], entry):
                        matching = True
                        break

            else:
                matching = False
        else:
            matching = True

        # If branched specified, only match if the repo is matched _and_ branched

        if matching and args.branched:
            if git.branch(path=repo_abs_path) == config[repo_path]['default branch']:
                matching = False

        # If modified specified, only match if the repo is matched _and_ modified

        if matching and args.modified:
            if not git.status(path=repo_abs_path):
                matching = False

        # If tag filtering specified, only match if the repo is tagged with one of the specified tags

        if matching and args.tag:
            for entry in args.tag:
                try:
                    tags = config[repo_path]['tags'].split(',')
                    if entry in tags:
                        break
                except KeyError:
                    pass
            else:
                matching = False

        # If subdirectories specified, only match if the repo is in the current directory tree

        if matching and args.subdirectories:
            repo_path_rel = os.path.relpath(absolute_repo_path(args, repo_path))

            if repo_path_rel == '..' or repo_path_rel.startswith('../'):
                matching = False

        # If we have a match, yield the config entry to the caller

        if matching:
            yield config[repo_path]

################################################################################

def branch_name(name, default_branch):
    """If name is None or DEFAULT_BRANCH return default_branch, otherwise return name"""

    return default_branch if not name or name == DEFAULT_BRANCH else name

################################################################################

def mg_clone(args, config, console):
    """Clone a repo, optionally check out a branch and attempt to read the
       configuration file and clone all the repos listed therein, checkouting
       the default branch in each one"""

    _ = console

    # Sanity checks

    if not args.parameters:
        error('The "clone" subcommand takes 1 or 2 parameters - the repo to clone and, optionally, the branch to check out')

    if args.branched or args.modified:
        error('The "modified" and "branched" options cannot be used with the "clone" subcommand')

    # Destination directory is the last portion of the repo URL with the extension removed

    directory = os.path.splitext(os.path.basename(args.parameters[0]))[0]

    if os.path.exists(directory):
        if os.path.isdir(directory):
            error(f'The "[BLUE:{directory}]" directory already exists')
        else:
            error(f'[BLUE:{directory}]" already exists')

    # Clone the repo and chdir into it

    if not args.quiet:
        colour.write(f'Cloning [BOLD:{args.parameters[0]}] into [BLUE:{directory}]')

    git.clone(args.parameters[0], path=directory)

    os.chdir(directory)

    # Optionally checkout a branch, if specified

    if len(args.parameters) > 1:
        git.checkout(args.parameters[1])

    # Open the configuration file in the repo (if no configuration file has been specified, use the default)

    if not args.configuration_file:
        args.configuration_file = args.default_configuration_file

    if not os.path.isfile(args.configuration_file):
        error(f'Cannot find the configuration file: [BOLD:{args.default_configuration_file}]')

    config.read(args.configuration_file)

    # Now iterate through the repos, creating directories and cloning them and checking
    # out the default branch

    for repo in select_git_repos(args, config):
        if repo.name != '.':
            directory = os.path.dirname(repo.name)

            if directory:
                os.makedirs(directory, exist_ok=True)

            if not args.quiet:
                colour.write(f'Cloning [BOLD:{repo["origin"]}] into [BLUE:{directory}]')

            git.clone(repo['origin'], path=repo.name)

            if not args.quiet:
                colour.write(f'    Checking out [BLUE:{repo["default branch"]}]')

            git.checkout(repo['default branch'], path=repo.name)

################################################################################

def mg_init(args, config, console):
    """Create or update the configuration
       By default, it scans the tree for git directories and adds or updates them
       in the configuration, using the current branch as the default branch. """

    # Sanity checks

    if args.modified or args.branched or args.tag or args.subdirectories:
        error('The "--tag", "--modified" "--sub", and "--branched" options cannot be used with the "init" subcommand')

    # Search for .git directories and add any that aren't already in the configuration

    repo_list = []
    for repo in find_working_trees(args):
        if not args.quiet:
            show_progress(console.columns, repo)

        repo_list.append(repo)

        if repo not in config:
            # Add a new configuration entry containing the default branch, remote origin
            # (if there is one) and name

            abs_repo_path = absolute_repo_path(args, repo)

            config[repo] = { }

            default_branch = git.branch(path=abs_repo_path)

            if not default_branch:
                error(f'Unable to determine default branch in [BLUE:{repo}]')

            config[repo]['default branch'] = default_branch

            remote = git.remotes(path=abs_repo_path)

            if 'origin' in remote:
                config[repo]['origin'] = remote['origin']
                config[repo]['repo name'] = os.path.basename(remote['origin']).removesuffix('.git')
            else:
                config[repo]['repo name'] = os.path.basename(repo)

            colour.write(f'Added [BOLD:{repo}] with default branch [BLUE:{default_branch}]')

    if not args.quiet:
        colour.write(cleareol=True)

    # Look for configuration entries that are no longer present and delete them

    removals = []

    for repo in config:
        if repo != 'DEFAULT' and repo not in repo_list:
            removals.append(repo)

    for entry in removals:
        del config[entry]
        colour.write(f'Removed [BOLD:{repo}] as it no longer exists')

    # The configuration file needs to be updated

    args.config_modified = True

################################################################################

def mg_dir(args, config, console):
    """Return the location of a working tree, given the name, or the root directory
       of the tree if not
       Returns an error unless there is a unique match"""

    _ = console
    _ = config

    if len(args.parameters) > 1:
        error('The +dir command takes no more than one parameter - the name of the working tree to search for')

    if args.modified or args.branched or args.tag or args.subdirectories:
        error('The "--tag", "--modified" "--sub", and "--branched" options cannot be used with the "dir" subcommand')

    # If a parameter is specified, look for matches, otherwise just return the location of the
    # configuration file

    if args.parameters:
        location = []
        wild_prefix_location = []
        wild_location = []

        search_name = args.parameters[0]

        # Search for exact matches, matches if prefixed by '*' or prefixed and suffixed with '*'
        # unless it already contains '*'

        for repo in select_git_repos(args, config):
            if fnmatch.fnmatch(repo['repo name'], search_name):
                location.append(repo.name)

            elif '*' not in search_name:
                if fnmatch.fnmatch(repo['repo name'], f'*{search_name}'):
                    wild_prefix_location.append(repo.name)

                elif fnmatch.fnmatch(repo['repo name'], f'*{search_name}*'):
                    wild_location.append(repo.name)

        # Look for a single exact match, a prefix with '*' match or prefix+suffix

        destination = None
        for destinations in (location, wild_prefix_location, wild_location):
            if len(destinations) == 1:
                destination = destinations
                break

            if len(destinations) > 1:
                destination = destinations

        if not destination:
            error(f'No matches with [BLUE:{search_name}]')

        if len(destination) > 1:
            dest_list = "\n\t".join([os.path.relpath(d) for d in destination])
            error(f'Multiple matches with [BLUE:{search_name}]: \n\t{dest_list}')

        colour.write(absolute_repo_path(args, destination[0]))

    else:
        colour.write(os.path.dirname(args.configuration_file))

################################################################################

def mg_tag(args, config, console):
    """Apply a configuration tag"""

    _ = console

    if len(args.parameters) > 1:
        error('The +tag command takes no more than one parameter')

    for repo in select_git_repos(args, config):
        try:
            tags = repo.get('tags').split(',')
        except AttributeError:
            tags = []

        if args.parameters:
            if args.parameters[0] not in tags:
                tags.append(args.parameters[0])
                repo['tags'] = ','.join(tags)
                args.config_modified = True
        elif tags:
            colour.write(f'[BOLD:{repo["repo name"]}] - {", ".join(tags)}')

################################################################################

def mg_untag(args, config, console):
    """Remove a configuration tag"""

    _ = console

    if len(args.parameters) > 1:
        error('The +tag command takes no more than one parameter')

    for repo in select_git_repos(args, config):
        try:
            tags = repo.get('tags', '').split(',')
        except AttributeError:
            tags = []

        if args.parameters[0] in tags:
            tags.remove(args.parameters[0])
            repo['tags'] = ','.join(tags)
            args.config_modified = True

################################################################################

def mg_config(args, config, console):
    """Output the path to the configuration file"""

    _ = config
    _ = console

    if len(args.parameters):
        error('The +config command does not take parameters')

    colour.write(os.path.relpath(args.configuration_file))

################################################################################

def run_git_command(args, config, console):
    """Run a command in each of the working trees, optionally continuing if
       there's an error"""

    _ = console

    for repo in select_git_repos(args, config):
        repo_command = [args.command]

        # Replace 'DEFAULT' in the command with the default branch in the repo

        for cmd in args.parameters:
            repo_command.append(branch_name(cmd, repo['default branch']))

        colour.write(f'\n[BOLD:{os.path.relpath(repo.name)}]\n')

        # Run the command in the workng tree

        repo_path = absolute_repo_path(args, repo.name)

        _, status = git.git_run_status(repo_command, path=repo_path, redirect=False)

        if status and not args.error_continue:
            sys.exit(status)

################################################################################

def parse_command_line():
    """Manually parse the command line as we want to be able to accept 'multigit <OPTIONS> <+MULTIGITCOMMAND | ANY_GIT_COMMAND_WITH_OPTIONS>
       and I can't see a way to get ArgumentParser to accept arbitrary command+options"""

    args = Arguments()

    # Expand arguments so that, for instance '-dv' is parsed as '-d -v'

    argv = []

    for arg in sys.argv:
        if arg[0] != '-' or arg.startswith('--'):
            argv.append(arg)
        else:
            for c in arg[1:]:
                argv.append('-' + c)

    # Parse the command line, setting options in the args dataclass appropriately

    i = 1
    while i < len(argv):
        param = argv[i]

        if param in ('--verbose', '-v'):
            args.verbose = True

        elif param in ('--quiet', '-q'):
            args.quiet = True

        elif param in ('--config', '-c'):
            try:
                i += 1
                args.default_configuration_file = argv[i]
            except IndexError:
                error('--config - missing configuration file parameter')

        elif param in ('--repos', '-r'):
            try:
                i += 1
                args.repos.append(argv[i])
            except IndexError:
                error('--repos - missing repo parameter')

        elif param in ('--tag', '-t'):
            try:
                i += 1
                args.tag.append(argv[i])
            except IndexError:
                error('--tag - missing tag parameter')

        elif param in ('--modified', '-m'):
            args.modified = True

        elif param in ('--branched', '-b'):
            args.branched = True

        elif param in ('--sub', '-s'):
            args.subdirectories = True

        elif param in ('--continue', '-C'):
            args.error_continue = True

        elif param in ('--help', '-h'):
            colour.write(HELP_INFO)
            sys.exit(0)

        elif param[0] == '-':
            error(f'Invalid option: "{param}"')
        else:
            break

        i += 1

    # After the options, we either have a multigit command (prefixed with '+') or a git command
    # followed by parameter

    try:
        if argv[i][0] == '+':
            args.command = argv[i][1:]
            args.internal_command = True
        else:
            args.command = argv[i]
            args.internal_command = False

    except IndexError:
        error('Missing command')

    # Save the command parameters

    args.parameters = argv[i+1:]

    # Locate the configuration file

    args.configuration_file = find_configuration(args.default_configuration_file)

    return args

################################################################################

COMMANDS = {
    'clone': mg_clone,
    'init': mg_init,
    'dir': mg_dir,
    'config': mg_config,
    'tag': mg_tag,
    'untag': mg_untag,
}

def main():
    """Main function"""

    # Parse the command line and santity check the command to run
    # (if it is an external command we let git worry about it)

    args = parse_command_line()

    if args.internal_command and args.command not in COMMANDS:
        error(f'Invalid command "{args.command}"')

    # If the configuration file exists, read it

    config = configparser.ConfigParser()

    # If running the '+init' command without an existing configuration file
    # use the default one (which may have been overridden on the command line)
    # Otherwise, fail if we can't find the configuration file.

    if not args.configuration_file:
        if args.internal_command:
            if args.command == 'init':
                args.configuration_file = os.path.abspath(args.default_configuration_file)
        else:
            error('Cannot locate configuration file')

    if args.configuration_file and os.path.isfile(args.configuration_file):
        config.read(args.configuration_file)

    # Get the console size

    try:
        console = os.get_terminal_size()
    except OSError:
        console = None
        args.quiet = True

    # Run an internal or external command-specific validation

    if args.internal_command:
        # Run the subcommand

        COMMANDS[args.command](args, config, console)

        # Save the updated configuration file if it has changed (currently, only the init command will do this).

        if config and args.config_modified:
            with open(args.configuration_file, 'w', encoding='utf8') as configfile:
                config.write(configfile)

    else:
        # Run the external command, no need to update the config as it can't change here

        run_git_command(args, config, console)

################################################################################

def multigit():
    """Entry point"""

    try:
        main()

    # Catch keyboard aborts

    except KeyboardInterrupt:
        sys.exit(1)

    # Quietly fail if output was being piped and the pipe broke

    except BrokenPipeError:
        sys.exit(2)

    # Catch-all failure for Git errors

    except git.GitError as exc:
        sys.stderr.write(exc.msg)
        sys.exit(exc.status)

################################################################################

if __name__ == '__main__':
    multigit()
