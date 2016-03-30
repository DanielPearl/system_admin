# >> - query /etc/hosts/ for value (host)
# >> - ssh to that value
# >> - change a config file
# >> - report back what was changed

# Preferably a variable that via the terminal command you can set to add or change a line in a file to whatever you like. Honestly though it's a open enough question where there is no wrong way. As long as it can change a file in a way is good enough for me. Bonus points for being more creative and making it have more options.

import os


class change_file:
    def __init__(self):
        pass

    def print_file(self, path):
        """
        path: name of path/file to be changed
        returns: prints contents of file in terminal
        """
        file_object = open(path, 'r') # what happens if open contains nothing (consider what 'r' does vs something else)?
        print(file_object.read())

    def append_file(self, path, text):
        """
        path: name of path/file to be changed
        text: text to be added to file
        returns: appends file with new text
        """
        file_object = open(path, 'a')
        file_object.write("\n")
        file_object.write(text)
        file_object.close()

    def rename_file(self, current_path, new_path):
        """
        current_path: name of path/file to be changed
        new_path: new path/name of file
        returns: changes file name
        """
        os.rename(current_path, new_path)

    def replace_file(self, path, replacement_text):
        """
        path: name of file to be changed
        replacement_text: new text to replace existing text in file
        returns: replaces text in file with replacement text
        """
        file_object = open(path, 'w')
        file_object.write(replacement_text)
        file_object.close()

    def ban_website(self, url):
        """
        url: site to be blocked
        returns: blocks website
        """
        if url != None:
            path = '/etc/hosts'
            text = '127.0.0.1   {}'.format(url)
            self.append_file(path, text)


cf = change_file()
cf.append_file('/etc/hosts', 'hello')

# for ban_website: sudo python3 change_config.py
