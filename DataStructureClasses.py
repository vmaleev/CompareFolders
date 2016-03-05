class File:
    def __init__(self, name, relative_path, fullPath, modif_date, size):
        self.name = name
        self.relative_path = relative_path
        self.fullPath = fullPath
        self.modification_date = modif_date
        self.size = size

    def __eq__ (self, other):
        return self.name == other.name \
               and self.relative_path == other.relativePath \
               and self.size == other.size \
               and self.modification_date == other.modification_date

    def __ne__ (self, other):
        return not self.__eq__(other)



class Folder:
    def __init__(self, name, relative_path, full_path, files=None, files_md5=None, sub_folders=None):
        self.name = name
        self.relative_path = relative_path
        self.fullPath = full_path
        self.files = files
        self.sub_folders = sub_folders
        self.files_md5 = files_md5

    def __eq__ (self, other):
        return self.name == other.name and self.relative_path == other.relative_path

    def __ne__ (self, other):
        return not self.__eq__(other)


def is_folders_equals(folder1: Folder, folder2: Folder) -> bool:
    result = True
    if folder1.name != folder2.name \
            or folder1.relative_path != folder2.relative_path \
            or folder1.files_md5 != folder2.files_md5:
        result = False
    return result


def is_files_equals(file1: File, file2: File) -> bool:
    result = True
    if file1.name != file2.name \
            or file1.relative_path != file2.relative_path \
            or file1.size != file2.size \
            or file1.modification_date != file2.modification_date:
        result = False
    return result
