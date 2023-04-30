import json
from linkedin_api import Linkedin
from bs4 import BeautifulSoup
import textwrap

if __name__ == '__main__':
    #
    # file = json.load(open('/Users/sulimansharif/projects/global-chem/test.json', 'r'))
    #
    # soup = BeautifulSoup(open('/Users/sulimansharif/projects/global-chem/linkedin.html', 'r') , 'html.parser')
    #
    # for code in soup.find_all('code'):
    #
    #     try:
    #
    #         text = json.loads(code.text)
    #         for row in text['included']:
    #             if '*profile' in row:
    #                 print(row['*profile'].split(':')[-1])
    #         # print (text['included'][0].keys())
    #         # if 'urn:li:collectionResponse' not in text:
    #         #     print (text['data'])
    #     except:
    #         continue

    # profiles = file['included']
    #
    # for profile in profiles[1:]:
    #     try:
    #       print (profile['profileUrn'].split(':')[-1])
    #     except:
    #       continue

    api = Linkedin('sharifsuliman1@gmail.com', 'Makubex0@', authenticate=True, debug=True)

    profile = api.get_profile('jc-pacheco')
    urn_id = profile['entityUrn'].split(':')[-1]

    company = api.search_people(connection_of=urn_id)

    recepients = []
    first_names = []

    for people in company:
        recepients.append(people['urn_id'])
        first_names.append(people['name'].split(' ')[0])

    for i, recepient in enumerate(recepients):

        message = ('''\
          Hi %s,

          My name is Sul and I am author of Global-Chem. An Open Source Government Knowledge graph of Common Chemical Names to 1-D Molecule.

          I recorded the chemicals for all 425 ingredients to Cannabis Sativa as a template chemical list. I think it would be useful to map the compositions of chemicals to their phylogeny for characterization of different strains.

          Would love to connect
          ''' % first_names[i])

        api.send_message(
            textwrap.dedent(message),
            recipients=[recepient]
        )
