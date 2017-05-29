def readButton():
        print ('Choose state of emergence: ')
        print ('0 --- If not in Emergence \n 1 --- If in Emergence')
        if raw_input()== '0':
            state= False
        else:
            state= True
        return state