
sample_type_dict = {
    'BILE': 'BIL',
    'BLANK BLOOD': 'BLKB',
    'BLANK SERUM': 'BLKS',
    'BLANK URINE': 'BLKU',
    'BLOOD - ABDOMINAL': 'ABDB',
    'BLOOD - ANTEMORTEM': 'AMB',
    'BLOOD - AORTA': 'AOB',
    'BLOOD - CHEST': 'CB',
    'BLOOD - CLOT': 'CLOTB',
    'BLOOD - FEMORAL VEIN': 'FVB',
    'BLOOD - HEART': 'HB',
    'BLOOD - ILIAC VEIN': 'IVB',
    'BLOOD - IVC': 'IVCB',
    'BLOOD - JUGULAR': 'JUGB',
    'BLOOD - LEFT CHEST': 'LCB',
    'BLOOD - MIXED': 'MB',
    'BLOOD - PERICARDIAL': 'PCB',
    'BLOOD - RIGHT CHEST': 'RCB',
    'BLOOD - SAPHENOUS VEIN': 'SVB',
    'BLOOD - SUBDURAL': 'SUBDB',
    'BLOOD - SVC': 'SVCB',
    'BRAIN HOMOGENATE': 'BRNHOM',
    'CHEST FLUID - LEFT CHEST': 'LCF',
    'CHEST FLUID - RIGHT CHEST': 'RCF',
    'DECOMP FLUID': 'DF',
    'DRUGS/PARAPHERNALIA': 'DRUG',
    'GASTRIC': 'G',
    'HAIR': 'HAIR',
    'HEART': 'HT',
    'KIDNEY': 'KID',
    'LARGE INTESTINAL CONTENT': 'LGIC',
    'LIVER HOMOGENATE': 'LIVHOM',
    'LUNG': 'LUNG',
    'MEDICATIONS': 'MEDS',
    'MUSCLE': 'MUSC',
    'OCULAR FLUID': 'OF',
    'PACEMAKER': 'PM',
    'SERUM - ANTEMORTEM': 'AMS',
    'SKELETAL MUSCLE': 'SKMUSC',
    'SMALL INTESTINAL CONTENT': 'SMIC',
    'SPECIMEN - ANTEMORTEM': 'AM',
    'SPECIMEN - OTHER': 'OTHER',
    'SPINAL CORD': 'SC',
    'SPLEEN': 'SPL',
    'URINE - ANTEMORTEM': 'AMU',
    'BLOOD - PERIPHERAL': 'PERIPHB',
    'BLOOD LEFT BUTTOCK': 'LBUTTB',
    'BLOOD - PERICARDIAL SAC': 'PCSB',
    'SUBCLAVIAN BLOOD': 'SCB',
    'BLOOD': 'B',
    'CHEST FLUID': 'CF',
    'URINE': 'U',
    'SERUM': 'S',
    'LIVER': 'LIV',
    'BRAIN': 'BRN',
    'INTESTINAL CONTENT - SM': 'SMIC',
    'RIGHT PLEURAL CAVITY': 'RPC',
    'PLACENTA': 'PLAC',
    'AMNIOTIC FLUID': 'AMFLU',
    'PERI': 'PCS',
    'BLOOD - CENTRAL': 'CB',
    'INTRAPARENCHYMAL BLOOD': 'PCB',
    'CHEST FLUID - LEFT CHEST & RIGHT CHEST': 'LCRC',
    'STOMACH MATERIAL ': 'STM',
    'DONOR-SAPHENOUS VEIN': 'DSV',
    'MUSCLE HOMOGENATE': 'MUSHOM',
    'SMALL BOWEL': 'SMIC',
    'DONOR-SAPHENOUS BLOOD': 'DSB',
    'PELVIC BLOOD': 'PB',
    'PERICARDIAL FLUID': 'PCF',
    'ILIAC ARTERY': 'IAB',
    'FLUID FROM PERICARDIAL SAC': 'FPS',
    'FEMORAL CLOTS': 'FC',
    'BLOOD SUBCLAVIAN': 'SCB',
    'SOFT TISSUE': 'ST',
    'BRAIN CLOT': 'BRCLT',
    'BLOOD - ABDOMEN': 'BABD',
    'BRAIN HEMORRHAGE': 'BRHEM',
    'SMALL INTESTINE': 'SMI',
    'DONOR BLOOD - FEMORAL VEIN': 'FV'
}

sample_container_dict = {
    '50ML BLUE TOP': 'BBT',
    '50ML PURPLE TOP': 'BPRPT',
    '50ML RED TOP': 'BRT',
    '500ML CONTAINER': 'LCNTR',
    'AMBER VIAL': 'AMBVIAL',
    'BLUE TOP TUBE': 'BT',
    'CLEAR TOP TUBE': 'CT',
    'CLEAR VIAL': 'CLRVIAL',
    'CONTAINER - OTHER': 'OTHER',
    'EVIDENCE BAG': 'EVBAG',
    'FRESH SPECIMEN CUP': 'CUP',
    'GOLD TOP SST': 'GLDSST',
    'GOLD TOP TUBE': 'GLDT',
    'GREEN TOP TUBE': 'GRNT',
    'GREEN/PURPLE TOP SST': 'GPSST',
    'GREY TOP TUBE': 'GT',
    'LARGE PLASTIC BOTTLE': 'LGBOT',
    'PINK TOP TUBE': 'PKT',
    'SMALL PLASTIC BOTTLE': 'SMBOT',
    'PURPLE TOP TUBE': 'PRPT',
    'RED TOP SST': 'RSST',
    'RED TOP TUBE': 'RT',
    'RED/BLACK TOP SST': 'RBSST',
    'SWAB': 'SWAB',
    'WHITE TOP TUBE': 'WT',
    'YELLOW TOP SST': 'YSST',
    'YELLOW TOP TUBE': 'YT',
    '30 ML GREEN TOP': 'BGT',
    '50 ML GREEN TOP': 'XLGT',
    'BLACK TOP TUBE': 'BTT',
    'BABY BOTTLE': 'BBTL',
    'CLEAR TOP TUBE SST': 'CSST',
    '50ML GREEN TOP': 'BGT',
    '60 ML NALGENE BOTTLE': 'BOT',
    '60ML NALGENE BOTTLE': 'BOT',
    '125 ML NALGENE BOTTL': 'BOT'    
}

caboose = {
    'PLACENTA': 1,
    'BILE': 1, 
    'AMNIOTIC FLUID': 2,
    'BRAIN': 3,
    'LIVER': 4,
    'MUSCLE': 5,
    'SKELETAL MUSCLE': 6,
    'SPLEEN': 7,
    'KIDNEY': 8,
    'LUNG': 9,
    'URINE': 10,
    'GASTRIC': 11,
    'SMALL INTESTINE': 12,
    'SMALL INTESTINAL CONTENT': 13,
    'SMALL BOWEL': 14,
    'LARGE INTESTINAL CONTENT': 15,
    'SPECIMEN - OTHER': 16,
    'INTESTINAL CONTENT - SM': 17,
    'STOMACH MATERIAL': 18,
    'MUSCLE HOMOGENATE': 19,
    'BRAIN HOMOGENATE': 20,
    'LIVER HOMOGENATE': 21,
}

vol_duplicate = [
    'OCULAR FLUID',
    'OCULAR',
    'PLACENTA',
    'BILE',
    'AMNIOTIC FLUID',
    'BRAIN',
    'LIVER',
    'MUSCLE',
    'SKELETAL MUSCLE',
    'SPLEEN',
    'KIDNEY',
    'LUNG',
    'URINE',
    'GASTRIC',
    'SMALL INTESTINE',
    'SMALL INTESTINAL CONTENT',
    'SMALL BOWEL',
    'LARGE INTESTINAL CONTENT',
    'SPECIMEN - OTHER',
    'INTESTINAL CONTENT - SM',
    'STOMACH MATERIAL',
    'MUSCLE HOMOGENATE',
    'BRAIN HOMOGENATE',
    'LIVER HOMOGENATE',
]

method_dict = {
    'QTABUSE':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTACET':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTANTIDEP':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTANTIHI':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTBZO1':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTBZO2':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTCCB':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTDASH':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTMEPER':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTMETHA':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTOLANZ':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTPSYCH':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTSALIC':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTSERT':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTSTIM':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'QTTRAZODON':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],
    'SCNITAZ':['LF-23.9 Shimadzu 8060 LC-MSMS #1', 'LF-23.10 Shimadzu 8060 LC-MSMS #2'],

    'QTTRAM':['LF-23.7 Bruker SCION GC-MSMS #1', 'LF-23.8 Bruker SCION GC-MSMS #2'],
    'QTOPI':['LF-23.7 Bruker SCION GC-MSMS #1', 'LF-23.8 Bruker SCION GC-MSMS #2'],
    'QTZOLP':['LF-23.7 Bruker SCION GC-MSMS #1', 'LF-23.8 Bruker SCION GC-MSMS #2'],
    'COTHC':['LF-23.7 Bruker SCION GC-MSMS #1', 'LF-23.8 Bruker SCION GC-MSMS #2'],

    'SCGEN':['LF-23.6 Bruker ToxTyper LC-Ion Trap-MSn',],
    'COSTIM':['LF-23.6 Bruker ToxTyper LC-Ion Trap-MSn',],
    'SCSYNCAN':['LF-23.6 Bruker ToxTyper LC-Ion Trap-MSn',],

    'SCLCMSMS':['LF-23.5 Shimadzu 8060NX LC-MSMS',],

    'SQVOL':['LF-23.1 Shimadzu Nexis GC-2030 #1', 'LF-23.2 Shimadzu Nexis GC-2030 #2'],

    'SCRNZ':['LF-23.3 Agilent ToxAnalyzer GC-NPD-MS #1', 'LF-23.4 Agilent ToxAnalyzer GC-NPD-MS #2'],
}