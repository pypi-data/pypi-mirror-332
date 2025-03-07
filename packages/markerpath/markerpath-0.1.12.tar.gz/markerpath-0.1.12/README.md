Usage:

1. Create a file with extension .marker in your base directory.  
2. Contents of this file
    an empty file
    OR
    lines of path relative to the base directory marked by the marker file. These paths will be appended to sys.path
    OR
    add_all_python_paths

3. In your python file with main anywhere under the base directory.
    import markerpath

    3.1 This will create a environment variable 
        MARKERPATH=<the base directory>

    3.2 Access this as such
        import os
        marker_home=os.environ["MARKERPATH"]


