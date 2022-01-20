import os
import shutil

root_dir = os.path.join(os.path.dirname(__file__), 'my_project_1')
an_dir = os.path.join(os.path.dirname(__file__), 'my_project_1', 'templates')

if not os.path.exists(an_dir):
    os.makedirs(an_dir)

for root, dirs, files in os.walk(root_dir):
    if root.count('templates'):
        for dir_ in dirs:
            if not os.path.exists(os.path.join(an_dir, dir_)):
                os.makedirs(os.path.join(an_dir, dir_))

        for file in files:
            src_file = os.path.join(root, file)
            an_file = os.path.join(an_dir, os.path.basename(root))
            if not os.path.dirname(src_file) == an_file:
                shutil.copy(src_file, an_file)
