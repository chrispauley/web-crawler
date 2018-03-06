# Python Web Crawler
# Each website is a new project with its own folder
import os

def create_project(directory):
    if not os.path.exists(directory):
        print('Creating the project directory: ' + directory)
        os.makedirs(directory)

# Create queued and crawled files if they do not exist
def create_data_files(projectName, baseUrl):
    queue = projectName + '/queue.txt'
    crawled = projectName + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, baseUrl)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# Add data to an exiting file
def append_to_file(path, data):
    f = open(path, 'a')
    file.write(data + '\n')
    f.close()

# delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()

# Read a file and convert each line to a set of items
def file_to_set(fileName):
    results = set()
    f = open(fileName, 'rt')
    for line in f:
        results.add(line.replace('\n',''))
    f.close()
    return results

# Write set into a file
def set_to_file(links, fileName):
    # msg = 'In set_to_file for '
    # print(fileName)
    # print(links)
    # print(fileName)
    f = open(fileName, "w")
    for link in sorted(links):
        # print(link+'\n')
        f.write(link+"\n")
    f.close()

# print("Test")
# PROJECT_NAME = 'theproject'
# PROJECT_BASE =  PROJECT_NAME + '.com'
# test_set = set()
# test_set.add(PROJECT_BASE)
#
# create_project(PROJECT_NAME)
# create_data_files(PROJECT_NAME, PROJECT_NAME + '.com')
# set_to_file(test_set, PROJECT_NAME + '/queue.txt')
# test_read = file_to_set(PROJECT_NAME + '/queue.txt')
# print(test_read)
