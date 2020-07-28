# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:01:04 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
w=15
h=15
l=15
x,y,z=mc.player.getTilePos()
mc.setBlocks(x,y,z,x+w,y+h,z+l,46)
mc.setBlocks(x+1,y+1,z+1,x+w-1,y+h-1,z+l-1,0)