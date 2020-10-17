class LeetCodeSolution:
    def __init__ (self, title, link, code):
        self.number = title.split('. ')[0].lstrip('#')
        self.title = title.split('. ')[1].rstrip('\n')
        self.md_title = "# {}".format(self.title)
        self.link = link[1:]
        self.special_link = "+ [{}](#{})".format(self.title, self.link[30:].rstrip('/\n'))
        self.md_link = 'Problem {}. <a href="{}">Link to the page </a>'.format(self.number, link[1:].rstrip('\n'))
        self.code = "``` python \n {}\n ```".format('\n'.join(map(lambda x: x.strip('\n')[4:], code)))
    
    
    def get_md_solution(self):
        return "{}\n\n[comment]: <> (Stop)\n\n{}\n\n{}\n\n{}".format(self.special_link, self.md_title, self.md_link, self.code)
        

def read_all_lines_from(filename):
    file = open(filename)
    result = file.readlines()
    file.close()
    return result


def write(filename, data):
    file = open(filename,"w")
    file.write(data)
    file.close


def generate_md(input,output):
    in_new = read_all_lines_from(input)
    newsource = LeetCodeSolution(in_new[0], in_new[1], in_new[3:])
    in_old = read_all_lines_from(output)
    write(output, merge_solutions(in_old, newsource.get_md_solution()))


def merge_solutions(old, new):
    old_splitted = ['', '']
    ifStop = False
    for string in old:
        if '[comment]: <> (Stop)' in string:
            ifStop = True
            continue
        if ifStop:
            old_splitted[1] += string
        else:
            old_splitted[0] += string
    if len(old_splitted) == 1:
        return new
    return '{}{}{}'.format(old_splitted[0], new, old_splitted[1])


generate_md(input('Введите имя файла решения .py'), input('Введите имя генерируемого файла .md'))