class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    total_mem_slots = 4
    
    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.mem_slots = list(mem_slots[:self.total_mem_slots])
    
    def get_config(self):
        config = [
            f'Материнская плата: {self.name}',
            f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
            f'Слотов памяти: {self.total_mem_slots}'
        ]
        
        memory_str = 'Память: '
        memory_parts = []
        for mem in self.mem_slots:
            memory_parts.append(f'{mem.name} - {mem.volume}')
        memory_str += '; '.join(memory_parts)
        config.append(memory_str)
        
        return config

cpu = CPU('Intel Core i7', 3200)
mem1 = Memory('Kingston', 8192)
mem2 = Memory('Samsung', 8192)
mb = MotherBoard('ASUS Prime', cpu, mem1, mem2)