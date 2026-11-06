class node:
    def __init__(self, data):
        self.data =data
        self.next=None

node1=node(10)
node2=node(20)
node3=node(30)
node4=node(40)

node1.next=node2
node2.next=node3
node3.next=node4

head=node1

#insertion at the beginning
new_node=node(5)
new_node.next= head
head=new_node


# Insert at the end
new_node = node(50)

current = head

while current.next is not None:
    current = current.next

current.next = new_node

head=new_node
current=head

while current is not None:
    print(current.data)
    current=current.next






