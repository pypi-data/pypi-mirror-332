from setuptools import setup, find_packages  # or find_namespace_packages

print('n\nn\nn\nn\n')

setup(
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            "my-world = test_atml:hello_world",
        ]
    }
)
