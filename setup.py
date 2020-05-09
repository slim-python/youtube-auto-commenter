import setuptools

setuptools.setup(
    name="comspam",
    version="1.0.0",
    author="Abhi Raj", py_modules=['youtube-auto-commenter'],
    install_requires=[
        "pyautogui",
    ],
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "License :: GPL-3.0-or-later",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        comspam=youtube-auto-commenter:mainmenu
    ''',
    python_requires='>=3.8',
    include_package_data=True,
)