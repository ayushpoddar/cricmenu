from setuptools import setup

APP = ['live.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleShortVersionString': '1.0.0',
        'LSUIElement': True,
    },
    'packages': ['rumps', 'requests'],
}

setup(
    app=APP,
    name='CricMenu',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], 
    install_requires=['rumps', 'requests']
)