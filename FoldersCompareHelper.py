from DataStructureClasses import File
from DataStructureClasses import Folder
import DataStructureClasses

class FoldersComparer:
    def __init__(self, sourse_folder: list(Folder), target_folder: list(Folder)):
        self.sourse_folder = sourse_folder
        self.target_folder = target_folder
        self.same_folders = None
        self.different_folders = None
        self.to_delete_folders = None
        self.to_create_folders = None
        self.different_files = None
        self.compare_folders()


    def compare_folders(self):
        self.same_folders = [f1 for f1 in self.sourse_folder for f2 in self.target_folder
                             if DataStructureClasses.is_folders_equals(f1, f2)]
        #FIXED: Fix it - comparer works over MD5 - but it should work over name and relative path
        self.to_create_folders = [f1 for f1 in self.sourse_folder if f1 not in self.target_folder]
        self.to_delete_folders = [f2 for f2 in self.target_folder if f2 not in self.sourse_folder]




