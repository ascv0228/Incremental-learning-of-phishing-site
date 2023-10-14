
import csv
# import features as fsm

#Function to extract features

files = {
    'new': ['dataset/new_image.csv'],
    'normal' : ["dataset/normal_image.csv"],
    'phishing' : ["dataset/phishing_image.csv"],
    'test' : ["dataset/testData.csv"],
    'train' : ["dataset/trainData.csv"]

}


depth = 0
domain_file = files['train'][0]
output_feature = domain_file[:-4] + '_2.csv'
son_domain_list = ['gov', 'edu', 'int', 'org', 'net', 'com', 'country_son', 'site', 'top', 'shop', 'Rare']
def son_domain(domain:str):
    son = domain[domain.rfind('.')+1:]
    country_son = ['al', 'dz', 'af', 'ar', 'ae', 'aw', 'om', 'az', 'eg', 'et', 'ie', 'ee', 'ad', 'ao', 'ai', 'ag', 'at', 'au', 'mo', 'bb', 'pg', 'bs', 'pk', 'py', 'ps', 'bh', 'pa', 'br', 'by', 'bm', 'bg', 'mp', 'bj', 'be', 'is', 'pr', 'ba', 'pl', 'bo', 'bz', 'bw', 'bt', 'bf', 'bi', 'bv', 'kp', 'gq', 'dk', 'de', 'tp', 'tg', 'dm', 'do', 'ru', 'ec', 'er', 'fr', 'fo', 'pf', 'gf', 'tf', 'va', 'ph', 'fj', 'fi', 'cv', 'fk', 'gm', 'cg', 'cd', 'co', 'cr', 'gg', 'gd', 'gl', 'ge', 'cu', 'gp', 'gu', 'gy', 'gz', 'kz', 'ht', 'kr', 'nl', 'an', 'hm', 'me', 'hn', 'hk', 'ki', 'dj', 'kg', 'gn', 'gw', 'ca', 'gh', 'ga', 'kh', 'cz', 'zw', 'cm', 'qa', 'ky', 'km', 'ci', 'kw', 'cc', 'hr', 'ke', 'ck', 'lv', 'ls', 'la', 'lb', 'lt', 'lr', 'ly', 'li', 're', 'lu', 'rw', 'ro', 'mg', 'im', 'mv', 'mt', 'mw', 'my', 'ml', 'mk', 'mh', 'mq', 'yt', 'mu', 'mr', 'us', 'um', 'as', 'vi', 'mn', 'ms', 'bd', 'pe', 'fm', 'mm', 'md', 'ma', 'mc', 'mz', 'mx', 'mo', 'nr', 'np', 'ni', 'ne', 'ng', 'nu', 'no', 'nf', 'na', 'za', 'aq', 'gs', 'ss', 'eu', 'pw', 'pn', 'pt', 'jp', 'se', 'ch', 'sv', 'ws', 'yu', 'sl', 'sn', 'cy', 'sc', 'sa', 'cx', 'st', 'sh', 'kn', 'lc', 'sm', 'pm', 'vc', 'lk', 'sk', 'si', 'sj', 'sz', 'sd', 'sr', 'sb', 'so', 'tj', 'tw', 'th', 'tz', 'to', 'tc', 'tt', 'tn', 'tv', 'tr', 'tm', 'tk', 'wf', 'vu', 'gt', 've', 'bn', 'ug', 'ua', 'uy', 'uz', 'es', 'eh', 'gr', 'hk', 'sg', 'nc', 'nz', 'hu', 'sy', 'jm', 'am', 'ac', 'ye', 'iq', 'ir', 'il', 'it', 'in', 'id', 'uk', 'vg', 'io', 'jo', 'vn', 'zm', 'je', 'td', 'gi', 'cl', 'cf', 'cn']
    if son in country_son :
        return 'country_son' 
    elif son in ['com', 'org', 'net', 'int', 'edu', 'gov', 'top', 'shop', 'site']:
        return son

    return 'Rare'

def get_son_domain_number(domain:str):
    son = son_domain(domain)
    return son_domain_list.index(son) / (len(son_domain_list)-1)

collect = []

if __name__ == "__main__":
    collect = []
    start = False
    with open(domain_file, 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            collect.append(row)
            # print(row)

    i = 0
    feature_names = [ 'domains', 'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth','Redirection', 
                      'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic', 
                      'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards', 
                      'char_number', 'char_word', 'char_symbol', 'son_domain',
                      'Label']
    
    f = open(output_feature, 'w', newline='')
    writer = csv.DictWriter(f, fieldnames=feature_names)
    writer.writeheader()
    
    for row in collect:
        # i+=1
        # if(i % 10 == 0):
        #     f.close()
        #     f = open(output_feature, 'a', newline='')
        #     writer = csv.DictWriter(f, fieldnames=feature_names)
        # print( row['Domain'])
        features = row
        features['son_domain'] = get_son_domain_number(row['domains'])
        features['URL_Depth'] = row['domains'].count('.') / 15
        # if depth < features['URL_Depth']:
        #     depth = features['URL_Depth']
        # print(features)
        writer.writerow(features)

    f.close()

# print("row['domains'].count('.'): ", depth)
