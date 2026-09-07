class Graph:
    LIMIT_Y = [0, 10]
    
    def set_data(self, data):
        self.data = data
    
    def draw(self):
        result = [str(x) for x in self.data if self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1]]
        print(' '.join(result))

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()  