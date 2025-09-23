import inspect

def callingInfo():
    current_frame = inspect.currentframe()
    
    try:
        caller_frame = current_frame.f_back

        frame_info = inspect.getframeinfo(caller_frame)

        class_name = ""
        method_name = frame_info.function

        if 'self' in caller_frame.f_locals:
            class_name = caller_frame.f_locals['self'].__class__.__name__
        elif 'cls' in caller_frame.f_locals:
            class_name = caller_frame.f_locals['cls'].__name__
        
        return class_name, method_name, frame_info.lineno
        
    finally:
        del current_frame
        if 'caller_frame' in locals():
            del caller_frame

# Пример использования
class TestClass:
    def test_method(self):
        info = callingInfo()
        print(info)
    
    @classmethod
    def test_class_method(cls):
        info = callingInfo()
        print(info)

def test_function():
    info = callingInfo()
    print(info)

if __name__ == "__main__":
    obj = TestClass()
    obj.test_method()
    TestClass.test_class_method()
    test_function()
    info = callingInfo()
    print(info)
info = callingInfo()
print(info)