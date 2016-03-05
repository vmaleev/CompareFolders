from DataStructureClasses import File
from DataStructureClasses import Folder
import DataStructureClasses


class FoldersComparer:
    def __init__(self, sourse_folders, target_folders):
        self.sourse_folders = sourse_folders
        self.target_folders = target_folders
        self.same_folders = None
        self.different_folders = None
        self.to_delete_folders = None
        self.to_create_folders = None
        self.different_files = None
        self.compare_folders()

    def compare_folders(self):
        self.same_folders = [f1 for f1 in self.sourse_folders for f2 in self.target_folders
                             if DataStructureClasses.is_folders_equals(f1, f2)]
        self.to_create_folders = [f1 for f1 in self.sourse_folders if f1 not in self.target_folders
                                  and f1.relative_path != '.']
        self.to_delete_folders = [f2 for f2 in self.target_folders if f2 not in self.sourse_folders
                                  and f2.relative_path != '.']
        self.different_folders = [f1 for f1 in self.sourse_folders
                                  if f1 not in self.same_folders and
                                  f1 not in self.to_create_folders and
                                  f1 not in self.to_delete_folders]
