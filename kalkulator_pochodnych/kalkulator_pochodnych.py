# na początku chciałem podejść ambitnie do zadania, ale po czasie okazało się bardzo wymagające, z tego
# względu przy formatowaniu działania uwzględniam np. funkcje arcsin, ale program nie policzy z niej pochodnej.
# Ale nie chciałem po prostu usuwać czegoś co zrobiłem
# W każdym ważnym moim zdaniem miejscu, wstawiam komentarze

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def equation_formatting(text):
    """Funckja formatująca odpowiednio działanie matematyczne.
    :param text: działanie matematyczne.
    :return: Lista z elementami działania
    """
    special_function = ['sin', 'cos', 'tan', 'cot', 'log', 'exp', 'arcsin', 'arccos', 'arctan', 'arccot', 'sqrt']
    operations = ['-', '+', '*', '/', '^']
    values = '0123456789.'
    if text[0] == '(' and text[-1] == ')': # sprawdzam czy nawiasy są wstawione na początku i na końcu działania.
        # Ponieważ aby program działał nawiasy muszą być na początku i na końcu,
        # ale jeżeli nie ma operacji dwuagrumentowych, to nawiasów ma nie być
        if '+' not in text and '-' not in text and '*' not in text and '/' not in text and '^' not in text:
            text = text[1:-1]
    else:
        if '+' in text or '-' in text or '*' in text or '/' in text or '^' in text:
            text = '(' + text + ')'
    component_list = []
    text = text.replace(" ", "").replace("**", "^") # zamieniam potęgowanie, gdyby użytkownik wpisał w pythonowym języku i usuwam spacje
    index_number = 0
    while index_number + 1 <= len(text): # Program toleruje nie wpisywanie mnożenia między wyrażeniami np. '2x'
        if text[index_number] == 'x' and text[index_number - 1:index_number + 2] != 'exp' and index_number + 1 != len(
                text) and index_number != 0:
            if (text[index_number - 1] in operations and text[index_number + 1] in operations) or (
                    text[index_number - 6:index_number] in special_function or text[
                                                                               index_number - 3:index_number] in special_function or text[
                                                                                                                                     index_number - 4:index_number] == 'sqrt') or \
                    (text[index_number - 1] == '(' and text[index_number + 1] == ')'):
                index_number += 1
            elif text[index_number - 1] not in operations and text[index_number + 1] not in operations and text[
                index_number - 1] != '(' and text[index_number + 1] != ')':
                text = text[:index_number] + '*x*' + text[index_number + 1:]
                index_number += 4
            elif text[index_number - 1] not in operations and text[index_number - 1] != '(':
                text = text[:index_number] + '*' + text[index_number:]
                index_number += 2
            elif text[index_number + 1] not in operations and text[index_number + 1] != ')':
                text = text[:index_number + 1] + '*' + text[index_number + 1:]
                index_number += 2
            else:
                index_number += 1
        elif text[index_number] == 'x' and text[index_number - 1:index_number + 2] != 'exp' and index_number + 1 == len(
                text):
            if text[index_number - 1] in operations or (text[index_number - 6:index_number] in special_function or text[
                                                                                                                   index_number - 3:index_number] in special_function or text[
                                                                                                                                                                         index_number - 4:index_number] == 'sqrt'):
                index_number += 1
            else:
                text = text[:index_number] + '*x'
                index_number += 2
        elif text[index_number] == 'x' and text[index_number - 1:index_number + 2] != 'exp' and index_number == 0:
            if text[1] in operations:
                index_number += 1
            else:
                text = text[0] + '*' + text[1:]
                index_number += 2
        else:
            index_number += 1
    text = text.replace('(x)', '(1*x)')
    index_number = 0
    while index_number + 1 <= len(text): # wstawiam po kolei każdy element do listy
        if text[index_number:index_number + 6] in special_function:
            component_list.append(text[index_number:index_number + 6])
            index_number += 6
        elif text[index_number:index_number + 4] == 'sqrt':
            component_list.append('sqrt')
            index_number += 4
        elif text[index_number:index_number + 3] in special_function:
            component_list.append(text[index_number:index_number + 3])
            index_number += 3
        else:
            if text[index_number] in values and index_number + 1 <= len(text) and text[index_number + 1] in values:
                temp_index = index_number
                while text[index_number] in values and index_number + 1 <= len(text):
                    index_number += 1
                component_list.append(text[temp_index:index_number])
            else:
                component_list.append(text[index_number])
                index_number += 1
    index_number = 0
    while index_number < len(component_list): # dodaję znak mnożenia między na przykład 5sin(x)
        if index_number != 0 and component_list[index_number] in special_function:
            if component_list[index_number - 1] in operations or component_list[index_number - 1] == '(':
                index_number += 1
            else:
                component_list.insert(index_number, '*')
                index_number += 2
        elif component_list[index_number] == 'x' and index_number + 1 != len(component_list) and component_list[
            index_number - 1] in special_function and component_list[index_number + 1] not in operations and \
                component_list[index_number + 1] != ')':
            component_list.insert(index_number + 1, '*')
            index_number += 2
        else:
            index_number += 1
    index_number = 0
    while index_number < len(component_list):
        if component_list[index_number] in special_function and index_number != 0:
            if component_list[index_number - 1] not in operations and component_list[
                index_number - 1] not in special_function and component_list[index_number - 1] != '(':
                component_list.insert(index_number, '*')
                index_number += 2
            else:
                index_number += 1
        else:
            index_number += 1
    index_number = 0
    while index_number < len(component_list):
        if component_list[index_number] == '(':
            component_list[index_number] = '['
            index_number += 1
        elif component_list[index_number] == ')':
            component_list[index_number] = ']'
            index_number += 1
        else:
            index_number += 1
    index_number = 0
    # Przy pisaniu funkcji budującej drzewo wyrażenia, zmodyfikowałem kod z wykładu 'build_parse_tree', w tym celu
    # muszę zmodyfikować listę którą mam do tego momentu kodu. Dla funkcji złożonej muszę pousuwać nawiasy z pomiędzy
    # kolejnymi składowymi funkcji złożonej i dodać jeden nawias do zamknięcia funkcji. Dla przykładu:
    # dla wyrażenia wyjściowego: '(cos(exp(x)))'
    # w tym momencie będzie: ['cos','[','exp','[','1','*','x',']',']']
    # po najbliższych dwóch pętlach będzie: ['cos', 'exp', '[', '1', '*', 'x', ']', ']', ']']
    while index_number < len(component_list):
        if component_list[index_number] in special_function and index_number + 2 < len(component_list):
            if component_list[index_number + 2] in special_function:
                component_list.pop(index_number + 1)
        index_number += 1
    index_number = 0
    while index_number < len(component_list):
        if component_list[index_number] in special_function:
            if component_list[index_number + 1] not in special_function:
                component_list.insert(index_number + 5, ']')
        index_number += 1
    return component_list


class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def __str__(self, if_main=True):
        left_child = self.get_left_child()
        right_child = self.get_right_child()
        if if_main:
            if left_child and right_child:
                return [left_child.__str__(False), self.get_root_val(), right_child.__str__(False)].__str__()
            elif left_child:
                return [left_child.__str__(False), self.get_root_val(), []].__str__()
            elif right_child:
                return [[], self.get_root_val(), right_child.__str__(False)].__str__()
            else:
                return [self.get_root_val()].__str__()
        else:
            if left_child and right_child:
                return [left_child.__str__(False), self.get_root_val(), right_child.__str__(False)]
            elif left_child:
                return [left_child.__str__(False), self.get_root_val(), []]
            elif right_child:
                return [[], self.get_root_val(), right_child.__str__(False)]
            else:
                return [self.get_root_val()]

    def __copy__(self):
        result = BinaryTree(self.get_root_val())
        if self.get_right_child():
            result.right_child = self.get_right_child().__copy__()
        if self.get_left_child():
            result.left_child = self.get_left_child().__copy__()
        return result


def build_parse_tree(formula_tree):
    """Funkcja budująca drzewo binarne wyrażenia matematycznego.
    :param formula_tree: Lista elementów do sparsowania.
    """
    formula_tree = equation_formatting(formula_tree)
    special_function = ['sin', 'cos', 'tan', 'cot', 'log', 'exp', 'arcsin', 'arccos', 'arctan', 'arccot', 'sqrt']
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in formula_tree:
        if i == '[':
            currentTree.insert_left('')
            pStack.push(currentTree)
            currentTree = currentTree.get_left_child()
        elif i not in ['+', '-', '*', '/', ']', '^'] and i not in special_function:
            currentTree.set_root_val(i)
            parent = pStack.pop()
            currentTree = parent
        elif i in special_function:
            currentTree.set_root_val(i)
            currentTree.insert_right('')
            pStack.push(currentTree)
            currentTree = currentTree.get_right_child()
        elif i in ['+', '-', '*', '/', '^']:
            currentTree.set_root_val(i)
            currentTree.insert_right('')
            pStack.push(currentTree)
            currentTree = currentTree.get_right_child()
        elif i == ']':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def formulas_of_derivative(function):
    """Funkcja zwracająca drzewo pochodnej wyrażenia.
    :param function: rodzaj funkcji.
    """
    if function == 'sin':
        return BinaryTree('cos')
    elif function == 'cos':
        tree = BinaryTree('*')
        tree.left_child = BinaryTree('-1')
        tree.right_child = BinaryTree('sin')
        return tree
    elif function == 'log':
        tree = BinaryTree('/')
        tree.left_child = BinaryTree('1')
        return tree
    elif function == 'exp':
        return BinaryTree('exp')


def devirative_tree(formula):
    """Funkcja budująca drzewo pochodnej wyrażenia matematycznego.
    :param formula: drzewo wyrażenia metematycznego.
    """
    operators = ['+', '-', '*', '/', '^']
    special_function = ['sin', 'cos', 'tan', 'log', 'exp', 'arcsin', 'arccos', 'arctan', 'sqrt']
    if formula.get_root_val() in operators:
        if formula.get_root_val() == '+':
            tree = BinaryTree(formula.get_root_val())
            tree.left_child = devirative_tree(formula.get_left_child())
            tree.right_child = devirative_tree(formula.get_right_child())
            return tree
        elif formula.get_root_val() == '-':
            tree = BinaryTree(formula.get_root_val())
            tree.left_child = devirative_tree(formula.get_left_child())
            tree.right_child = devirative_tree(formula.get_right_child())
            return tree
        elif formula.get_root_val() == '*':
            pStack = Stack()
            tree = BinaryTree('+')
            tree.left_child = BinaryTree("*")
            current_tree = tree
            pStack.push(current_tree)
            current_tree = current_tree.get_left_child()
            current_tree.left_child = devirative_tree(formula.get_left_child().__copy__())
            current_tree.right_child = formula.get_right_child().__copy__()
            current_tree = pStack.pop()
            current_tree.right_child = BinaryTree('*')
            current_tree = current_tree.get_right_child()
            current_tree.left_child = formula.get_left_child().__copy__()
            current_tree.right_child = devirative_tree(formula.get_right_child()).__copy__()
            return tree
        elif formula.get_root_val() == '/':
            pStack = Stack()
            tree = BinaryTree('/')
            tree.right_child = BinaryTree("^")
            current_tree = tree
            pStack.push(current_tree)
            current_tree = current_tree.get_right_child()
            current_tree.left_child = formula.get_right_child().__copy__()
            current_tree.right_child = BinaryTree('2')
            current_tree = pStack.pop()
            current_tree.left_child = BinaryTree('-')
            current_tree = current_tree.get_left_child()
            current_tree.left_child = BinaryTree('*')
            current_tree.right_child = BinaryTree('*')
            pStack.push(current_tree)
            current_tree = current_tree.get_left_child()
            current_tree.left_child = devirative_tree(formula.get_left_child().__copy__())
            current_tree.right_child = formula.get_right_child().__copy__()
            current_tree = pStack.pop()
            current_tree = current_tree.get_right_child()
            current_tree.left_child = devirative_tree(formula.get_right_child().__copy__())
            current_tree.right_child = formula.get_left_child().__copy__()
            return tree
        elif formula.get_root_val() == '^':
            pStack = Stack()
            tree = BinaryTree('*')
            tree.left_child = BinaryTree("*")  # todo
            current_tree = tree
            pStack.push(current_tree)
            current_tree = current_tree.get_left_child()
            current_tree.left_child = formula.get_right_child().__copy__()
            current_tree.right_child = BinaryTree('^')
            pStack.push(current_tree)
            current_tree = current_tree.get_right_child()
            current_tree.left_child = formula.get_left_child().__copy__()
            current_tree.right_child = BinaryTree('-')
            pStack.push(current_tree)
            current_tree = current_tree.get_right_child()
            current_tree.left_child = formula.get_right_child().__copy__()
            current_tree.right_child = BinaryTree('1')
            current_tree = pStack.pop()
            current_tree = pStack.pop()
            current_tree = pStack.pop()
            current_tree.right_child = devirative_tree(formula.get_left_child().__copy__())
            return tree
    elif formula.get_root_val() in special_function:
        tree = BinaryTree('*')
        pStack = Stack()
        current_tree = tree
        pStack.push(current_tree)
        current_tree.right_child = formulas_of_derivative(formula.get_root_val())
        current_tree = current_tree.get_right_child()
        if current_tree.get_right_child() == None:
            current_tree.right_child = formula.get_right_child()
        else:
            current_tree.right_child.right_child = formula.get_right_child()
        current_tree = pStack.pop()
        current_tree.left_child = devirative_tree(formula.get_right_child())
        return tree
    elif formula.get_root_val() == 'x':
        return BinaryTree('1')
    else:
        return BinaryTree('0')

def prepare_string_for_devirative_tree(tree):
    """Funkcja zwracająca listę argumentów pochodnej funkcji.
    :param tree: drzewo pochoddnej.
    """
    operators = ['+', '-', '*', '/', '^']
    special_function = ['sin', 'cos', 'log', 'exp']
    if tree.get_root_val() in operators:
        return [prepare_string_for_devirative_tree(tree.get_left_child()), tree.get_root_val(), prepare_string_for_devirative_tree(tree.get_right_child())]
    elif tree.get_root_val() in special_function:
        return ['delete_element', tree.get_root_val(), prepare_string_for_devirative_tree(tree.get_right_child())]
    else:
        return tree.get_root_val()

def do_string(list_of_elements):
    text = ''
    index_number = 0
    while index_number < len(list_of_elements):
        if isinstance(list_of_elements[index_number], list):
            temp = list_of_elements[index_number]
            list_of_elements.insert(index_number + 1, ')')
            list_of_elements.insert(index_number+1, temp[2])
            list_of_elements.insert(index_number+1, temp[1])
            list_of_elements.insert(index_number+1, temp[0])
            list_of_elements.insert(index_number + 1, '(')
            list_of_elements.pop(index_number)
            index_number = 0
        else:
            index_number += 1
    while 'delete_element' in list_of_elements:
        list_of_elements.remove('delete_element')
    for i in list_of_elements:
        text += i
    return text

def main(text):
    return (do_string(prepare_string_for_devirative_tree(devirative_tree(build_parse_tree(text)))))


text2 = '(x+((2x)*(5sin(cos(exp(x))))))'
text3 = '((100x)+(exp(cos(sin(2x)))+x))'
text4 = '((cos(20.5x)+(3sin(x)))-((4exp(3x))/exp(x))'
text5 = 'exp(cos(x))+(x)'
text6 = '((2x)+(4x))'
if __name__ == "__main__":
    #print((build_parse_tree(text7)))
    print(main(text5))
