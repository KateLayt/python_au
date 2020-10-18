class LeetCodeSolution:
    def __init__ (self, title, link, code):
        self.title = title.split('. ')[1].rstrip('\n')
        self.link = link[1:].rstrip('\n')
        self.code = "``` python \n {}\n ```".format('\n'.join(map(lambda x: x.strip('\n')[4:], code)))
    
    
    def get_md_title(self):
        return "## {}".format(self.title)
    
    
    def get_title_link(self):
        return "+ [{}](#{})".format(self.title, self.link[30:].rstrip('/'))

    
    def get_md_solution(self):
        return "\n{}\n\n[comment]: <> (Stop)\n\n{}\n\n{}\n\n{}".format(self.get_title_link(), self.get_md_title(), self.link, self.code)
        

def read_all_lines_from(filename):
    file = open(filename)
    result = file.readlines()
    file.close()
    return result


def write_with_title(filename, data):
    file = open(filename,"w")
    main_title = ''
    upper_next = True
    for letter in filename:
        if upper_next:
            main_title += letter.upper()
            upper_next = False
            continue
        if letter == '.':
            break
        if letter == '-':
            main_title += ' '
            upper_next = True
            continue
        main_title += letter
    file.write("# {}\n".format(main_title))
    file.write(data)
    file.close


def generate_md(input_filename,output_filename):
    in_new = read_all_lines_from(input_filename)
    newsource = LeetCodeSolution(in_new[0], in_new[1], in_new[3:])
    in_old = read_all_lines_from(output_filename)
    write_with_title(output_filename, merge_solutions(in_old, newsource.get_md_solution()))


def merge_solutions(old, new):
    old_splitted = ['', '']
    ifStop = False
    ifTitle = False
    if old != '':
        ifTitle = True
    for line_index, line in enumerate(old):
        if ifTitle and line_index == 0:
            continue
        if '[comment]: <> (Stop)' in line:
            ifStop = True
            continue
        if ifStop:
            old_splitted[1] += line
        else:
            old_splitted[0] += line
    if len(old_splitted) == 1:
        return new
    return '{}{}{}'.format(old_splitted[0], new, old_splitted[1])


generate_md(input('Введите имя файла решения .py'), input('Введите имя генерируемого файла .md'))
