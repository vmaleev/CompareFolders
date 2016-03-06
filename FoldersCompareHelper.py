import DataStructureClasses


class FoldersComparer:
    def __init__(self, sourse_folders, target_folders):
        self.sourse_folders = sourse_folders
        self.target_folders = target_folders
        self.same_folders = None
        self.different_folders = None
        self.to_delete_folders = None
        self.to_create_folders = None
        self.to_delete_files = None
        self.to_create_files = None
        self.__compare_folders()
        self.__compare_files()

    def __compare_folders(self):
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

    def __compare_files(self):
        folders_for_source = [f1 for f1 in self.sourse_folders if f1 in self.different_folders]
        folders_for_target = [f1 for f1 in self.target_folders if f1 in self.different_folders]
        for s_folder in folders_for_source:
            for t_folder in folders_for_target:
                if s_folder == t_folder:
                    self.to_delete_files = [file for file in t_folder.files if file not in s_folder.files]
                    self.to_create_files = [file for file in s_folder.files if file not in t_folder.files]
