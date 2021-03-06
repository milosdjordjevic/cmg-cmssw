import copy
import os
import CMGTools.RootTools.fwlite.Config as cfg
from CMGTools.RootTools.fwlite.Config import printComps
from CMGTools.WMass.triggerMap import triggers_mu

jsonAna = cfg.Analyzer(
        'JSONAnalyzer',
            )

triggerAna = cfg.Analyzer(
     'triggerBitFilter',
     # keepFailingEvents = False    
            )

vertexAna = cfg.Analyzer(
    'VertexAnalyzer',
    allVertices = 'slimmedPrimaryVertices',
    goodVertices = 'slimmedPrimaryVertices',
    vertexWeight = None,
    fixedWeight = 1,
    verbose = False,
            )

WAna = cfg.Analyzer(
        'WAnalyzer',
            recoilcut = 1000,
            pfmetcut = 0,
            jetptcut = 1000,
            pt = 30,
            eta = 2.1,
            iso = 0.5,
            savegenp = False,
            verbose = True,
            # triggerMap = pathsAndFilters
            triggerBits = {'SingleMu' : triggers_mu},
            )

WtreeProducer = cfg.Analyzer(
        'WTreeProducer'
            )

ZAna = cfg.Analyzer(
        'ZAnalyzer',
            recoilcut = 1000,
            pfmetcut = 0,
            jetptcut = 1000,
            pt = 30,
            eta = 2.1,
            iso = 0.5,
            savegenp = False,
            verbose = True,
            # triggerMap = pathsAndFilters
            triggerBits = {'SingleMu' : triggers_mu},
            )

ZtreeProducer = cfg.Analyzer(
        'ZTreeProducer'
            )
genAna = cfg.Analyzer(
        'GenParticleAnalyzerFSR',
            src = 'genParticlesPruned'
            )

sequence = cfg.Sequence( [
        genAna,
            jsonAna,
            triggerAna,
            vertexAna,
            WAna,
            WtreeProducer,
            ZAna,
            ZtreeProducer
           ] )

from CMGTools.H2TauTau.proto.samples.diboson import WW, ZZ, WZ
from CMGTools.H2TauTau.proto.samples.getFiles import getFiles

WW.files = getFiles('/WW_TuneZ2_7TeV_pythia6_tauola/Summer11LegDR-PU_S13_START53_LV6-v1/AODSIM/V5_B/PAT_CMG_V5_18_0', 'cmgtools', '.*root')
WW.triggers = triggers_mu
# WW.triggers = ["HLT_IsoMu24_v1","HLT_IsoMu24_v2","HLT_IsoMu24_v3","HLT_IsoMu24_v4","HLT_IsoMu24_v5","HLT_IsoMu24_v6","HLT_IsoMu24_v7",\
                                  # "HLT_IsoMu24_v8","HLT_IsoMu24_v9","HLT_IsoMu24_v10","HLT_IsoMu24_v11","HLT_IsoMu24_v12","HLT_IsoMu24_v13","HLT_IsoMu24_v14",\
                                  # "HLT_IsoMu24_eta2p1_v1","HLT_IsoMu24_eta2p1_v2","HLT_IsoMu24_eta2p1_v3","HLT_IsoMu24_eta2p1_v4","HLT_IsoMu24_eta2p1_v5",\
                                  # "HLT_IsoMu24_eta2p1_v6","HLT_IsoMu24_eta2p1_v7","HLT_IsoMu24_eta2p1_v8"
                                  # ]

WZ.files = getFiles('/WZ_TuneZ2_7TeV_pythia6_tauola/Summer11LegDR-PU_S13_START53_LV6-v1/AODSIM/V5_B/PAT_CMG_V5_18_0', 'cmgtools', '.*root')
WZ.triggers = triggers_mu
# WZ.triggers = ["HLT_IsoMu24_v1","HLT_IsoMu24_v2","HLT_IsoMu24_v3","HLT_IsoMu24_v4","HLT_IsoMu24_v5","HLT_IsoMu24_v6","HLT_IsoMu24_v7",\
                                  # "HLT_IsoMu24_v8","HLT_IsoMu24_v9","HLT_IsoMu24_v10","HLT_IsoMu24_v11","HLT_IsoMu24_v12","HLT_IsoMu24_v13","HLT_IsoMu24_v14",\
                                  # "HLT_IsoMu24_eta2p1_v1","HLT_IsoMu24_eta2p1_v2","HLT_IsoMu24_eta2p1_v3","HLT_IsoMu24_eta2p1_v4","HLT_IsoMu24_eta2p1_v5",\
                                  # "HLT_IsoMu24_eta2p1_v6","HLT_IsoMu24_eta2p1_v7","HLT_IsoMu24_eta2p1_v8"
                                  # ]

ZZ.files = getFiles('/ZZ_TuneZ2_7TeV_pythia6_tauola/Summer11LegDR-PU_S13_START53_LV6-v1/AODSIM/V5_B/PAT_CMG_V5_18_0', 'cmgtools', '.*root')
ZZ.triggers = triggers_mu
# ZZ.triggers = ["HLT_IsoMu24_v1","HLT_IsoMu24_v2","HLT_IsoMu24_v3","HLT_IsoMu24_v4","HLT_IsoMu24_v5","HLT_IsoMu24_v6","HLT_IsoMu24_v7",\
                                  # "HLT_IsoMu24_v8","HLT_IsoMu24_v9","HLT_IsoMu24_v10","HLT_IsoMu24_v11","HLT_IsoMu24_v12","HLT_IsoMu24_v13","HLT_IsoMu24_v14",\
                                  # "HLT_IsoMu24_eta2p1_v1","HLT_IsoMu24_eta2p1_v2","HLT_IsoMu24_eta2p1_v3","HLT_IsoMu24_eta2p1_v4","HLT_IsoMu24_eta2p1_v5",\
                                  # "HLT_IsoMu24_eta2p1_v6","HLT_IsoMu24_eta2p1_v7","HLT_IsoMu24_eta2p1_v8"
                                  # ]

selectedComponents = [ZZ,WZ,WW]

ZZ.splitFactor = 750
WZ.splitFactor = 750
WW.splitFactor = 750

config = cfg.Config( components = selectedComponents,
                     sequence = sequence )

printComps(config.components, True)
