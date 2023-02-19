import matplotlib.pyplot as plt

# dict = {'001': '使用中', '002': '临时离开', '003': '使用中', '004': '使用中', '005': '使用中', '006': '空闲', '007': '使用中', '008': '使用中', '009': '临时离开', '010': '使用中', '011': '使用中', '012': '空闲', '013': '使用中', '014': '使用中', '015': '使用中', '016': '使用中', '017': '使用中', '018': '使用中', '019': '使用中', '020': '使用中', '021': '使用中', '022': '使用中', '023': '使用中', '024': '使用中', '025': '使用中', '026': '临时离开', '027': '使用中', '028': '使用中', '029': '使用中', '030': '使用中', '031': '空闲', '032': '使用中', '033': '使用中', '034': '使用中', '035': '使用中', '036': '使用中', '037': '使用中', '038': '使用中', '039': '使用中', '040': '使用中', '041': '使用中', '042': '使用中', '043': '使用中', '044': '临时离开', '045': '使用中', '046': '使用中', '047': '使用中', '048': '使用中', '049': '使用中', '050': '使用中', '051': '空闲', '052': '使用中', '053': '使用中', '054': '使用中', '055': '使用中', '056': '使用中', '057': '使用中', '058': '使用中', '059': '使用中', '060': '使用中', '061': '使用中', '062': '空闲', '063': '使用中', '064': '空闲', '065': '使用中', '066': '使用中', '067': '使用中', '068': '空闲', '069': '使用中', '070': '使用中', '071': '使用中', '072': '使用中', '073': '使用中', '074': '使用中', '075': '使用中', '076': '使用中', '077': '使用中', '078': '使用中', '079': '空闲', '080': '使用中', '081': '使用中', '082': '使用中', '083': '使用中', '084': '使用中', '085': '空闲', '086': '使用中', '087': '使用中', '088': '使用中', '089': '使用中', '090': '使用中', '091': '使用中', '092': '临时离开', '093': '使用中', '094': '使用中', '095': '使用中', '096': '使用中', '097': '使用中', '098': '使用中', '099': '使用中', '100': '空闲', '101': '使用中', '102': '使用中', '103': '使用中', '104': '使用中', '105': '使用中', '106': '使用中', '107': '使用中', '108': '使用中', '109': '使用中', '110': '使用中', '111': '使用中', '112': '使用中', '113': '空闲', '114': '使用中', '115': '使用中', '116': '使用中', '117': '使用中', '118': '使用中', '119': '使用中', '120': '使用中', '121': '临时离开', '122': '使用中', '123': '空闲', '124': '使用中', '125': '使用中', '126': '使用中', '127': '使用中', '128': '使用中', '129': '使用中', '130': '使用中', '131': '使用中', '132': '使用中', '133': '使用中', '134': '使用中', '135': '使用中', '136': '使用中', '137': '使用中', '138': '空闲', '139': '使用中', '140': '使用中', '141': '使用中', '142': '使用中', '143': '使用中', '144': '使用中', '145': '使用中', '146': '临时离开', '147': '使用中', '148': '使用中', '149': '使用中', '150': '使用中', '151': '使用中', '152': '使用中', '153': '使用中', '154': '使用中', '155': '使用中', '156': '使用中', '157': '使用中', '158': '使用中', '159': '使用中', '160': '空闲', '161': '使用中', '162': '使用中', '163': '使用中', '164': '使用中', '165': '使用中', '166': '使用中', '167': '使用中', '168': '使用中', '169': '空闲', '170': '使用中', '171': '使用中', '172': '使用中', '173': '空闲', '174': '使用中', '175': '使用中', '176': '使用中', '177': '使用中', '178': '使用中', '179': '使用中', '180': '使用中', '181': '使用中', '182': '空闲', '183': '使用中', '184': '空闲', '185': '使用中', '186': '使用中', '187': '使用中', '188': '使用中', '189': '使用中', '190': '使用中', '191': '使用中', '192': '空闲', '193': '使用中', '194': '使用中', '195': '使用中', '196': '使用中', '197': '使用中', '198': '使用中', '199': '使用中', '200': '空闲', '201': '空闲', '202': '使用中', '203': '使用中', '204': '空闲', '205': '使用中', '206': '使用中', '207': '已预约', '208': '使用中', '209': '使用中', '210': '使用中', '211': '使用中', '212': '使用中', '213': '使用中', '214': '使用中', '215': '使用中', '216': '空闲', '217': '使用中', '218': '使用中', '219': '使用中', '220': '使用中', '221': '使用中', '222': '使用中', '223': '使用中', '224': '空闲', '225': '使用中', '226': '使用中', '227': '使用中', '228': '使用中', '229': '使用中', '230': '使用中', '231': '使用中', '232': '使用中', '233': '使用中', '234': '使用中', '235': '使用中', '236': '使用中', '237': '空闲', '238': '空闲', '239': '使用中', '240': '空闲', '241': '使用中', '242': '使用中', '243': '使用中', '244': '使用中', '245': '空闲', '246': '已预约', '247': '空闲', '248': '使用中', '249': '使用中', '250': '使用中', '251': '使用中', '252': '使用中', '253': '使用中', '254': '使用中', '255': '使用中', '256': '使用中', '257': '使用中', '258': '使用中', '259': '使用中', '260': '使用中', '261': '使用中', '262': '使用中', '263': '使用中', '264': '空闲', '265': '使用中', '266': '使用中', '267': '临时离开', '268': '使用中', '269': '使用中', '270': '使用中', '271': '使用中', '272': '空闲', '273': '使用中', '274': '使用中', '275': '临时离开', '276': '空闲', '277': '使用中', '278': '使用中', '279': '使用中', '280': '使用中', '281': '使用中', '282': '使用中', '283': '空闲', '284': '使用中', '285': '使用中', '286': '空闲', '287': '使用中', '288': '使用中', '289': '使用中', '290': '使用中', '291': '使用中', '292': '使用中', '293': '使用中', '294': '使用中', '295': '使用中', '296': '空闲', '297': '空闲', '298': '使用中', '299': '使用中', '300': '空闲', '301': '使用中', '302': '使用中', '303': '使用中', '304': '使用中', '305': '使用中', '306': '使用中', '307': '使用中', '308': '使用中', '309': '使用中', '310': '空闲', '311': '空闲', '312': '使用中', '313': '临时离开', '314': '临时离开', '315': '使用中', '316': '使用中', '317': '临时离开', '318': '使用中', '319': '使用中', '320': '使用中', '321': '使用中', '322': '使用中', '323': '使用中', '324': '使用中', '325': '使用中', '326': '使用中', '327': '使用中', '328': '使用中', '329': '使用中', '330': '使用中', '331': '使用中', '332': '空闲', '333': '使用中', '334': '临时离开', '335': '使用中', '336': '使用中', '337': '使用中', '338': '使用中', '339': '使用中', '340': '使用中', '341': '使用中', '342': '使用中', '343': '使用中', '344': '使用中', '345': '使用中', '346': '使用中', '347': '使用中', '348': '空闲', '349': '使用中', '350': '使用中', '351': '使用中', '352': '使用中', '353': '使用中', '354': '空闲', '355': '使用中', '356': '使用中', '357': '使用中', '358': '使用中', '359': '使用中', '360': '使用中', '361': '使用中', '362': '临时离开', '363': '使用中', '364': '使用中', '365': '空闲', '366': '使用中', '367': '使用中', '368': '使用中', '369': '空闲', '370': '使用中', '371': '使用中', '372': '空闲', '373': '使用中', '374': '使用中', '375': '使用中', '376': '使用中', '377': '空闲', '378': '使用中', '379': '使用中', '380': '使用中', '381': '空闲', '382': '空闲', '383': '使用中', '384': '使用中', '385': '使用中', '386': '使用中', '387': '使用中', '388': '使用中', '389': '使用中', '390': '使用中', '391': '使用中', '392': '使用中', '393': '使用中', '394': '使用中', '395': '使用中', '396': '空闲', '397': '使用中', '398': '使用中', '399': '使用中', '400': '使用中', '401': '空闲', '402': '使用中', '403': '使用中', '404': '使用中', '405': '使用中', '406': '使用中', '407': '空闲', '408': '空闲', '409': '使用中', '410': '使用中', '411': '使用中', '412': '空闲', '413': '使用中', '414': '空闲', '415': '使用中', '416': '使用中', '417': '使用中', '418': '使用中', '419': '使用中', '420': '使用中', '421': '使用中', '422': '空闲', '423': '使用中', '424': '使用中', '425': '使用中', '426': '使用中', '427': '使用中', '428': '使用中', '429': '空闲', '430': '使用中', '431': '使用中', '432': '空闲', '433': '使用中', '434': '使用中', '435': '使用中', '436': '使用中', '437': '使用中', '438': '使用中', '439': '使用中', '440': '使用中', '441': '空闲', '442': '使用中', '443': '使用中', '444': '使用中', '445': '使用中', '446': '使用中', '447': '使用中', '448': '使用中', '449': '空闲', '450': '使用中', '451': '临时离开', '452': '空闲', '453': '空闲', '454': '使用中', '455': '使用中', '456': '空闲', '457': '使用中', '458': '空闲', '459': '使用中', '460': '使用中', '461': '使用中', '462': '空闲', '463': '使用中', '464': '使用中', '465': '使用中', '466': '使用中', '467': '使用中', '468': '使用中'}
def pei(dict):
    x_1 = 0 # 空闲数
    x_2 = 0
    for i in dict.items():
        if i[1] == '空闲':
            x_1 += 1
        else:
            x_2 += 1
    # print(x_1,x_2)
    plt.pie([x_1,x_2],
    labels=['free {}'.format(x_1),'busy {}'.format(x_2)],
    colors=['g','r'],
    autopct='%.2f%%',)
    plt.title("time")
    plt.show()
