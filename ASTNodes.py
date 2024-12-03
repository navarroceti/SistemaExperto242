class ASTNode:
    pass

class PropNode(ASTNode):
    def __init__(self, value):
        self.value = value

class NegNode(ASTNode):
    def __init__(self, child):
        self.child = child

class CondNode(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right