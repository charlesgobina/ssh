
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluation_stack = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        if cell in self._evaluation_stack:
            return "#Circular"
        
        self._evaluation_stack.add(cell)
        value = self.get(cell)
        
        try:
            if value.startswith("="):
                if value[1:].startswith("'") and value[-1] == "'":
                    self._evaluation_stack.remove(cell)
                    return value[2:-1]
                elif value[1:].isdigit():
                    self._evaluation_stack.remove(cell)
                    return int(value[1:])
                elif value[1:] in self._cells:
                    result = self.evaluate(value[1:])
                    self._evaluation_stack.remove(cell)
                    return result
                else:
                    self._evaluation_stack.remove(cell)
                    return '#Error'
            if value.isdigit():
                self._evaluation_stack.remove(cell)
                return int(value)
            if value.startswith("'") and value.endswith("'"):
                self._evaluation_stack.remove(cell)
                return value[1:-1]
            try:
                # Evaluate arithmetic expressions
                result = eval(value, {}, {})
                if isinstance(result, int):
                    self._evaluation_stack.remove(cell)
                    return result
                else:
                    self._evaluation_stack.remove(cell)
                    return '#Error'
            except:
                if value.startswith("'") and not value.endswith("'"):
                    self._evaluation_stack.remove(cell)
                    return '#Error'
                self._evaluation_stack.remove(cell)
                return value
        except Exception as e:
            self._evaluation_stack.remove(cell)
            raise e

