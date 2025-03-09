from setuptools import setup, find_packages  # or find_namespace_packages

setup(
    # ...
    entry_points={
        'console_scripts': [
            "my-world = test_atml:hello_world",
        ]
    }
)
