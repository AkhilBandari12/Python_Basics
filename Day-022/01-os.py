#!/usr/bin/env python3

import os

print("Some use cases of the `os` module.\n")

print(f"Operating System type: {os.name}")
print(f"Environment variables: {os.environ}")
print("\nos.envrion returns a dict")
print("Hence, it is possible to retreive a specific value")
print(f"""Calling os.environ['USER'] : {os.environ["USER"]}""")
print("os.environ(<KEY>) will error if KEY is not present")
print("Use os.printenv(KEY) in such cases")
print(f"""Calling os.getenv('USER'): {os.getenv("USER")}""")
print("Get the current working directory, and change to another")
print(f"Current Working Directory: {os.getcwd()}")
print("Changing workding directory, with os.chdir('<path>')")
os.chdir("/tmp/")
print(f"Current working directory: {os.getcwd()}")
print("Create a single directory using os.mkdir(<path>)")
os.removedirs("/tmp/new_dir")
print("Creating /tmp/new_dir/")
os.mkdir("/tmp/new_dir")
print("Changing to the new dir")
os.chdir("/tmp/new_dir")
print(f"Where are we?: {os.getcwd()}")
print("Creating multiple directory hierarchy using os.makedirs(<path/to/)")
print("Creating /tmp/new_dir/dir1/dir2/")
os.makedirs("/tmp/new_dir/dir1/dir2")
os.chdir("/tmp/new_dir/dir1/dir2")
print(f"Where are we?: {os.getcwd()}")
