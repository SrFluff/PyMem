'''

The slot system

You get an X amount of slots,
each slot can be reserved and set to a value
then you can deallocate it using
dealloc, theoretically, you could use like
2 slots and just keep switching their values
:3

'''

slots = [0 , 0 , 0 , 0 , 0]

#Slots holds the acutal values of the slots

sat = ['e' , 'e' , 'e' , 'e' , 'e']

#The sat(Slot Allocation Table) keeps track of whether a slot is empty or occupied

import os

def cls():

    os.system('clear')

def alloc(slot_space, cont):

    global sat
    global slots

    if len(slots) >=  slot_space:

        if sat[slot_space] == 'e':

            slots[slot_space] = cont
            sat[slot_space] = 'o'

        else:

            print('Error - Slot not empty')

    else:

        print('Error - Index out of range')

def dealloc(slot_index):

    global slots
    global sat

    if len(slots) >= slot_index:

        if sat[slot_index] == 'o':

            sat[slot_index] = 'e'
            slots[slot_index] = 0

        else:

            print('Error - Slot is already empty')

    else:

        print('Error - Index out of range')

alloc(0, True)
alloc(1, True)
alloc(2, 'answers')

'''

Slot breakdown:

slot[0] = Main process
slot[1] = OS process
slot[2] = input()

'''

while slots[0]:

    cls()
    slots[2] = input("> ")
    cls()
    slots[0] = False
    dealloc(0)

dealloc(1)
dealloc(2)
