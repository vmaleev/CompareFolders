import DataStructureClasses
import os
import hashlib


def get_modification_time(filename):
    st = os.stat(filename)
    return st.st_mtime


def get_file_size(filename):
    st = os.stat(filename)
    return st.st_size


class ReadFolderStructure:
    def __init__(self, path):
        self.path = path

    def read_structure(self, current_path=None) -> DataStructureClasses.Folder:
        if current_path is None:
            current_path = self.path
        files_in_folder = []
        sub_folders_in_folder = []
        md5string = []
        folder = DataStructureClasses.Folder(os.path.split(current_path)[-1], os.path.relpath(current_path, self.path),
                                             current_path)
        for dir_entry in os.listdir(current_path):
            dir_entry_path = os.path.join(current_path, dir_entry)
            if os.path.isfile(dir_entry_path):
                file = DataStructureClasses.File(dir_entry,
                                                 os.path.relpath(dir_entry_path, current_path),
                                                 dir_entry_path,
                                                 get_modification_time(dir_entry_path),
                                                 get_file_size(dir_entry_path))
                files_in_folder.append(file)
                md5string.append(str(file.name))
                md5string.append(str(file.modification_date))
                md5string.append(str(file.size))
            elif os.path.isdir(dir_entry_path):
                sub_folder = self.read_structure(dir_entry_path)
                sub_folders_in_folder.append(sub_folder)
        folder.files = files_in_folder
        folder.sub_folders = sub_folders_in_folder
        folder.files_md5 = hashlib.md5(''.join(md5string).encode()).hexdigest()
        return folder
