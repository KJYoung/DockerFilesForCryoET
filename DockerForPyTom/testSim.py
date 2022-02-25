from pytom.basic.files import pdb2em
from pytom.simulation.EMSimulation import simpleSimulation
from pytom_volume import vol, initSphere
from pytom.basic.structures import WedgeInfo

modeVol = False
modeSim = False
# PDB to MRC
# for i in [100, 150, 1000, 1900]: for first settings.

if modeVol:
    for i in [500]:
        pdbPath = "/cdata/pdbData/1bxn.pdb"
        pdbPixelSize = 2.7
        volumePath = "/cdata/volumes/1bxn_{}.mrc".format(i)
        volumepdb = pdb2em(pdbPath, pixelSize=pdbPixelSize, cubeSize=i, fname=volumePath)

if modeSim:
    # Simulation
    from pytom.basic.files import read
    ident = "130"
    volumePath = "/cdata/volumes/1bxn_{}.mrc".format(ident)
    simulatedPath = "/cdata/simulated/1bxn_{}.mrc".format(ident)

    v = read(volumePath)
    wedge = 0.
    shift = [-1, 2, 3]
    rotation = [0, 0, 0]
    # there is a slight inconsistency when smoothing > 0 -
    # cleaner implementation would be multipliction with sqrt(mask) in corr function
    wi = WedgeInfo(wedgeAngle=wedge, rotation=[10.0,20.0,30.0], cutoffRadius=0.0)
    s = simpleSimulation( volume=v, rotation=rotation, shiftV=shift, wedgeInfo=wi, SNR=10.)
    s.write(simulatedPath)