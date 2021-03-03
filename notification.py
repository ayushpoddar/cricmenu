import os

# Notify
def notify(title, message):
    command = f'''
        osascript -e 'display notification "{message}" with title "{title}"'
        '''
    os.system(command)


