from setuptools import setup, find_packages

setup(
    name="gtk-llm-chat",
    author="Sebastian Silva <sebastian@fuentelibre.org>",
    version="1.1.1",
    packages=find_packages(),
    install_requires=[
        'libayatana-appindicator',
        'PyGObject',
        'markdown-it-py',
    ],
    entry_points={
        'console_scripts': [
            'gtk-llm-chat=gtk_llm_chat.main:main',
            'gtk-llm-applet=gtk_llm_chat.gtk_llm_applet:main',
        ],
    }
) 