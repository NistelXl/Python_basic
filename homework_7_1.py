import os

ROOT = os.path.dirname(__file__)
project = 'my_project_1'
paths = [os.path.join(project, 'settings'), os.path.join(project, 'mainapp'), os.path.join(project, 'adminapp'), os.path.join(project, 'authapp')]

for _path in paths:
    os.makedirs(os.path.join(ROOT, _path), exist_ok=True)