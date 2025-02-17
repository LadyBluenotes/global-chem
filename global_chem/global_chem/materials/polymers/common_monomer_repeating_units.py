#!/usr/bin/env python3
#
# GlobalChem - Common Monomer Repeating Units
#
# -------------------------------------------

class CommonMonomerRepeatingUnits(object):

    def __init__(self):

        self.name = 'common_monomer_repeating_units'

    @staticmethod
    def get_smiles():
        
        '''
        
        Missing Entry: threo-(E)-3-(methoxycarbonyl)-4-methylbut-1-ene-1,4-diyl
        
        '''
        

        smiles = {
            '3′-bromo-2-chloro[1,1′:4′,1′′-terphenyl]-4,4′′': 'ClC1=CC=CC=C1C2=CC=C(C3=CC=CC=C3)C(Br)=C2',
            '[3,3′-biquinoline]-6,6′': 'C1(C2=CC3=CC=CC=C3N=C2)=CC4=CC=CC=C4N=C1',
            '[2,3′-bipyridine]-4,5′': 'C1(C2=CC=CN=C2)=NC=CC=C1',
            '(Z)-but-1-enel': 'C=CCC',
            'ethene-1,2-diyl': 'C=C',
            'propane-1,3-diyl': 'CCC',
            'methylmethylene': '[CH]C',
            '1-phenylethylene': 'C=CC1=CC=CC=C1',
            '1,2-dioxobutane': 'CCC(C=O)=O',
            '1,3-dioxohexane': 'CCCC(CC=O)=O',
            'oxyoxalyl': 'O=CC(O)=O',
            'oxysuccinyl': 'O=CCCC(O)=O',
            'naphthalene': 'C12=CC=CC=C1C=CC=C2',
            '2H-furo[3,2-b]pyran': 'C12=CCOC1=CC=CO2',
            'pyridine': 'C1=NC=CC=C1',
            '1-carboxylatoethylene': 'NC1(C(O)=O)CC1',
            'x-iminocyclopentane': 'N=C1CCCC1',
            'pyridine-3,5-diylpiperidine': 'N1(C2=CC3=CN=C2)C3CCCC1',
            '(4-chloro[3,3′-bipyridine])methylene': '[CH]C1=NC=CC(Cl)=C1C2=CC=CN=C2',
            'imino[1-oxo-2-(phenylsulfanyl)ethylene]': 'O=C=C(N)SC1=CC=CC=C1',
            'methylphenylsiloxane': '[H]O[SiH](C)C1=CC=CC=C1',
            'diethoxyphosphazene': 'CCO[PH2](N)OCC',
            'piperidine-3,5-diylideneethanediylidene': 'C/C=C1CNCCC1',
            'sulfanediylcarbonyl': 'O=[CH]S',
            'spiro[4.5]decane-2,8-diylmethylene': 'C1(CC(CC2)CC3)CC32CC1',
            '4H-1,2,4-triazole-3,5-diylmethylene': 'C1(C2)=NN=C2N1',
            '(2-phenyl-1,3-phenylene)ethylene': 'C1(C=C2)=CC=CC2=C1C3=CC=CC=C3',
            '(5′-chloro[1,2′-binaphthalene])methylene': 'CC1=CC=C2C=CC=CC2=C1C3=CC=C4C(Cl)=CC=CC4=C3',
            '(6-chlorocyclohex-1-ene)(1-bromoethylene)': 'ClC1C=CC(C(Br)C)CC1',
            'oxy{[3-(trifluoromethyl)phenyl]methylene}': 'FC(C1=CC([CH]O)=CC=C1)(F)F',
            '1,3-phenyleneethylene': 'C1(C=C2)=CC=CC2=C1',
            '(tetramethoxy-1,4-phenylene)(1,2-diphenylethene)': 'COC(C(OC)=CC(OC)=C1OC)=C1/C(C2=CC=CC=C2)=C/C3=CC=CC=C3',
            '(1,1′,3,3′-tetraoxo[5,5′-biisoindoline]-2,2′-diyl)biphenyl': 'O=C(C1=C2C=CC(C3=CC=C4C(OCN(C5=CC=C(C6=CC=CC=C6)C=C5)CO4)=C3)=C1)NC2=O',
            'morpholine-2,6-diylpyridine-3,5-diylthianthrene': 'C(C=C1S2)(C3=CN=CC(C4CNCCO4)=C3)=CC=C1SC5=C2C=CC=C5',
            'naphthalene-1,4-phenylenecyclohexane': 'C12=CC=CC=C1C=C(C3=CC=CC(C4CCCCC4)=C3)C=C2',
            'pyridine-1,4-phenylenecyclopentane': 'C1(C2=CC=CC(C3CCCC3)=C2)=CC=CN=C1',
            'pyridine-4H-1,2,4-triazole-3,5-diylmethylene': 'CC(N1)=NN=C1C2=NC=CC=C2',
            'oxyspiro[3.5]nona-2,5-diene-7,1-diylcyclohex-4-ene-1,3-diyl': 'OC1C=CC2(CCC2C3CC=CCC3)CC1',
            'piperidine-oxymethylene': 'COC1NCCCC1',
            'pyridine-methyleneoxy-1,4-phenylene': 'C1(OCC2=NC=CC=C2)=CC=CC=C1',
            'imino(1-chloro-2-oxoethylene)(4-nitro-1,3-phenylene)(3-bromopropane)': 'NC(C(C1=CC=C([N+]([O-])=O)C(CCBr)=C1)=O)Cl',
            'pyridine-acenaphthylene-3,8-diylpyrrole-diylacenaphthylene': 'C1(C2=C(C=C3)C(C3=C(C4=CNC=C4C5=C(C=C6)C(C6=CC=C7)=C7C=C5)C=C8)=C8C=C2)=CC=CN=C1',
            'pyridine-(phenylmethylene)iminocyclohexane': 'C1(C(NC2CCCCC2)C3=CC=CC=C3)=CC=CC=N1',
            '(methylimino)methyleneimino-1,3-phenylene': 'CNCNC1=CC=CC=C1',
            'pyridine-diyliminocyclohexane(phenylmethylene)': 'C1(NC2CCC(CC3=CC=CC=C3)CC2)=CC=CC=N1',
            'imino(1-oxoethylene)silanediylpropane': 'NC(C[Si](C)(C)C)=O',
            'pyridine-cyclohexane-oxypropane': 'CCCOC(CCC1)CC1C2=CC=CN=C2',
            'sulfaneethylenesulfanediyl(2-amino-4-carboxypentane)': 'SCCSC(N)CC(C)C(O)=O',
            'sulfaneethylenesulfanediyl(4-amino-1-carboxypentane)': 'SCCSC(C(O)=O)CC(N)C',
            'pyridine-methylenepyridine(tetrahydropyran)': 'C1(CC2=CN=CC(C3COCCC3)=C2)=CC=CN=C1',
            'sulfane(2-chloropropane)sulfanepropane': 'SCC(CSCCC)Cl',
            'pyridine-carbonyloxymethylene': 'O=C(OC)C1=CC=CN=C1',
            '1,3-phenylene(1-bromoethylene)cyclohexane(2-butylethylene)': 'BrC(C1CCCC(C(CCC)C)C1)C2=CC=CC=C2',
            'oxy(1,1-dichloroethylene)imino(1-oxoethylene)': 'OC(Cl)(CNCOC)Cl',
            'sulfane(1-chloroethylene)-1,3-phenylene(1-chloroethylene)': 'SC(CC1=CC(C(C)Cl)=CC=C1)Cl',
            'sulfane(1-iodoethylene)sulfane(5-bromo-3-chloropentane)': 'SC(CSCCC(CCBr)Cl)I',
            'oxymethylene-ONN-azoxy(chloromethylene)': 'OCN(O)-NCCl',
            '(3-chlorobiphenyl)methylene(3-chloro-1,4-phenylene)methylene': 'ClC1=CC(C2=CC=C(C3=CC=C(C)C(Cl)=C3)C=C2)=CC=C1',
            'imino(x-methyl-1,3-phenylene)iminomalonyl': 'NC1=CC(C)=CC(NC(CC=O)=O)=C1',
            'oxyhexane-oxycarbonylimino(methylphenylene)iminocarbonyl': 'OCCCCCCOC(NC1=CC(C)=C(NC=O)C=C1)=O',
            '2,4,8,10-tetraoxaspiro[5.5]undecane-oxyhexane-1,6-diyloxy': 'CC1OCC2(COC(OCCCCCCO)OC2)CO1',
            'pyridine-methylenepyrrole-oxymethylene': 'COC1=CNC=C1CC2=CC=CN=C2',
            'oxymethyleneiminocarbonylsulfane-1,3-phenyleneethylene': 'COCNC(SC1=CC=CC(CC)=C1)=O',
            'oxyiminomethylenehydrazine-methylene': 'ONCNNC',
            'piperidine-methylenepiperidine-4,2-diylcyclopentane-ethylenecyclopentane-1,2-diylmethylene': 'CC(C1)CCC1CC(C2)CCC2C(C3)NCCC3CC4NCCCC4',
            '1,3-dioxa-8-thia-5,10-diazadodecane': 'OCOCNCCSCNCC',
            'oxymethyleneoxymethyleneoxymethyleneimino-1,3-phenylenemethyleneiminomethylene': 'OCOCOCNC1=CC(CNC)=CC=C1',
            'pyridine-1,4-phenylenemethyleneoxymethyleneiminomethyleneoxy-1,4-phenylenemethylene': 'CC(C=C1)=CC=C1OCNCOCC(C=C2)=CC=C2C3=CC=CN=C3',
            'sulfinylmethylenesulfanediylpropane-1,3-diylsulfonyl-1,4-phenylene': 'SOCSCCCS(=O)(C1=CC=CC=C1)=O',
            'oxyterephthaloylhydrazine-terephthaloyl': 'OC(C1=CC=C(C(NNC(C2=CC=C(C=O)C=C2)=O)=O)C=C1)=O',
            'nitrilo-1,4-phenylenenitriloprop-2-en-3-yl-1-ylidene-1,4-phenyleneprop-1-en-1-yl-3-ylidene': 'NC1=CC=C(N=CC=CC2=CC=C(C=CCC)C=C2)C=C1',
            'oxycarbonylnitrilopropane-idenenitrilocarbonyl': 'OC(N=CCC=NC=O)=O',
            'oxyethyleneiminomethylenesulfanediylethyleneiminocyclohexane': 'OCCCNCSCCNC1CCCCC1',
            'iminomethyleneiminocarbonyl{2-[(2,4-dinitrophenyl)hydrazono]cyclopentane}carbonyl': 'OC(C1=CC=C(C(OCCCCCC)=O)C=C1)=O',
            'oxyterephthaloyloxyhexane': 'NCCNC(C1/C(C(C=O)CC1)=N/NC2=C([N+]([O-])=O)C=C([N+]([O-])=O)C=C2)=O',
            'nitrilocyclohexa-2,5-diene-idenenitrilo-1,4-phenyleneimino-1,4-phenyleneimino1,4-phenylene': 'N=C1C=CC(C=C1)=NC2=CC=C(NC3=CC=C(NC4=CC=CC=C4)C=C3)C=C2',
            'cyclohexane-methanylylidenecyclohexane-idenemethanylylidenecyclohexane-methylene': 'CC(CC1)CCC1C=C(CC2)CCC2=CC3CCCCC3'
        }

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {
            '3′-bromo-2-chloro[1,1′:4′,1′′-terphenyl]-4,4′′': '[#17]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]1:[#6]:[#6]:[#6](-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2):[#6](-[#35]):[#6]:1',
            '[3,3′-biquinoline]-6,6′': '[#6]1(-[#6]2:[#6]:[#6]3:[#6]:[#6]:[#6]:[#6]:[#6]:3:[#7]:[#6]:2):[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#7]:[#6]:1',
            '[2,3′-bipyridine]-4,5′': '[#6]1(-[#6]2:[#6]:[#6]:[#6]:[#7]:[#6]:2):[#7]:[#6]:[#6]:[#6]:[#6]:1',
            '(Z)-but-1-enel': '[#6]=[#6]-[#6]-[#6]',
            'threo-(E)-3-(methoxycarbonyl)-4-methylbut-1-ene-1,4-diyl': '*',
            'ethene-1,2-diyl': '[#6]=[#6]',
            'propane-1,3-diyl': '[#6]-[#6]-[#6]',
            'methylmethylene': '[#6H]-[#6]',
            '1-phenylethylene': '[#6]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '1,2-dioxobutane': '[#6]-[#6]-[#6](-[#6]=[#8])=[#8]',
            '1,3-dioxohexane': '[#6]-[#6]-[#6]-[#6](-[#6]-[#6]=[#8])=[#8]',
            'oxyoxalyl': '[#8]=[#6]-[#6](-[#8])=[#8]',
            'oxysuccinyl': '[#8]=[#6]-[#6]-[#6]-[#6](-[#8])=[#8]',
            'naphthalene': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            '2H-furo[3,2-b]pyran': '[#6]12=[#6]-[#6]-[#8]-[#6]-1=[#6]-[#6]=[#6]-[#8]-2',
            'pyridine': '[#6]1:[#7]:[#6]:[#6]:[#6]:[#6]:1',
            '1-carboxylatoethylene': '[#7]-[#6]1(-[#6](-[#8])=[#8])-[#6]-[#6]-1',
            'x-iminocyclopentane': '[#7]=[#6]1-[#6]-[#6]-[#6]-[#6]-1',
            'pyridine-3,5-diylpiperidine': '[#7]12-[#6]3:[#6]:[#6](:[#6]:[#7]:[#6]:3)-[#6]-1-[#6]-[#6]-[#6]-[#6]-2',
            '(4-chloro[3,3′-bipyridine])methylene': '[#6H]-[#6]1:[#7]:[#6]:[#6]:[#6](-[#17]):[#6]:1-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'imino[1-oxo-2-(phenylsulfanyl)ethylene]': '[#8]=[#6]=[#6](-[#7])-[#16]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'methylphenylsiloxane': '[#8H]-[SiH](-[#6])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'diethoxyphosphazene': '[#6]-[#6]-[#8]-[#15H2](-[#7])-[#8]-[#6]-[#6]',
            'piperidine-3,5-diylideneethanediylidene': '[#6]-[#6]=[#6]1-[#6]-[#7]-[#6]-[#6]-[#6]-1',
            'sulfanediylcarbonyl': '[#8]=[#6H]-[#16]',
            'spiro[4.5]decane-2,8-diylmethylene': '[#6]12-[#6]-[#6]3-[#6]-[#6]-[#6](-[#6]-[#6]-3)(-[#6]-1)-[#6]-[#6]-2',
            '4H-1,2,4-triazole-3,5-diylmethylene': '[#6]12-[#6]-[#6](:[#7]:[#7]:1):[#7H]:2',
            '(2-phenyl-1,3-phenylene)ethylene': '[#6]12-[#6]=[#6]-[#6](:[#6]:[#6]:[#6]:1):[#6]:2-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '(5′-chloro[1,2′-binaphthalene])methylene': '[#6]-[#6]1:[#6]:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#6]:1-[#6]1:[#6]:[#6]:[#6]2:[#6](-[#17]):[#6]:[#6]:[#6]:[#6]:2:[#6]:1',
            '(6-chlorocyclohex-1-ene)(1-bromoethylene)': '[#17]-[#6]1-[#6]=[#6]-[#6](-[#6](-[#35])-[#6])-[#6]-[#6]-1',
            'oxy{[3-(trifluoromethyl)phenyl]methylene}': '[#9]-[#6](-[#6]1:[#6]:[#6](-[#6H]-[#8]):[#6]:[#6]:[#6]:1)(-[#9])-[#9]',
            '1,3-phenyleneethylene': '[#6]12-[#6]=[#6]-[#6](:[#6]:[#6]:[#6]:1):[#6]:2',
            '(tetramethoxy-1,4-phenylene)(1,2-diphenylethene)': '[#6]-[#8]-[#6]1:[#6](-[#8]-[#6]):[#6]:[#6](-[#8]-[#6]):[#6](-[#8]-[#6]):[#6]:1/[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)=[#6]/[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '(1,1′,3,3′-tetraoxo[5,5′-biisoindoline]-2,2′-diyl)biphenyl': '[#8]=[#6]1-[#6]2:[#6](:[#6]:[#6]:[#6](-[#6]3:[#6]:[#6]:[#6]4:[#6](-[#8]-[#6]-[#7](-[#6]5:[#6]:[#6]:[#6](-[#6]6:[#6]:[#6]:[#6]:[#6]:[#6]:6):[#6]:[#6]:5)-[#6]-[#8]-4):[#6]:3):[#6]:2)-[#6](-[#7]-1)=[#8]',
            'morpholine-2,6-diylpyridine-3,5-diylthianthrene': '[#6]1(:[#6]:[#6]2-[#16]-[#6]3:[#6](-[#16]-[#6]:2:[#6]:[#6]:1):[#6]:[#6]:[#6]:[#6]:3)-[#6]1:[#6]:[#7]:[#6]:[#6](-[#6]2-[#6]-[#7]-[#6]-[#6]-[#8]-2):[#6]:1',
            'naphthalene-1,4-phenylenecyclohexane': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6](-[#6]1:[#6]:[#6]:[#6]:[#6](-[#6]3-[#6]-[#6]-[#6]-[#6]-[#6]-3):[#6]:1):[#6]:[#6]:2',
            'pyridine-1,4-phenylenecyclopentane': '[#6]1(-[#6]2:[#6]:[#6]:[#6]:[#6](-[#6]3-[#6]-[#6]-[#6]-[#6]-3):[#6]:2):[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'pyridine-4H-1,2,4-triazole-3,5-diylmethylene': '[#6]-[#6]1:[#7H]:[#6](:[#7]:[#7]:1)-[#6]1:[#7]:[#6]:[#6]:[#6]:[#6]:1',
            'oxyspiro[3.5]nona-2,5-diene-7,1-diylcyclohex-4-ene-1,3-diyl': '[#8]-[#6]1-[#6]=[#6]-[#6]2(-[#6]-[#6]-[#6]-2-[#6]2-[#6]-[#6]=[#6]-[#6]-[#6]-2)-[#6]-[#6]-1',
            'piperidine-oxymethylene': '[#6]-[#8]-[#6]1-[#7]-[#6]-[#6]-[#6]-[#6]-1',
            'pyridine-methyleneoxy-1,4-phenylene': '[#6]1(-[#8]-[#6]-[#6]2:[#7]:[#6]:[#6]:[#6]:[#6]:2):[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'imino(1-chloro-2-oxoethylene)(4-nitro-1,3-phenylene)(3-bromopropane)': '[#7]-[#6](-[#6](-[#6]1:[#6]:[#6]:[#6](-[#7+](-[#8-])=[#8]):[#6](-[#6]-[#6]-[#35]):[#6]:1)=[#8])-[#17]',
            'pyridine-acenaphthylene-3,8-diylpyrrole-diylacenaphthylene': '[#6]1(-[#6]2:[#6]3-[#6]=[#6]-[#6]4:[#6]:3:[#6](:[#6]:[#6]:[#6]:4-[#6]3:[#6]:[#7H]:[#6]:[#6]:3-[#6]3:[#6]4-[#6]=[#6]-[#6]5:[#6]:4:[#6](:[#6]:[#6]:[#6]:5):[#6]:[#6]:3):[#6]:[#6]:2):[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'pyridine-(phenylmethylene)iminocyclohexane': '[#6]1(-[#6](-[#7]-[#6]2-[#6]-[#6]-[#6]-[#6]-[#6]-2)-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2):[#6]:[#6]:[#6]:[#6]:[#7]:1',
            '(methylimino)methyleneimino-1,3-phenylene': '[#6]-[#7]-[#6]-[#7]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'pyridine-diyliminocyclohexane(phenylmethylene)': '[#6]1(-[#7]-[#6]2-[#6]-[#6]-[#6](-[#6]-[#6]3:[#6]:[#6]:[#6]:[#6]:[#6]:3)-[#6]-[#6]-2):[#6]:[#6]:[#6]:[#6]:[#7]:1',
            'imino(1-oxoethylene)silanediylpropane': '[#7]-[#6](-[#6]-[Si](-[#6])(-[#6])-[#6])=[#8]',
            'pyridine-cyclohexane-oxypropane': '[#6]-[#6]-[#6]-[#8]-[#6]1-[#6]-[#6]-[#6]-[#6](-[#6]-1)-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'sulfaneethylenesulfanediyl(2-amino-4-carboxypentane)': '[#16]-[#6]-[#6]-[#16]-[#6](-[#7])-[#6]-[#6](-[#6])-[#6](-[#8])=[#8]',
            'sulfaneethylenesulfanediyl(4-amino-1-carboxypentane)': '[#16]-[#6]-[#6]-[#16]-[#6](-[#6](-[#8])=[#8])-[#6]-[#6](-[#7])-[#6]',
            'pyridine-methylenepyridine(tetrahydropyran)': '[#6]1(-[#6]-[#6]2:[#6]:[#7]:[#6]:[#6](-[#6]3-[#6]-[#8]-[#6]-[#6]-[#6]-3):[#6]:2):[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'sulfane(2-chloropropane)sulfanepropane': '[#16]-[#6]-[#6](-[#6]-[#16]-[#6]-[#6]-[#6])-[#17]',
            'pyridine-carbonyloxymethylene': '[#8]=[#6](-[#8]-[#6])-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            '1,3-phenylene(1-bromoethylene)cyclohexane(2-butylethylene)': '[#35]-[#6](-[#6]1-[#6]-[#6]-[#6]-[#6](-[#6](-[#6]-[#6]-[#6])-[#6])-[#6]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'oxy(1,1-dichloroethylene)imino(1-oxoethylene)': '[#8]-[#6](-[#17])(-[#6]-[#7]-[#6]-[#8]-[#6])-[#17]',
            'sulfane(1-chloroethylene)-1,3-phenylene(1-chloroethylene)': '[#16]-[#6](-[#6]-[#6]1:[#6]:[#6](-[#6](-[#6])-[#17]):[#6]:[#6]:[#6]:1)-[#17]',
            'sulfane(1-iodoethylene)sulfane(5-bromo-3-chloropentane)': '[#16]-[#6](-[#6]-[#16]-[#6]-[#6]-[#6](-[#6]-[#6]-[#35])-[#17])-[#53]',
            'oxymethylene-ONN-azoxy(chloromethylene)': '[#8]-[#6]-[#7](-[#8])-[#7]-[#6]-[#17]',
            '(3-chlorobiphenyl)methylene(3-chloro-1,4-phenylene)methylene': '[#17]-[#6]1:[#6]:[#6](-[#6]2:[#6]:[#6]:[#6](-[#6]3:[#6]:[#6]:[#6](-[#6]):[#6](-[#17]):[#6]:3):[#6]:[#6]:2):[#6]:[#6]:[#6]:1',
            'imino(x-methyl-1,3-phenylene)iminomalonyl': '[#7]-[#6]1:[#6]:[#6](-[#6]):[#6]:[#6](-[#7]-[#6](-[#6]-[#6]=[#8])=[#8]):[#6]:1',
            'oxyhexane-oxycarbonylimino(methylphenylene)iminocarbonyl': '[#8]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#8]-[#6](-[#7]-[#6]1:[#6]:[#6](-[#6]):[#6](-[#7]-[#6]=[#8]):[#6]:[#6]:1)=[#8]',
            '2,4,8,10-tetraoxaspiro[5.5]undecane-oxyhexane-1,6-diyloxy': '[#6]-[#6]1-[#8]-[#6]-[#6]2(-[#6]-[#8]-[#6](-[#8]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#8])-[#8]-[#6]-2)-[#6]-[#8]-1',
            'pyridine-methylenepyrrole-oxymethylene': '[#6]-[#8]-[#6]1:[#6]:[#7H]:[#6]:[#6]:1-[#6]-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'oxymethyleneiminocarbonylsulfane-1,3-phenyleneethylene': '[#6]-[#8]-[#6]-[#7]-[#6](-[#16]-[#6]1:[#6]:[#6]:[#6]:[#6](-[#6]-[#6]):[#6]:1)=[#8]',
            'oxyiminomethylenehydrazine-methylene': '[#8]-[#7]-[#6]-[#7]-[#7]-[#6]',
            'piperidine-methylenepiperidine-4,2-diylcyclopentane-ethylenecyclopentane-1,2-diylmethylene': '[#6]-[#6]1-[#6]-[#6](-[#6]-[#6]-1)-[#6]-[#6]1-[#6]-[#6](-[#6]-[#6]-1)-[#6]1-[#6]-[#6](-[#6]-[#6]-[#7]-1)-[#6]-[#6]1-[#7]-[#6]-[#6]-[#6]-[#6]-1',
            '1,3-dioxa-8-thia-5,10-diazadodecane': '[#8]-[#6]-[#8]-[#6]-[#7]-[#6]-[#6]-[#16]-[#6]-[#7]-[#6]-[#6]',
            'oxymethyleneoxymethyleneoxymethyleneimino-1,3-phenylenemethyleneiminomethylene': '[#8]-[#6]-[#8]-[#6]-[#8]-[#6]-[#7]-[#6]1:[#6]:[#6](-[#6]-[#7]-[#6]):[#6]:[#6]:[#6]:1',
            'pyridine-1,4-phenylenemethyleneoxymethyleneiminomethyleneoxy-1,4-phenylenemethylene': '[#6]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#8]-[#6]-[#7]-[#6]-[#8]-[#6]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'sulfinylmethylenesulfanediylpropane-1,3-diylsulfonyl-1,4-phenylene': '[#16]-[#8]-[#6]-[#16]-[#6]-[#6]-[#6]-[#16](=[#8])(-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)=[#8]',
            'oxyterephthaloylhydrazine-terephthaloyl': '[#8]-[#6](-[#6]1:[#6]:[#6]:[#6](-[#6](-[#7]-[#7]-[#6](-[#6]2:[#6]:[#6]:[#6](-[#6]=[#8]):[#6]:[#6]:2)=[#8])=[#8]):[#6]:[#6]:1)=[#8]',
            'nitrilo-1,4-phenylenenitriloprop-2-en-3-yl-1-ylidene-1,4-phenyleneprop-1-en-1-yl-3-ylidene': '[#7]-[#6]1:[#6]:[#6]:[#6](-[#7]=[#6]-[#6]=[#6]-[#6]2:[#6]:[#6]:[#6](-[#6]=[#6]-[#6]-[#6]):[#6]:[#6]:2):[#6]:[#6]:1',
            'oxycarbonylnitrilopropane-idenenitrilocarbonyl': '[#8]-[#6](-[#7]=[#6]-[#6]-[#6]=[#7]-[#6]=[#8])=[#8]',
            'oxyethyleneiminomethylenesulfanediylethyleneiminocyclohexane': '[#8]-[#6]-[#6]-[#6]-[#7]-[#6]-[#16]-[#6]-[#6]-[#7]-[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'iminomethyleneiminocarbonyl{2-[(2,4-dinitrophenyl)hydrazono]cyclopentane}carbonyl': '[#8]-[#6](-[#6]1:[#6]:[#6]:[#6](-[#6](-[#8]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6])=[#8]):[#6]:[#6]:1)=[#8]',
            'oxyterephthaloyloxyhexane': '[#7]-[#6]-[#6]-[#7]-[#6](-[#6]1/[#6](-[#6](-[#6]=[#8])-[#6]-[#6]-1)=[#7]/[#7]-[#6]1:[#6](-[#7+](-[#8-])=[#8]):[#6]:[#6](-[#7+](-[#8-])=[#8]):[#6]:[#6]:1)=[#8]',
            'nitrilocyclohexa-2,5-diene-idenenitrilo-1,4-phenyleneimino-1,4-phenyleneimino1,4-phenylene': '[#7]=[#6]1-[#6]=[#6]-[#6](-[#6]=[#6]-1)=[#7]-[#6]1:[#6]:[#6]:[#6](-[#7]-[#6]2:[#6]:[#6]:[#6](-[#7]-[#6]3:[#6]:[#6]:[#6]:[#6]:[#6]:3):[#6]:[#6]:2):[#6]:[#6]:1',
            'cyclohexane-methanylylidenecyclohexane-idenemethanylylidenecyclohexane-methylene': '[#6]-[#6]1-[#6]-[#6]-[#6](-[#6]-[#6]-1)-[#6]=[#6]1-[#6]-[#6]-[#6](-[#6]-[#6]-1)=[#6]-[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
        }

        return smarts