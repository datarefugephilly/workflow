import argparse
import ftplib
import os
import tqdm
import time
import re

"""
Example usage as a CLI:
```
python3 download_ftp_tree ftp.something.com /some/directory .
```
The code above will look for a directory called /some/directory/ on the ftp
host, and then duplicate the directory and its entire contents into the local
current working directory.
Additional options are available for authentication and more. See help:
```
python3 download_ftp_tree -h
```
"""


def _is_ftp_dir(ftp_handle, name, guess_by_extension=True):
    """ simply determines if an item listed on the ftp server is a valid directory or not """

    # if the name has a "." in the fourth to last position, its probably a file extension
    # this is MUCH faster than trying to set every file to a working directory, and will work 99% of time.
    if guess_by_extension is True:
        if len(name) >= 4:
            if name[-4] == '.':
                return False

    original_cwd = ftp_handle.pwd()     # remember the current working directory
    try:
        ftp_handle.cwd(name)            # try to set directory to new name
        ftp_handle.cwd(original_cwd)    # set it back to what it was
        return True
    except:
        return False


def _make_parent_dir(fpath):
    """ ensures the parent directory of a filepath exists """
    dirname = os.path.dirname(fpath)
    while not os.path.exists(dirname):
        try:
            os.mkdir(dirname)
            print("created {0}".format(dirname))
        except:
            _make_parent_dir(dirname)


def _download_ftp_file(ftp_handle, name, dest, overwrite):
    """ downloads a single file from an ftp server """
    _make_parent_dir(dest.lstrip("/"))
    if not os.path.exists(dest) or overwrite is True:
        try:
            with open(dest, 'wb') as f:
                ftp_handle.retrbinary("RETR {0}".format(name), f.write)
        except FileNotFoundError:
            print("FAILED: {0}".format(dest))
    else:
        print("already exists: {0}".format(dest))


def _mirror_ftp_dir(ftp_handle, files, excluded, name, guess_by_extension, specifications):
    """ replicates a directory on an ftp server recursively """

    def handle_item(item, specifications):
        """
        Matches an item against a set of include/exclude specifications. The action for the
        first matching regex is used. If nothing matches no action is taken.
        """
        for (inex, regex) in specifications:

            # If item matches this spec:
            if regex.search(item):
                # If this is an exclude spec, we're done
                if inex == 'e':
                    #print('excluding', item)
                    excluded.append(item)
                    return
                else:
                    break

        if _is_ftp_dir(ftp_handle, item, guess_by_extension):
            _mirror_ftp_dir(ftp_handle, files, excluded, item, guess_by_extension, specifications)
        else:
            try:
                size = ftp.size(item)
            except Exception:
                size = 1  # FTP does not always implement size
            files[item] = size
            #print('including',item)


    print('cumulative size: {} excluded items: {} currently rescursing {}'.format(
        sizeof_fmt(sum(list(files.values()))), len(excluded), name))

    for item in ftp_handle.nlst(name):
        handle_item(item, specifications)

def download(ftp_handle, files, overwrite, sleep=4):
    progress = tqdm.tqdm(total=sum(list(files.values())))
    for item, size in files.items():
        time.sleep(sleep)
        _download_ftp_file(ftp_handle, item, item, overwrite)
        progress.update(size)
    progress.close()


def download_ftp_tree(ftp_handle, path, destination, sleep=4,
                      overwrite=False, guess_by_extension=True, specifications=[]):
    """
    Downloads an entire directory tree from an ftp server to the local destination
    :param ftp_handle: an authenticated ftplib.FTP instance
    :param path: the folder on the ftp server to download
    :param destination: the local directory to store the copied folder
    :param overwrite: set to True to force re-download of all files, even if they appear to exist already
    :param guess_by_extension: It takes a while to explicitly check if every item is a directory or a file.
        if this flag is set to True, it will assume any file ending with a three character extension ".???" is
        a file and not a directory. Set to False if some folders may have a "." in their names -4th position.

    Returns a list of paths that were excluded by specifications.
    """
    path = path.lstrip("/")
    original_directory = os.getcwd()    # remember working directory before function is executed
    os.chdir(destination)               # change working directory to ftp mirror directory
    files = {}
    excluded = []
    _mirror_ftp_dir(ftp_handle, files, excluded, path, guess_by_extension, specifications)
    download(ftp_handle, files, overwrite, sleep)
    os.chdir(original_directory)        # reset working directory to what it was before function exec
    return excluded

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def parse_args(args=None):
    class Include(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            d = getattr(namespace, self.dest, self.default)
            setattr(namespace, self.dest, val + 1)

    class Ex(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            val = getattr(namespace, self.dest, self.default)
            setattr(namespace, self.dest, val - 1)

    parser = argparse.ArgumentParser(description='Bulk download over FTP.')
    parser.add_argument('host', type=str)
    parser.add_argument('remote_dir', type=str, help='source directory')
    parser.add_argument('local_dir', type=str, help='target directory')
    parser.add_argument('--username', type=str, help='username for login')
    parser.add_argument('--password', type=str, help='password for login')
    parser.add_argument('--sleep', type=int, default=4,
                        help=('delay between files to avoid hammering sever '
                              '(in seconds)'))
    parser.add_argument('-o', '--overwrite', action='store_true', help='overwrite files that already exist')
    specs_group = parser.add_argument_group(
            'Specifications',
            """
            An ordered set of specification tuples that control what objects will be included or excluded from downloads.
            Each specification is either include (i) or exclude (e), and a regular expression. The first specification that
            matches a path is used. If a path does not match any specifications, it is downloaded.
            """
            )
    specs_group.add_argument('-s', '--specification', metavar='i/e regex', nargs=2, dest='specs', action='append',
            help='i (include) or e (exclude), followed by a regular expression')
    #specs_group.add_argument('-i', '--include', metavar='include regex', dest='filters', action='append', help='sources to include')
    #specs_group.add_argument('-e', '--exclude', metavar='exclude regex', dest='filters', action='append', help='sources to exclude')

    parsed = parser.parse_args(args)

    specs = []
    if not parsed.specs is None:
        for (inex, regex) in parsed.specs:
            if not (inex=='i' or inex=='e'):
                raise "specification must start with i or e ({} {})".format(inex,regex)

            specs.append((inex, re.compile(regex)))

    parsed.specs = specs
    return parsed

def main(args=None):
    args = parse_args(args)
    print('Downloading ftp://{}/{} to {}'.format(args.host, args.remote_dir, args.local_dir))
    if args.specs != []:
        print('Using specifications:')
        for s in args.specs:
            print(' '.join([s[0], s[1].pattern]))

    ftp = ftplib.FTP(args.host, args.username or None, args.password or None)
    ftp.login()
    excluded = download_ftp_tree(ftp, args.remote_dir, args.local_dir, args.sleep,
            overwrite=args.overwrite, specifications=args.specs)
    if excluded != []:
        filename = 'excluded_files.{}.txt'.format(args.host)
        print('Writing {}'.format(filename))
        with open(filename, 'w') as f:
            for e in excluded:
                f.write(e + '\n')

if __name__ == "__main__":
    print(parse_args())
    main()
