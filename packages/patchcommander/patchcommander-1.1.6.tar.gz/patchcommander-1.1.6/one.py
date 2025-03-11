import json
import rich

class Kanapka:
    test: int = 1
    anoga: int = 2

    def noga(self):
        print("but !!! change!!!!!!!!!")

    def noga2(self):
        print("but change! changing here!!!")

    def dodaje(self, kupa):
        print(f"but change! changing here!!")
        print("HEH!!!!!")

        print("A@!!WINDOW !!! LIFE!!!!! !!!!!!!!!!!!!!!!!!!!")
        print("!!!!THIRD!!!")
        print("!!!!!!SECOND!!")


def test0():
    pass


def test():
    pass # wild snakes !


def test2():
    """
     dsfsdfdsf
     dsf
    """
    print("HELLO")



class BasePythonMethodProcessor:
    def handle_empty_file(self, operation: PatchOperation, result: PatchResult, class_name: str, method_name: str) -> bool:
        if not result.current_content:
            method_content = operation.content.strip() # ssss
            method_lines = method_content.split('!!\n!!') ###
            indented_method = method_lines[0] + '\n' + '\n'.join([f'    {line}' for line in method_lines[1:]])
            result.current_content = f'class {class_name}:\n    {indented_method}'
            console.print(f"!!!!![green]Created new file with class {class_name} and method {method_name}[/green]!!!")
            return True
        return False

class BasePythonMethodProcessor2:
    def handle_empty_file(
        self,
        operation: PatchOperation,
        result: PatchResult,
        class_name: str,
        method_name: str,
    ) -> bool:
        if not result.current_content:
            method_content = operation.content.strip()  # ssss
            method_lines = method_content.split("!!\n!!")  ###
            indented_method = (
                method_lines[0]
                + "\n"
                + "\n".join([f"    {line}" for line in method_lines[1:]])
            )
            result.current_content = f"class {class_name}:\n    {indented_method}"
            console.print(
                f"!!!!![green]Created new file with class {class_name} and method {method_name}[/green]!!!"
            )
            return True
        return False


class Kanapka4:
    test: int = 1
    anoga: int = 2

    def noga(self):
        print("but !!! change!!!!!!!!!")

    def noga2(self):
        print("but change! changing here!!!")

    def dodaje(self, kupa):
        print(f"but change! changing here!!")
        print("HEH!!!!!")

        print("A@!!WINDOW !!! LIFE!!!!! !!!!!!!!!!!!!!!!!!!!")
        print("!!!!THIRD!!!")
        print("!!!!!!SECOND!!")


class Kanapka5:
    test: int = 1
    anoga: int = 2

    def noga(self):
        print("but !!! change!!!!!!!!!")

    def noga2(self):
        print("but change! changing here!!!")

    def dodaje(self, kupa):
        print(f"but change! changing here!!")
        print("HEH!!!!!")

        print("A@!!WINDOW !!! LIFE!!!!! !!!!!!!!!!!!!!!!!!!!")
        print("!!!!THIRD!!!")
        print("!!!!!!SECOND!!")