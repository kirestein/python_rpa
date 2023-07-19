import brazilcep as bc


def get_cep(cep_input=input('Enter a valid cep (format: xxxxx-xxx): ')):
    number = input('Enter the number of your address: ')
    have_complement = input('Have your address a complement (s/n): ').lower()
    if have_complement.startswith('s'):
        comp = input('Enter the complement: ')
    else:
        comp = '-'

    datas = [bc.get_address_from_cep(cep_input), number, comp]
    return datas


# address = {
#     'CEP': address_data['cep'],
#     'street': address_data['street'],
#     'number': number,
#     'comp': comp,
#     'bairro': address_data['district'],
#     'city': address_data['city'],
#     'state': address_data['uf']
# }
# [print(key, value) for key, value in address.items()]

# cep_input = input('Enter a valid cep (format: xxxxx-xxx): ')
# get_address(cep_input)
