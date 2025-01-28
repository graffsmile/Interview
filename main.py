class Stack:
    """Создаем класс Stack со следующими методами:
    is_empty — проверка стека на пустоту. Метод возвращает True или False;
    push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
    pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
    peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
    size — возвращает количество элементов в стеке
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items += item

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError('stack is empty')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError('stack is empty')


    def size(self):
        return len(self.items)


def is_balance(sequence_parentheses):
    stack = Stack()
    sequence_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for parentheses in sequence_parentheses:
        if parentheses in '({[':
            stack.push(parentheses)
        elif parentheses in ')}]':
            if stack.is_empty():
                return False
            if stack.pop() != sequence_dict[parentheses]:
                return False
    return stack.is_empty()

def sequences_test(sequence_parentheses):
    result = is_balance(sequence_parentheses)
    if result:
        return 'Сбалансировано'
    else:
        return 'Несбалансированно'



if __name__ == '__main__':
    sequences_list = [
        '(((([{}]))))',
        '[([])((([[[]]])))]',
        '{()}',
        '{{[()]}}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]'
    ]
    for sequence in sequences_list:
        print(f' Последовательность {sequence}: {sequences_test(sequence)}')