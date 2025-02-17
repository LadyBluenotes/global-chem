#!/usr/bin/env python3
#
# GlobalChem - Rings in Drugs
#
# -----------------------------------

class RingsInDrugs(object):

    def __init__(self):

        self.name = 'rings_in_drugs'

    @staticmethod
    def get_smiles():

        smiles = {
            "benzene": "C1=CC=CC=C1",
            "pyridine": "C1=CC=CN=C1",
            "piperidine": "N1CCCCC1",
            "piperazine": "N1CCNCC1",
            "cyclohexane": "C1CCCCC1",
            "oxane": "O1CCCCC1",
            "imidazole": "C1=NC=CN1",
            "pyrrolidine": "C1CCNC1",
            "(R)-5-thia-1-azabicyclo[4.2.0]oct-2-en-8-one": "O=C1C[C@@H]2N1C=CCS2",
            "cyclopropane": "C1CC1",
            "tetrahydrofuran" : "C1CCOC1",
            "thiazole": "C1=NC=CS1",
            "indole": "C12=CC=CC=C1C=CN2",
            "diazine": "C1=NC=CC=N1",
            "(R)-4-thia-1-azabicyclo[3.2.0]heptan-7-one": "O=C1N2CCS[C@@H]2C1",
            "6,7,8,9,10,11,12,13,14,15,16,17-dodecahydro-3H-cyclopenta[a]phenanthren-3-one": "O=C1C=CC(C2C[C@H](CCC3)C3CC2)C(CCC)=C1",
            "tetrazole": "N1=NN=C[N]1",
            "cyclopentane": "C1CCCC1",
            "thiophenyl" : "C1=CC=CS1",
            "naphthalene": "C12=CC=CC=C1C=CC=C2",
            "1H-benzo[d]imidazole" : "C12=CC=CC=C1N=CN2",
            "quinoline": "C12=CC=CC=C1C=CC=N2",
            "1H-purine": "C12=CNC=NC1=NC=N2",
            "1,2,6,7,8,9,10,11,12,13,14,15,16,17-tetradecahydro-3H-cyclopenta[a]phenanthren-3-one": "O=C1CCC([C@@H]2C[C@H](CCC3)C3CC2)C(CCC)=C1",
            "furan" : "C1=CC=CO1",
            "1H-1,2,4-Triazole": "N1=CN=CN1",
            "10H-Phenothiazine" : "C12=CC=CC=C1NC3=C(C=CC=C3)S2",
            "quinazoline" : "C12=CC=CC=C1C=NC=N2",
            "morpholine": "C1CNCCO1",
            "pyrimidin-2(1H)-one" : "O=C1N=CC=CN1",
            "quinolin-4(1H)-one": "O=C1C2=C(C=CC=C2)NC=C1",
            "(9S,14R)-6,7,8,9,10,11,12,13,14,15,16,17-dodecahydro-3H-cyclopenta[a]phenanthren-3-one": "O=C1C=CC([C@H]2CCC3[C@@H](CCC3)C2)C(CCC)=C1",
            "isoxazole": "C1=CC=NO1",
            "imidazoline": "C1=NCCN1",
            "1,4-dihydropyridine": "C1=CCC=CN1",
            "pyrimidine-2,4(1H,3H)-dione": "O=C(N1)NC=CC1=O",
            "3,4-dihydro-2H-benzo[e][1,4]diazepin-2-one": "O=C1N=C2C=CC=CC2=CNC1",
            "cyclohexene": "C1=CCCCC1",
            "pyrrolidin-2-one": "O=C1NCCC1",
            "imidazolidine-2,4-dione": "O=C(CN1)NC1=O",
            "1,2,3,4-tetrahydroisoquinoline": "C1(C=CC=C2)=C2CCNC1",
            "3,4-dihydro-2H-benzo[e][1,2,4]thiadiazine 1,1-dioxide": "O=S1(NCNC2=C1C=CC=C2)=O",
            "7,8,9,11,12,13,14,15,16,17-decahydro-6H-cyclopenta[a]phenanthrene": "CCCC1=CC=CC=C1[C@@H]2C[C@H](CCC3)C3CC2",
            "1H-pyrazole": "N1=CC=CN1",
            "quinuclidine": "C1(CC2)CCN2CC1",
            "epoxide": "C1CO1",
            "pyrazine": "C1=CN=CC=N1",
            "oxazolidinone": "O=C1OCCN1",
            "tetrahydronaphthalene":"C1(C=CC=C2)=C2CCCC1",
            "adamantane": "C1(CC(C2)C3)CC2CC3C1",
            "1,8-naphthyridin-4(1H)-one":"O=C(C=CN1)C2=C1N=CC=C2",
            "3,7-dihydro-1H-purine-2,6-dione": "O=C(C(NC=N1)=C1N2)NC2=O",
            "hexadecahydro-1H-cyclopenta[a]phenanthrene": "CCC[C@H]1CCCCC1[C@@H]2C[C@H](CCC3)C3CC2",
            "7,8,9,10-tetrahydrotetracene-5,12-dione": "O=C(C(C=C(CCCC1)C1=C2)=C2C3=O)C4=C3C=CC=C4",
            "cyclobutane": "C1CCC1",
            "1,2-dihydro-3H-1,2,4-triazol-3-one": "O=C1NNC=N1",
            "1,3,4-thiadiazole": "C1=NN=CS1",
            "azepane": "C1NCCCCC1",
            "8-azabicyclo[3.2.1]octane": "C12CCCC(CC2)N1",
            "piperidine-2,6-dione":"O=C(N1)CCCC1=O",
            "2,3-dihydro-1H-indene":"O=C(N1)CCCC1=O",
            "benzo[d]isoxazole":"C12=CC=CC=C1C=NO2",
            "1,9-dihydro-6H-purin-6-one":"O=C1C2=C(NC=N2)N=CN1",
            "9H-fluorene":"C12=CC=CC=C1C3=C(C=CC=C3)C2",
            "10,11-dihydro-5H-dibenzo[b,f]azepine":"C12=CC=CC=C1CCC3=C(C=CC=C3)N2",
            "(6aR,10aR)-4,6,6a,7,8,9,10,10a-octahydroindolo[4,3-fg]quinoline":"C12=CC=CC3=C1C(C[C@@H]4[C@@H]2CCCN4)=CN3",
            "1H-pyrrole": "C1=CC=CN1",
            "1,3-dioxolane":"O1CCOC1",
            "(1R,5S)-3-azabicyclo[3.1.0]hexane": "[C@@H]1(C2)[C@H]2CNC1",
            "cyclopentanone": "O=C1CCCC1",
            "pyrrolidine-2,5-dione":"O=C(N1)CCC1=O",
            "pyrazolidine":"O=C(NN1)CC1=O",
            "(R)-1-azabicyclo[3.2.0]hept-2-en-7-one":"O=C1N2C=CC[C@@H]2C1",
            "thiazolidine-2,4-dione":"O=C(CS1)NC1=O",
            "benzofuran":"C12=CC=CC=C1C=CO2",
            "1H-indazole":"C12=CC=CC=C1C=NN2",
            "indolin-2-one":"O=C1NC2=CC=CC=C2C1",
            "benzo[b]thiophene":"C12=CC=CC=C1C=CS2",
            "(R)-1,2,3,7,8,8a-hexahydronaphthalene":"C12=CCCC[C@@H]1CCC=C2",
            "4,5,6,7-tetrahydrothieno[3,2-c]pyridine":"C1(C=CS2)=C2CCNC1",
            "4H-chromen-4-one":"O=C(C=CO1)C2=C1C=CC=C2",
            "3,4-dihydroquino-2(1H)-one":"O=C(CC1)NC2=C1C=CC=C2",
            "napthalene-1,4-dione": "O=C(C=CC1=O)C2=C1C=CC=C2",
            "2H-benzo[e][1,2,4]thiadiazine 1,1-dioxide":"O=S(C1=C2C=CC=C1)(NC=N2)=O",
            "4H-benzo[f][1,2,4]triazolo[4,3-a][1,4]diazepine":"C1(N2C(CN=C3)=NN=C2)=C3C=CC=C1",
            "9H-thioxanthene":"C12=CC=CC=C1CC3=C(C=CC=C3)S2",
            "(5aR,8aR)-5,8,8a,9-tetrahydrofuro[3',4':6,7]naphtho[2,3-d][1,3]dioxol-6(5aH)-one":"O=C(OC1)[C@H]2[C@H]1CC3=CC4=C(C=C3C2)OCO4",
            "(3a1S,5aS,10bS)-3a,3a1,4,5,5a,6,11,12-octahydro-1H-indolizino[8,1-cd]carbazole":"C12=CC=CC=C1[C@@]34[C@H](CCC5[C@@H]3N(CC=C5)CC4)N2",
            "(4aR,5aR)-4a,5a,6,12a-tetrahydrotetracene-1,11(4H,5H)-dione":"O=C1C2=CC3[C@H](CC=CC3=O)C[C@@H]2CC4=CC=CC=C41",
            "1H-1,2,3-triazole": "N1=NC=CN1",
            "azetidin-2-one":"O=C1NCC1",
            "oxetan-2-one":"O=C1OCC1"
        }

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {
            'benzene':'[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'pyridine':'[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'piperidine':'[#7]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'piperazine':'[#7]1-[#6]-[#6]-[#7]-[#6]-[#6]-1',
            'cyclohexane':'[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'oxane':'[#8]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'imidazole':'[#6]1:[#7]:[#6]:[#6]:[#7H]:1',
            'pyrrolidine':'[#6]1-[#6]-[#6]-[#7]-[#6]-1',
            '(R)-5-thia-1-azabicyclo[4.2.0]oct-2-en-8-one':'[#8]=[#6]1-[#6]-[#6@@H]2-[#7]-1-[#6]=[#6]-[#6]-[#16]-2',
            'cyclopropane':'[#6]1-[#6]-[#6]-1',
            'tetrahydrofuran':'[#6]1-[#6]-[#6]-[#8]-[#6]-1',
            'thiazole':'[#6]1:[#7]:[#6]:[#6]:[#16]:1',
            'indole':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#7H]:2',
            'diazine':'[#6]1:[#7]:[#6]:[#6]:[#6]:[#7]:1',
            '(R)-4-thia-1-azabicyclo[3.2.0]heptan-7-one':'[#8]=[#6]1-[#7]2-[#6]-[#6]-[#16]-[#6@@H]-2-[#6]-1',
            '6,7,8,9,10,11,12,13,14,15,16,17-dodecahydro-3H-cyclopenta[a]phenanthren-3-one':'[#8]=[#6]1-[#6]=[#6]-[#6](-[#6]2-[#6]-[#6@@H]3-[#6]-[#6]-[#6]-[#6]-3-[#6]-[#6]-2)-[#6](-[#6]-[#6]-[#6])=[#6]-1',
            'tetrazole':'[#7]1=[#7]-[#7]=[#6]-[#7]-1',
            'cyclopentane':'[#6]1-[#6]-[#6]-[#6]-[#6]-1',
            'thiophenyl':'[#6]1:[#6]:[#6]:[#6]:[#16]:1',
            'naphthalene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            '1H-benzo[d]imidazole':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#7]:[#6]:[#7H]:2',
            'quinoline':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#7]:2',
            '1H-purine':'[#6]12:[#6]:[#7H]:[#6]:[#7]:[#6]-1:[#7]:[#6]:[#7]:2',
            '1,2,6,7,8,9,10,11,12,13,14,15,16,17-tetradecahydro-3H-cyclopenta[a]phenanthren-3-one':'[#8]=[#6]1-[#6]-[#6]-[#6](-[#6@@H]2-[#6]-[#6@@H]3-[#6]-[#6]-[#6]-[#6]-3-[#6]-[#6]-2)-[#6](-[#6]-[#6]-[#6])=[#6]-1',
            'furan':'[#6]1:[#6]:[#6]:[#6]:[#8]:1',
            '1H-1,2,4-Triazole':'[#7]1:[#6]:[#7]:[#6]:[#7H]:1',
            '10H-Phenothiazine':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#7]-[#6]1:[#6](:[#6]:[#6]:[#6]:[#6]:1)-[#16]-2',
            'quinazoline':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#7]:[#6]:[#7]:2',
            'morpholine':'[#6]1-[#6]-[#7]-[#6]-[#6]-[#8]-1',
            'pyrimidin-2(1H)-one':'[#8]=[#6]1:[#7]:[#6]:[#6]:[#6]:[#7H]:1',
            'quinolin-4(1H)-one':'[#8]=[#6]1:[#6]2:[#6](:[#6]:[#6]:[#6]:[#6]:2):[#7H]:[#6]:[#6]:1',
            '(9S,14R)-6,7,8,9,10,11,12,13,14,15,16,17-dodecahydro-3H-cyclopenta[a]phenanthren-3-one':'[#8]=[#6]1-[#6]=[#6]-[#6](-[#6@H]2-[#6]-[#6]-[#6]3-[#6@@H](-[#6]-[#6]-[#6]-3)-[#6]-2)-[#6](-[#6]-[#6]-[#6])=[#6]-1',
            'isoxazole':'[#6]1:[#6]:[#6]:[#7]:[#8]:1',
            'imidazoline':'[#6]1=[#7]-[#6]-[#6]-[#7]-1',
            '1,4-dihydropyridine':'[#6]1=[#6]-[#6]-[#6]=[#6]-[#7]-1',
            'pyrimidine-2,4(1H,3H)-dione':'[#8]=[#6]1:[#7H]:[#6](:[#6]:[#6]:[#7H]:1)=[#8]',
            '3,4-dihydro-2H-benzo[e][1,4]diazepin-2-one':'[#8]=[#6]1-[#7]=[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2=[#6]-[#7]-[#6]-1',
            'cyclohexene':'[#6]1=[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'pyrrolidin-2-one':'[#8]=[#6]1-[#7]-[#6]-[#6]-[#6]-1',
            'imidazolidine-2,4-dione':'[#8]=[#6]1-[#6]-[#7]-[#6](-[#7]-1)=[#8]',
            '1,2,3,4-tetrahydroisoquinoline':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#6]-[#7]-[#6]-2',
            '3,4-dihydro-2H-benzo[e][1,2,4]thiadiazine 1,1-dioxide':'[#8]=[#16]1(-[#7]-[#6]-[#7]-[#6]2:[#6]-1:[#6]:[#6]:[#6]:[#6]:2)=[#8]',
            '7,8,9,11,12,13,14,15,16,17-decahydro-6H-cyclopenta[a]phenanthrene':'[#6]-[#6]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6@@H]1-[#6]-[#6@@H]2-[#6]-[#6]-[#6]-[#6]-2-[#6]-[#6]-1',
            '1H-pyrazole':'[#7]1:[#6]:[#6]:[#6]:[#7H]:1',
            'quinuclidine':'[#6]12-[#6]-[#6]-[#7](-[#6]-[#6]-1)-[#6]-[#6]-2',
            'epoxide':'[#6]1-[#6]-[#8]-1',
            'pyrazine':'[#6]1:[#6]:[#7]:[#6]:[#6]:[#7]:1',
            'oxazolidinone':'[#8]=[#6]1-[#8]-[#6]-[#6]-[#7]-1',
            'tetrahydronaphthalene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#6]-[#6]-[#6]-2',
            'adamantane':'[#6]12-[#6]-[#6]3-[#6]-[#6](-[#6]-1)-[#6]-[#6](-[#6]-3)-[#6]-2',
            '1,8-naphthyridin-4(1H)-one':'[#8]=[#6]1:[#6]:[#6]:[#7H]:[#6]2:[#6]:1:[#6]:[#6]:[#6]:[#7]:2',
            '3,7-dihydro-1H-purine-2,6-dione':'[#8]=[#6]1:[#6]2:[#7H]:[#6]:[#7]:[#6]:2:[#7H]:[#6](:[#7H]:1)=[#8]',
            'hexadecahydro-1H-cyclopenta[a]phenanthrene':'[#6]-[#6]-[#6]-[#6@H]1-[#6]-[#6]-[#6]-[#6]-[#6]-1-[#6@@H]1-[#6]-[#6@@H]2-[#6]-[#6]-[#6]-[#6]-2-[#6]-[#6]-1',
            '7,8,9,10-tetrahydrotetracene-5,12-dione':'[#8]=[#6]1-[#6]2:[#6]:[#6]3-[#6]-[#6]-[#6]-[#6]-[#6]:3:[#6]:[#6]:2-[#6](=[#8])-[#6]2:[#6]-1:[#6]:[#6]:[#6]:[#6]:2',
            'cyclobutane':'[#6]1-[#6]-[#6]-[#6]-1',
            '1,2-dihydro-3H-1,2,4-triazol-3-one':'[#8]=[#6]1:[#7H]:[#7H]:[#6]:[#7]:1',
            '1,3,4-thiadiazole':'[#6]1:[#7]:[#7]:[#6]:[#16]:1',
            'azepane':'[#6]1-[#7]-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            '8-azabicyclo[3.2.1]octane':'[#6]12-[#6]-[#6]-[#6]-[#6](-[#6]-[#6]-1)-[#7]-2',
            'piperidine-2,6-dione':'[#8]=[#6]1-[#7]-[#6](-[#6]-[#6]-[#6]-1)=[#8]',
            '2,3-dihydro-1H-indene':'[#8]=[#6]1-[#7]-[#6](-[#6]-[#6]-[#6]-1)=[#8]',
            'benzo[d]isoxazole':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#7]:[#8]:2',
            '1,9-dihydro-6H-purin-6-one':'[#8]=[#6]1:[#6]2:[#6](:[#7H]:[#6]:[#7]:2):[#7]:[#6]:[#7H]:1',
            '9H-fluorene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]1:[#6](:[#6]:[#6]:[#6]:[#6]:1)-[#6]-2',
            '10,11-dihydro-5H-dibenzo[b,f]azepine':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#6]-[#6]1:[#6](:[#6]:[#6]:[#6]:[#6]:1)-[#7]-2',
            '(6aR,10aR)-4,6,6a,7,8,9,10,10a-octahydroindolo[4,3-fg]quinoline':'[#6]12:[#6]:[#6]:[#6]:[#6]3:[#6]:1:[#6](-[#6]-[#6@@H]1-[#6@@H]-2-[#6]-[#6]-[#6]-[#7]-1):[#6]:[#7H]:3',
            '1H-pyrrole':'[#6]1:[#6]:[#6]:[#6]:[#7H]:1',
            '1,3-dioxolane':'[#8]1-[#6]-[#6]-[#8]-[#6]-1',
            '(1R,5S)-3-azabicyclo[3.1.0]hexane':'[#6]1-[#6@@H]2-[#6@H]-1-[#6]-[#7]-[#6]-2',
            'cyclopentanone':'[#8]=[#6]1-[#6]-[#6]-[#6]-[#6]-1',
            'pyrrolidine-2,5-dione':'[#8]=[#6]1-[#7]-[#6](-[#6]-[#6]-1)=[#8]',
            'pyrazolidine':'[#8]=[#6]1-[#7]-[#7]-[#6](-[#6]-1)=[#8]',
            '(R)-1-azabicyclo[3.2.0]hept-2-en-7-one':'[#8]=[#6]1-[#7]2-[#6]=[#6]-[#6]-[#6@@H]-2-[#6]-1',
            'thiazolidine-2,4-dione':'[#8]=[#6]1-[#6]-[#16]-[#6](-[#7]-1)=[#8]',
            'benzofuran':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#8]:2',
            '1H-indazole':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#7]:[#7H]:2',
            'indolin-2-one':'[#8]=[#6]1-[#7]-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2-[#6]-1',
            'benzo[b]thiophene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#16]:2',
            '(R)-1,2,3,7,8,8a-hexahydronaphthalene':'[#6]12=[#6]-[#6]-[#6]-[#6]-[#6@@H]-1-[#6]-[#6]-[#6]=[#6]-2',
            '4,5,6,7-tetrahydrothieno[3,2-c]pyridine':'[#6]12:[#6]:[#6]:[#16]:[#6]:1-[#6]-[#6]-[#7]-[#6]-2',
            '4H-chromen-4-one':'[#8]=[#6]1:[#6]:[#6]:[#8]:[#6]2:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            '3,4-dihydroquino-2(1H)-one':'[#8]=[#6]1-[#6]-[#6]-[#6]2:[#6](-[#7]-1):[#6]:[#6]:[#6]:[#6]:2',
            'napthalene-1,4-dione':'[#8]=[#6]1-[#6]=[#6]-[#6](=[#8])-[#6]2:[#6]-1:[#6]:[#6]:[#6]:[#6]:2',
            '2H-benzo[e][1,2,4]thiadiazine 1,1-dioxide':'[#8]=[#16]1(-[#6]2:[#6](:[#6]:[#6]:[#6]:[#6]:2)-[#7]=[#6]-[#7]-1)=[#8]',
            '4H-benzo[f][1,2,4]triazolo[4,3-a][1,4]diazepine':'[#6]12-[#7]3:[#6](-[#6]-[#7]=[#6]-[#6]:1:[#6]:[#6]:[#6]:[#6]:2):[#7]:[#7]:[#6]:3',
            '9H-thioxanthene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#6]1:[#6](:[#6]:[#6]:[#6]:[#6]:1)-[#16]-2',
            "(5aR,8aR)-5,8,8a,9-tetrahydrofuro[3',4':6,7]naphtho[2,3-d][1,3]dioxol-6(5aH)-one":'[#8]=[#6]1-[#8]-[#6]-[#6@H]2-[#6@H]-1-[#6]-[#6]1:[#6](-[#6]-2):[#6]:[#6]2:[#6](:[#6]:1)-[#8]-[#6]-[#8]-2',
            '(3a1S,5aS,10bS)-3a,3a1,4,5,5a,6,11,12-octahydro-1H-indolizino[8,1-cd]carbazole':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6@@]13-[#6@H](-[#6]-[#6]-[#6]4-[#6@@H]-1-[#7](-[#6]-[#6]=[#6]-4)-[#6]-[#6]-3)-[#7]-2',
            '(4aR,5aR)-4a,5a,6,12a-tetrahydrotetracene-1,11(4H,5H)-dione':'[#8]=[#6]1-[#6]2=[#6]-[#6]3-[#6@H](-[#6]-[#6]=[#6]-[#6]-3=[#8])-[#6]-[#6@@H]-2-[#6]-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2-1',
            '1H-1,2,3-triazole':'[#7]1:[#7]:[#6]:[#6]:[#7H]:1',
            'azetidin-2-one':'[#8]=[#6]1-[#7]-[#6]-[#6]-1',
            'oxetan-2-one':'[#8]=[#6]1-[#8]-[#6]-[#6]-1',
        }

        return smarts