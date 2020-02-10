#Temporary control creation script.

import maya.cmds as cmds

def control(sels = []): #'circle' is the default value.
    if not sels:
        sels=cmds.ls(sl=True)
    
    n_ctrls = []
    
    for sel in sels:
        pos = cmds.xform(sel, q=True, ws=True, translation=True)
        orient = cmds.xform(sel, q=True, ws=True, rotation=True)
        size = cmds.xform(sel, q=True, ws=True, scale=True)
        
        ctrl = cmds.circle(c=[0,0,0], nr=[0,1,0], sw=360, r=2, d=3, ut=0, tol=0.01, s=8, ch=1)[0]
        
        cmds.xform(ctrl, ws=True, translation=pos)
        cmds.xform(ctrl, ws=True, rotation=orient)
        cmds.xform(ctrl, ws=True, scale=size)
        
        name = sel.rpartition('_') #rpartition moves right to left, instead of partition's left to right.
        name = name[0] + name[1] + 'Ctrl' 
        ctrl = cmds.rename(ctrl, name)
        n_ctrls.append(ctrl)
        
    group(n_ctrls)
    cmds.select(n_ctrls, r=True)

def group(sels=[]):
    if not sels:
        sels=cmds.ls(sl=True)
        
    n_sels = []
    
    for sel in sels:
        pos = cmds.xform(sel, q=True, ws=True, translation=True)
        orient = cmds.xform(sel, q=True, ws=True, rotation=True)
        scale = cmds.xform(sel, q=True, ws=True, scale=True)
        
        grp = cmds.group(empty=True, world=True)
        cmds.xform(grp, ws=True, translation=pos)
        cmds.xform(grp, ws=True, rotation=orient)
        cmds.xform(grp, ws=True, scale=scale)
        
        grp = cmds.rename(grp, sel + '_Grp')
        sel = cmds.parent(sel, grp)[0]
        n_sels.append(sel)
                
    cmds.select(n_sels, r=True)
    
def constrain(sels=[]):
    if not sels:
        sels = cmds.ls(sl=True)
        
    if len(sels) % 2 == 0: #is the length of the selection even?
        ctrls = sels[0 : len(sels)/2]
        jnts = sels[(len(sels)/2) : len(sels)]
        
        for i in range(len(ctrls)):
            cmds.parentConstraint(ctrls[i], jnts[i], mo=True, weight=1)
            
        cmds.select(ctrls, r=True)
        
    else:
        cmds.error("Must select an even number of objects.")
        
        
constrain()