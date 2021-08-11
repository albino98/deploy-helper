import os
import shutil
from shutil import copyfile, copy


def copyFilesToDir(source_files, dest):
    result = {"error": False, "message": "Deploy executed successfully."}
    try:
        if len(source_files) < 1 or dest is None or dest == "":
            result = {"error": True, "message": "Deploy not executed. Source files or desination are not present. "}
            return result
        # create dest foldes if not exists
        if not os.path.exists(dest):
            os.makedirs(dest)
        # copy files
        for file in source_files:
            copy(file, dest)

    # If source and destination are same
    except shutil.SameFileError:
        result = {"error": True, "message": "Source and destination represents the same file."}
        print("Source and destination represents the same file.")

    # If file exists.
    except FileExistsError:
        result = {"error": True, "message": "One or more file already exists in destination directory."}
        print("One or more file already exists in destination directory.")

    # If there is any permission issue
    except PermissionError:
        result = {"error": True, "message": "Permission denied."}
        print("Permission denied.")

    # For other errors
    except Exception as ex:
        result = {"error": True, "message": str(ex)}
        print("Error occurred while copying files: " + str(ex))

    return result