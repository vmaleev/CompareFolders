import ReadFolderHelper
import FoldersCompareHelper


reader1 = ReadFolderHelper.ReadFolderStructure('/Users/vmaleev/Temp/FolderTest1')
structure1 = reader1.read_structure()
folder_list1 = reader1.get_folder_list(structure1)

reader2 = ReadFolderHelper.ReadFolderStructure('/Users/vmaleev/Temp/FolderTest2')
structure2 = reader2.read_structure()
folder_list2 = reader2.get_folder_list(structure2)

object = FoldersCompareHelper.FoldersComparer(folder_list1, folder_list2)


print(structure1.name)