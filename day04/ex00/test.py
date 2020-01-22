from FileLoader import FileLoader

loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")
#print(data)
loader.display(data, -2)
