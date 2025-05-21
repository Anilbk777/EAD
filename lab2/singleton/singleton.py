

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating a new instance")
            cls._instance = super(Singleton, cls).__new__(cls)
            
            cls._instance.value = 0
        else:
            print("Using existing instance")
        return cls._instance
    
    def increment(self):
        self.value += 1
        return self.value


if __name__ == "__main__":
   
    s1 = Singleton()
    print(f"s1 value: {s1.value}")
    
    s1.increment()
    print(f"s1 value after increment: {s1.value}")
    
    s2 = Singleton()
    print(f"s2 value: {s2.value}")
    
    print(f"Are s1 and s2 the same object? {s1 is s2}")
    
    s2.increment()
    print(f"s1 value after s2 increment: {s1.value}")
    print(f"s2 value after s2 increment: {s2.value}")