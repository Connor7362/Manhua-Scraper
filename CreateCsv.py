import csv

"""Takes a dictionary and creates a csv using the dictionary"""
def write_csv(content):
    with open('writeTest.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='*')
        for mh in content:
            title = mh + '*'
            chapter_list = content[mh]
            link = ""
            # print(chapter_list)
            for i in range(len(chapter_list) - 1):
                link += chapter_list[i] + '*'
            link += chapter_list[len(chapter_list) - 1]
            writer.writerow([title + link])
