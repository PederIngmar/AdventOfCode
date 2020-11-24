# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:30:43 2019

@author: peder1403
"""

data = open("18_day16_input.txt").read().strip("\n").split(",")
D = []
for l in data:
    L = []
    L.append(l[0])
    if len(l) > 3:
        l2 = l[1:].split("/")
        L.append(l2[0])
        L.append(l2[1])
    else:
        L.append(l[1:])

    D.append(L)

###############################

class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_list:
	def __init__(self):
		self.head=node()

	# Adds new node containing 'data' to the end of the linked list.
	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	# Returns the length (integer) of the linked list.
	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total

	# Prints out the linked list in traditional Python list format.
	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print(elems)

	# Returns the value of the node at 'index'.
	def get(self,index):
		if index>=self.length() or index<0: # added 'index<0' post-video
			print("ERROR: 'Get' Index out of range!")
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1

	# Deletes the node at index 'index'.
	def erase(self,index):
		if index >= self.length() or index<0: # added 'index<0' post-video
			print("ERROR: 'Erase' Index out of range!")
			return
		cur_idx=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_idx==index:
				last_node.next=cur_node.next
				return
			cur_idx+=1

	# Allows for bracket operator syntax (i.e. a[0] to return first item).
	def __getitem__(self,index):
		return self.get(index)


	#######################################################
	# Functions added after video tutorial

	# Inserts a new node at index 'index' containing data 'data'.
	# Indices begin at 0. If the provided index is greater than or
	# equal to the length of the linked list the 'data' will be appended.
	def insert(self,index,data):
		if index>=self.length() or index<0:
			return self.append(data)
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index:
				new_node=node(data)
				prior_node.next=new_node
				new_node.next=cur_node
				return
			prior_node=cur_node
			cur_idx+=1

	# Inserts the node 'node' at index 'index'. Indices begin at 0.
	# If the 'index' is greater than or equal to the length of the linked
	# list the 'node' will be appended.
	def insert_node(self,index,node):
		if index<0:
			print("ERROR: 'Erase' Index cannot be negative!")
			return
		if index>=self.length(): # append the node
			cur_node=self.head
			while cur_node.next!=None:
				cur_node=cur_node.next
			cur_node.next=node
			return
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index:
				prior_node.next=node
				return
			prior_node=cur_node
			cur_idx+=1


	def index(self, data):
		cur_node=self.head
		c = 0
		while cur_node.next!=None:
			if cur_node.data == data:
				print(data)
				return c
			cur_node=cur_node.next
			c += 1


	# Sets the data at index 'index' equal to 'data'.
	# Indices begin at 0. If the 'index' is greater than or equal
	# to the length of the linked list a warning will be printed
	# to the user.
	def set(self,index,data):
		if index>=self.length() or index<0:
			print("ERROR: 'Set' Index out of range!")
			return
		cur_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index:
				cur_node.data=data

			cur_idx+=1







########################################


P = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]

linkedP = linked_list()
for i in range(len(P)):
    linkedP.append(P[i])




#linkedP.display()

for i in range(1):
    #if i == 1:
        #print("part 1:", ''.join(P))

    for d in D:
        if d[0] == "s":
            for i in range(int(d[1])):
                linkedP.insert(0, linkedP.get(15))
                linkedP.erase(16)
            linkedP.display()
            print(d)
            #P = P[-int(d[1]):]+P[:-int(d[1])]
        if d[0] == "x":
            #print(d[1], d[2])
            #linkedP.display()
            a = linkedP.get(int(d[1]))
            b = linkedP.get(int(d[2]))
            linkedP.set(int(d[1]), a)
            linkedP.set(int(d[2]), b)
            linkedP.display()
            print(d, a,b)
            """
            a = linkedP.__getitem__(int(d[1]))
            b = linkedP.__getitem__(int(d[2]))
            linkedP.erase(int(d[1]))
            linkedP.erase(int(d[2]))
            linkedP.insert(int(d[2]),a)
            linkedP.insert(int(d[1]),b)
            """
            #linkedP.get(int(d[1])), linkedP.get(int(d[2])) = linkedP.get(int(d[2])), linkedP.get(int(d[1]))
            #P[int(d[1])], P[int(d[2])] = P[int(d[2])], P[int(d[1])]
        if d[0] == "p":
            a = linkedP.index(d[1])
            b = linkedP.index(d[2])
            #print(d[1],d[2],a,b)

            linkedP.set(a,d[2])
            linkedP.set(b,d[1])
            linkedP.display()
            print(d)



#print("part 2:", ''.join(P))
