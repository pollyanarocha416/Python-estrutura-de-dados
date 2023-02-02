#elas sao ierarquicas
#ela tem uma raiz e ramos vao crecendo
#nos: onde a info e armazenada
#arestas: e a conecsao dos nos da arvore
#Caminho: e um conjunto de nos conectados a-> b->c->
#no filho: q recebe -> b
#no pai: ele dar a ->
# subarvore: e td q esta em um lado de uma raiz
#no folha: nao tem filho
#nó raiz e 0, ...
# Altura o caminho maior


# toda arvore tem uma raiz
#so um pai
# arvore binaria a raiz so tem dois filhos 


# Metodos de uma arvore:

#class Arvore:
#    def binaryTree():#criar uma instancia da arvore
#    def get_left_child():# retorna a sobarvore a esquerda do no
#    def get_right_child():  # retorna a sobarvore a direita do no
#    def set_root_val(val):  # armazena um valor no no corrente
#    def get_root_val():  # retorna valor no no corrente
#    def insert_left(val):# cria uma nova arvore a esquerda do no
#    def insert_right(val):  # cria uma nova arvore a direita do no

my_tree = ['a',#raiz
            ['b',   #subarvore a esquerda
                ['d', [], []],# filho
                ['e', [], []]# filho
            ],
            ['c', #subaevore a direita
                ['f', [], []],#filho
                []
            ]
        ]
print(my_tree)
print('Subarvore esqu = ', my_tree[1])
print('Raiz = ', my_tree[0])
print('Subarvore direita = ', my_tree[2])







#Implementação da busca
class BSTNode(object):
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def get(self, key):
        if key < self.key:
            return self.left.get(key) if self.left else None
        elif key > self.key:
            return self.right.get(key) if self.right else None
        else:
            return self


tree = BSTNode(8)
...
found = tree.get(4)
if found:
    print(found)


#Árvore Binária de Busca
class BSTNodes(object):
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


root = BSTNodes(42)
root.left = BSTNodes(10)
root.right = BSTNodes(90)
root.left.left = BSTNodes(2)
