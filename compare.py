import AsuraAPI
import CsvReader
import CreateCsv

"""Takes the dictionary created by the API and the current dictionary then updates the current dictionary with the 
new links"""
def compare_csv():
    files = ["test.csv"]

    asura = AsuraAPI
    c = CsvReader
    write = CreateCsv

    output = asura.get_page()
    updatedList = asura.get_chapter(output)  # is the list with potential updated manhua
    currList = c.read_csv(["writeTest.csv"])  # old list that needs to be compared to needs to be as a list
    updates = []

    for comic in updatedList:
        if (comic in currList) and (len(currList[comic]) < len(updatedList[comic])):
            updatedChapters = len(updatedList[comic])
            currChapters = len(currList[comic])
            newChapters = updatedChapters - currChapters
            for i in range(newChapters)[::-1]:
                currList[comic].insert(0, updatedList[comic][i])
            updates.append((comic, newChapters, False,currList[comic][newChapters]))
        elif comic not in currList:
            currList[comic] = updatedList[comic]
            updates.append((comic, 0, True, currList[comic][len(currList[comic])-1]))

    write.write_csv(currList)
    print(updates)
    return updates
