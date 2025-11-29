class Solution:
    def deleteNode(self, del_node):
        if del_node and del_node.next is None:
            return 
        del_node.data = del_node.next.data
        del_node.next=del_node.next.next