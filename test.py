import ReadFolderHelper


reader = ReadFolderHelper.ReadFolderStructure('/Users/vmaleev/VagrantEnv')


structure = reader.read_structure()

print(structure.name)