import os
import fnmatch

'''
To use, place script one level above repo you want to scan, and set the ROOT variable equal
to that repo's directory
'''
def fnmatch_multi(names, patterns):
    '''Helper method to allow passing a list of args to fnmatch.
    Patterns should be either list of strings, or a single string.'''
    for name in names:
        if any(fnmatch.fnmatch(name, pattern) for pattern in patterns):
            yield name

ROOT = 'test'
FIND = 'spam'
REPLACE = 'eggs'

counter = 0
changes_count = 0

for dir, subdirs, files in os.walk(ROOT):
    
    # subdirs will be populated with every folder encountered within ROOT, recursively. 
    #  This purges .git folder(s) from discovered dirs. Could be made more inclusive (exclusive?) with 
    # 'd != '.git'' --> 'd not in [list of strs]' 
    subdirs[:] = [d for d in subdirs if d != '.git']
    
    # probably DON'T find and replace in .sh files, as they typically initialize the secrets (not plug in)
    included = fnmatch_multi(files, ['*.groovy', '*.yaml', '*.txt'])
    excluded = fnmatch_multi(files, ['*.git', '*.bak', '*.gitignore'])
    filtered = set(included) - set(excluded)
    
    print("scanning:")
    for filename in filtered:

        FILENAME = os.path.join(dir, filename)

        print('  `{}`'.format(FILENAME))

        with open(FILENAME, 'r', newline='\n') as f:
            copy = f.read()

        # # The below two lines will create a backup of all read files. 
        # # This script is not smart enough to know which files it actually changes, and will
        # # backup everything scanned.
        
        # with open(FILENAME+'.bak', 'w') as f:
        #     f.write(copy)

        temp = id(copy)
        copy = copy.replace(FIND, REPLACE)
        
        if id(copy) != temp:
            changes_count += 1

        with open(FILENAME, 'w', newline='\n') as f:
            f.write(copy)

        counter += 1

print()
print("finished!")
print("scanned {} files".format(counter), "and modified {}".format(changes_count))