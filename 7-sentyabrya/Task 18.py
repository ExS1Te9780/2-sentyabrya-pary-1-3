class Graph:
    def __init__(self, data):
        self.data = data.copy() if data else []
        self.is_show = True
    
    def set_data(self, data):
        self.data = data.copy() if data else []
    
    def show_table(self):
        if not self.is_show:
            print("Отображение данных закрыто")
            return
        print(' '.join(map(str, self.data)))
    
    def show_graph(self):
        if not self.is_show:
            print("Отображение данных закрыто")
            return
        print(f"Графическое отображение данных: {' '.join(map(str, self.data))}")
    
    def show_bar(self):
        if not self.is_show:
            print("Отображение данных закрыто")
            return
        print(f"Столбчатая диаграмма: {' '.join(map(str, self.data))}")
    
    def set_show(self, fl_show):
        self.is_show = fl_show

data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()