# # TODO: Refactor this into a dictionary made from a csv file that Pat maintains.
# def workstation_to_agency(workstation_value):
#     """Pat's original design for calculating Agency field value"""
#     if "sha" in workstation_value:
#         return 'SHA'
#     elif "ad-geo" in workstation_value:
#         return 'DHMH'
#     elif "anlt" in workstation_value:
#         return 'DOIT'
#     elif "bha" in workstation_value:
#         return 'DHMH'
#     elif "boa" in workstation_value:
#         return 'DNR'
#     elif "cac" in workstation_value:
#         return 'DNR'
#     elif "carrhd" in workstation_value:
#         return 'DHMH'
#     elif "cgla" in workstation_value:
#         return 'DNR'
#     elif "chart" in workstation_value:
#         return 'CHART'
#     elif "doit" in workstation_value:
#         return 'DOIT'
#     elif "dt-nbar" in workstation_value:
#         return 'MEMA'
#     elif "dtseoc" in workstation_value:
#         return 'MEMA'
#     elif "f1" in workstation_value:
#         return 'MDTA'
#     elif "fis" in workstation_value:
#         return 'DNR'
#     elif "for" in workstation_value:
#         return 'DNR'
#     elif "hchd" in workstation_value:
#         return 'DHMH'
#     elif "ideha" in workstation_value:
#         return 'DHMH'
#     elif "ipr" in workstation_value:
#         return 'DNR'
#     elif "it" in workstation_value:
#         return 'DOIT'
#     elif "It-" in workstation_value:
#         return 'DOIT'
#     elif "its" in workstation_value:
#         return 'DNR'
#     elif "lap" in workstation_value:
#         return 'DNR'
#     elif "mcac" in workstation_value:
#         return 'MCAC'
#     elif "mda" in workstation_value:
#         return 'MDA'
#     elif "mdp" in workstation_value:
#         return 'MDP'
#     elif "met" in workstation_value:
#         return 'MET'
#     elif "mgs" in workstation_value:
#         return 'DNR'
#     elif "mht" in workstation_value:
#         return 'MDP'
#     elif "mmccon" in workstation_value:
#         return 'MLIS'
#     elif "mta" in workstation_value:
#         return 'MTA'
#     elif "ofkaw" in workstation_value:
#         return 'DBED'
#     elif "ox" in workstation_value:
#         return 'DNR'
#     elif "pc-" in workstation_value:
#         return 'MDE'
#     elif "phpa" in workstation_value:
#         return 'DHMH'
#     elif "prk" in workstation_value:
#         return 'DNR'
#     elif "ras" in workstation_value:
#         return 'DNR'
#     elif "scdd" in workstation_value:
#         return 'MDA'
#     elif "schd" in workstation_value:
#         return 'DHMH'
#     elif "t22" in workstation_value:
#         return 'MTA'
#     elif "t23" in workstation_value:
#         return 'MTA'
#     elif "t21" in workstation_value:
#         return 'MTA'
#     elif "whs" in workstation_value:
#         return 'DNR'
#     elif "brel" in workstation_value:
#         return 'COMP'
#     elif "w-7" in workstation_value:
#         return 'DHCD'
#     elif "cechd" in workstation_value:
#         return 'DHMH'
#     elif "dda-83905" in workstation_value:
#         return 'DHMH'
#     elif "fha-" in workstation_value:
#         return 'DHMH'
#     elif "hsia-" in workstation_value:
#         return 'DHMH'
#     elif "mhcc-" in workstation_value:
#         return 'DHMH'
#     elif "sandy-b" in workstation_value:
#         return 'DHMH'
#     elif "wic-000" in workstation_value:
#         return 'DHMH'
#     elif "wochd-" in workstation_value:
#         return 'DHMH'
#     elif "geoserv" in workstation_value:
#         return 'DHMH'
#     elif "vsa-" in workstation_value:
#         return 'DHMH'
#     elif "000_02_146299" in workstation_value:
#         return 'DHR'
#     elif "fa62512" in workstation_value:
#         return 'DJS'
#     elif "dwd27088" in workstation_value:
#         return 'DLLR'
#     elif "lmai" in workstation_value:
#         return 'DLLR'
#     elif "oos009" in workstation_value:
#         return 'DNR'
#     elif "minint-" in workstation_value:
#         return 'MDA'
#     elif "mdewin" in workstation_value:
#         return 'MDE'
#     elif "tr-1024352" in workstation_value:
#         return 'MDE'
#     elif "tr-1024362" in workstation_value:
#         return 'MDE'
#     elif "tr-1024368" in workstation_value:
#         return 'MDE'
#     elif "tr-1024371" in workstation_value:
#         return 'MDE'
#     elif "tr-1024385" in workstation_value:
#         return 'MDE'
#     elif "tr-1024386" in workstation_value:
#         return 'MDE'
#     elif "tr-1024388" in workstation_value:
#         return 'MDE'
#     elif "tr-1024393" in workstation_value:
#         return 'MDE'
#     elif "q13" in workstation_value:
#         return 'MDOT'
#     elif "va52450" in workstation_value:
#         return 'MDP'
#     elif "mdtagis" in workstation_value:
#         return 'MDTA'
#     elif "lt-thutchison" in workstation_value:
#         return 'MEMA'
#     elif "meshp" in workstation_value:
#         return 'MPA'
#     elif "mpa-hp" in workstation_value:
#         return 'MPA'
#     elif "s530" in workstation_value:
#         return 'MPA'
#     elif "s535" in workstation_value:
#         return 'MPA'
#     elif "s536" in workstation_value:
#         return 'MPA'
#     elif "s538" in workstation_value:
#         return 'MPA'
#     elif "s541" in workstation_value:
#         return 'MPA'
#     elif "s542" in workstation_value:
#         return 'MPA'
#     elif "msp000" in workstation_value:
#         return 'MSP'
#     elif "s530" in workstation_value:
#         return 'MPA'
#     elif "sandy-b" in workstation_value:
#         return 'DHMH'
#     elif "sgatesdlsl1" in workstation_value:
#         return 'MLIS'
#     elif "skennedydlsl1" in workstation_value:
#         return 'MLIS'
#     elif "smccullochdlsl1" in workstation_value:
#         return 'MLIS'
#     elif "srossdlsl1" in workstation_value:
#         return 'MLIS'
#     elif "ssd-800g1-01" in workstation_value:
#         return 'MDP'
#     elif "tclarkdlsl1" in workstation_value:
#         return 'MLIS'
#     elif "tl222845" in workstation_value:
#         return 'MTA'
#     elif "tl231013" in workstation_value:
#         return 'MTA'
#     elif "tr-1024" in workstation_value:
#         return 'Training'
#     elif "training" in workstation_value:
#         return 'Training'
#     elif "tzimmermandlsl1" in workstation_value:
#         return 'MLIS'
#     elif "va47" in workstation_value:
#         return 'MVA'
#     elif "va511" in workstation_value:
#         return 'MVA'
#     elif "va54" in workstation_value:
#         return 'MVA'
#     elif "va625" in workstation_value:
#         return 'MVA'
#     elif "va52450" in workstation_value:
#         return 'MDOT'
#     elif "vsa-" in workstation_value:
#         return 'DHMH'
#     elif "wic-00076933" in workstation_value:
#         return 'DHMH'
#     elif "wochd-7397" in workstation_value:
#         return 'DHMH'
#     elif "yweissmannmgal1" in workstation_value:
#         return 'MLIS'
#     elif "wsu00" in workstation_value:
#         return 'DNR'
#     else:
#         return 'Research'
