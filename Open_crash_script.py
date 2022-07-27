def openscript():
    nuke.scriptClear()
    nuke.scriptOpen("")
    #nuke.message('hi')
    for i in nuke.allNodes():
        i.setSelected(True)
        nukescripts.toggle("disable")
        i.setSelected(False)



def toggle_all_nodes():
    for i in nuke.allNodes():
        i.setSelected(True)
        nukescripts.toggle("disable")
        i.setSelected(False)



nuke.menu('Nuke').addMenu('Tharun').addCommand('Openscript',openscript)
nuke.menu('Nuke').addMenu('Tharun').addCommand('Toggle all Nodes',toggle_all_nodes)





################################# version 2###############################

#print nuke.root()['Hero_plate'].value()

#label = nuke.selectedNode()['label'].value()
#print label


def heroplate():
    for i in nuke.allNodes('Read'):
        #print i['label'].value()
        #print 'label :',label
        if 'Hero Plate' in i['label'].value():
            return i['name'].value()
        else:
            #print 'No Hero_Plate'
            pass
heroplate()

heroplate = heroplate()
print heroplate
print nuke.toNode(heroplate).setSelected(True)


'''
# deselect all nodes 
for i in nuke.allNodes():
    i.setSelected(False)
nuke.toNode(heroplate).setSelected(True)
'''
