with open('resume_summery.txt', 'r') as f:
    file_contents = f.read()
    line = file_contents.split('\n')

    for i in range(5):
        print(line[i])