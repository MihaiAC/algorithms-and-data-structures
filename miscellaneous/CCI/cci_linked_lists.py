class Node:
    def __init__(self,value,next_node=None):
        self.value = value
        self.next_node = next_node
    
    def build_linked_list(array):
        head = Node(array[0])
        tail = head
        for elem in array[1:]:
            node = Node(elem)
            tail.next_node = node
            tail = node
        return head
    
    def to_list(self):
        head = self.next_node
        lst = list()
        lst.append(self.value)
        while(head != None):
            lst.append(head.value)
            head = head.next_node
        return lst

def remove_dups(head):
    hash_map = dict()
    node = head
    
    while(node !=  None):
        hash_map[node.value] = 1
        node = node.next_node
    
    node = head
    while(node.next_node is not None):
        if(hash_map[node.next_node.value] == 0):
            node.next_node = node.next_node.next_node
        else:
            hash_map[node.value] = 0
            node = node.next_node
    
    return head

def kth_to_last(head,k):
    pointer_1 = head
    if(head == None):
        print("The linked list is empty!")
        return -1 #assuming only non-negative values in the list
    
    pointer_2 = head
    for _ in range(0,k-1):
        pointer_2 = pointer_2.next_node
        if(pointer_2 == None):
            print("The linked list is not long enough.")
            return -1

    while(pointer_2.next_node != None):
        pointer_1 = pointer_1.next_node
        pointer_2 = pointer_2.next_node
    
    return pointer_1.value


head = Node.build_linked_list(list([4,5,6,7,8,5,5]))
print(kth_to_last(head,4))