# Author: CZ
# Time: 2019-07-04
"""
    split a role's lines each sence in a play

"""
from easygui import*


class SplitandSave:

    def __init__(self, fp, cc):
        self.filepath = fp
        self.role = cc

    def save_file(self, content, count):
        role = self.role
        file_name = role + ' lines in scene '+str(count) + '.txt'
        role_file = open(file_name, 'w')
        role_file.writelines(content)
        role_file.close()

    def split_scene(self):
        file_name = self.filepath
        role = self.role
        with open(file_name, 'r') as f:
            role_content = []
            count = 1
            for each_line in f:
                if each_line[:6] != "======" and each_line[:2].isspace() is False:
                    if '.' in each_line:
                        (name, content) = each_line.split('.', 1)
                        if name == role:
                            role_content.append(content)
                elif each_line[:3].isspace() is False:
                    if role_content:
                        self.save_file(role_content, count)
                    role_content = []
                    count += 1


path = fileopenbox(default='*.txt')
character = 'Rom'
SplitandSave(path, character).split_scene()
print(SplitandSave(path, character).filepath)


