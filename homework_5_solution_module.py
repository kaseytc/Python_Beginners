def AskForFileName():
    '''
    ask the user for the name of the input file
    '''
    ask_for_file_name = True
    while ask_for_file_name:
        file_name = raw_input('''Please input a file name: ''')
        try:
            file_open = open(file_name)
            ask_for_file_name = False
            file_open.close()
            return file_name
        except IOError:
            print 'File cannot be found!'


def ReadFileContents(file_name):
    '''
    open the file and read all the lines in the file into memory
    '''
    try:
        input_file = open(file_name)
        all_file_contents = input_file.readlines()
        input_file.close()
        return all_file_contents
    except IOError:
        print 'File cannot be found!'


def BuildHeadList(all_file_contents):
    '''
    loop over the variable populated in ReadFileContents
    and append to another list called head_list the header information from the file.
    These are the lines from the top of the file to the lines that start with the word ATOM.
    '''
    head_list = []
    for line in all_file_contents:
        if not line.startswith('ATOM'):
            head_list.append(line)
        if line.startswith('ATOM'):
            break
    return head_list


def BuildAtomList(all_file_contents):
    '''
    loop over the variable populated in ReadFileContents
    and append to another list called atom_list all the lines
    that begin with ATOM and ONLY these lines.
    '''
    atom_list = []
    for line in all_file_contents:
        if line.startswith('ATOM'):
            atom_list.append(line)
    return atom_list


def BuildTailList(all_file_contents):
    '''
    loop over the variable populated in ReadFileContents
    and append to another list called tail_list all the lines
    that are below those that begin with ATOM (the lines left over).
    '''
    tail_list = []
    for line in reversed(all_file_contents):
        if not line.startswith('ATOM'):
            tail_list.append(line)
        if line.startswith('ATOM'):
            break
    tail_list.reverse()
    return tail_list


def WriteNewFile(head_list, atom_list, tail_list):
    '''
    take the three lists created above (head_list, atom_list, tail_list) as arguments
    and will write these lists to an output file called output.txt
    that should look exactly like 1JKB.pdb when finished writing.
    '''
    output_file = open('output.txt', 'w')
    for line in head_list:
        output_file.write(line)
    for line in atom_list:
        output_file.write(line)
    for line in tail_list:
        output_file.write(line)
    output_file.close()
    return 'output.txt'


if __name__=='__main__':
    all_file_contents = ReadFileContents('1JKB.pdb')
    print type(all_file_contents)

    head_list = BuildHeadList(all_file_contents)
    print type(head_list)

    atom_list = BuildAtomList(all_file_contents)
    print type(atom_list)

    tail_list = BuildTailList(all_file_contents)
    print type(tail_list)
