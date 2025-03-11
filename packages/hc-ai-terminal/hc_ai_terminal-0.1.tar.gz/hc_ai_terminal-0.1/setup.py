from setuptools import setup, find_packages

setup(
    name="hc_ai_terminal",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ai = ai_terminal.ai:main',  # Replace with correct module path
        ],
    },
)
