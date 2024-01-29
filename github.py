import os
for i in range(10):
    os.system('git add .')
    os.system(f'git commit -m "Push Automation Number {i}"')
    os.system('git push -u origin main')