# Retorna el numero de valles dado el recorrido del caminante


def contar_valles(recorrido):
    if not set(recorrido).issubset({'D', 'U'}):
        raise ValueError("\nEntrada invalida Debe contener solo 'D' y 'U'.")

    valles = 0
    nivel = 0
    valle = False

    for paso in recorrido:
        if paso == 'D':
            nivel -= 1
        elif paso == 'U':
            nivel += 1

        if nivel < 0:
            valle = True
        elif nivel == 0 and valle:
            valles += 1
            valle = False

    return valles



# Arbol

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BST:
    
    def __init__(self):
        self.root = None
        
    def add(self,val):
        if(self.root is None):
            self.root = Node(val)
        else:
            self._aux_add(self.root,val)
            
    # Añade recurivamente
    def _aux_add(self, node, val):
        if val <= node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._aux_add(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._aux_add(node.right, val)
    
    
    # raiz -> left-> right            
    def preorden(self):
        return self._aux_preorden(self.root,[])
    def _aux_preorden(self,node, list):
        if node is not None:
            list.append(node.val)
            self._aux_preorden(node.left, list)
            self._aux_preorden(node.right, list)
        return list
    
    
    
    # left -> root -> right
    def inorden(self):
        return(self._aux_inorden(self.root,[]))
    def _aux_inorden(self, node, list):
        if node is not None:
            self._aux_inorden(node.left,list)
            list.append(node.val)
            self._aux_inorden(node.right,list)
        return list
        
        
    # left -> right ->  root
    def postorden(self):
        return self._aux_postorden(self.root,[])
    def _aux_postorden(self, node, list):
        if node is not None:
            self._aux_postorden(node.left, list)
            self._aux_postorden(node.right, list)
            list.append(node.val)
        return list
    
  
    

if __name__ == "__main__":
    
    
    print("\nIngrese los valores del arbon binario (separados por ','):")
    tree_data = list(map(int, input().split(',')))
    tree = BST()
    for valor in tree_data:
        tree.add(valor)
        
    
    
    print("Recorrido Preorden:", tree.preorden())
    print("Recorrido Inorden:", tree.inorden())
    print("Recorrido Postorden:", tree.postorden())
    
    
    
    # Valles
    
    # Ingresar recorrido
    print("\nIngrese el recorrido (U -> arriba, D -> abajo), debe pasarse sin espacios:")
    recorrido = input()

    # Ejemplo de contar valles en la recorrido ingresada
    print("Número de valles:", contar_valles(recorrido))
    




    
    
    