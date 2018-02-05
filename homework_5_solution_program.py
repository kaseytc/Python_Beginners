import homework_5_solution_module as module


def Run():
    '''
    input file 1JKB.pdb and compare with output.txt file
    '''
    file_1 = module.AskForFileName()
    all_file_contents = module.ReadFileContents(file_1)
    head_list = module.BuildHeadList(all_file_contents)
    atom_list = module.BuildAtomList(all_file_contents)
    tail_list = module.BuildTailList(all_file_contents)
    file_2 = module.WriteNewFile(head_list, atom_list, tail_list)
    DifferenceTwoFiles(file_1, file_2)


def DifferenceTwoFiles(file_1, file_2):
    '''
    open both files reading in all lines into two separate variables
    and compare the two to determine if the files are different.
    '''
    diff_list = []
    try:
        file_01 = open(file_1)
        file_02 = open(file_2)
    except IOError:
        print 'Files cannot be found!'
    else:
        file_01_content = file_01.readlines()
        file_02_content = file_02.readlines()
        for i, line in enumerate(file_01_content):
            if line != file_02_content[i]:
                diff_list.append(line)
        print 'If the length of the difference list is 0, then the input file and the output file are the same; ' \
              'otherwise, these two files are different.'
        print 'The result of the length of the difference list is: ' + str(len(diff_list))
        file_01.close()
        file_02.close()


if __name__ == '__main__':
    Run()

