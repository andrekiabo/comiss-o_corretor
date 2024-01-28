# calcular 5% e 4% do valor do imóvel
# Calcular 25% desses 5% para corretor e 75% para imobiliária
# Dividir o valor do corretor por 2.

valor_imovel = input('Digite o valor inteiro do imóvel sem pontos: ')

try:
    valor_imovel = float(valor_imovel)
    valor_imovel_format = '{:,.2f}'.format(valor_imovel).replace('.', 'x').replace(',', '.').replace('x', ',')
    print('')
    print(f'Valor do imóvel: R${valor_imovel_format}')
    print('')
#4% 
    porcentagem4 = (valor_imovel / 100) * 4
    porcentagem4_format = '{:,.2f}'.format(porcentagem4).replace('.', 'x').replace(',', '.').replace('x', ',')
    print(f'- 4% do valor do imóvel é: R${porcentagem4_format}')

    comissao_imobiliaria = porcentagem4 / 100 * 75
    comissao_imobiliaria_format = '{:,.2f}'.format(comissao_imobiliaria).replace('.', 'x').replace(',', '.').replace('x', ',')
    print(f'(75%) R${comissao_imobiliaria_format} - imobiliária')

    comissao_corretor = porcentagem4 / 100 * 25
    comissao_corretor_format = '{:,.2f}'.format(comissao_corretor).replace('.', 'x').replace(',', '.').replace('x', ',')
    print(f'(25%) R${comissao_corretor_format} - corretor')
    dividir_comissao_corretor = comissao_corretor / 2
    dividir_comissao_corretor_format = '{:,.2f}'.format(dividir_comissao_corretor).replace('.', 'x').replace(',', '.').replace('x', ',')
    print (f'Comissão dividida fica R${dividir_comissao_corretor_format} para cada.')

#5% 
    print('')
    porcentagem5 = (valor_imovel / 100) * 5
    porcentagem5_format2 = '{:,.2f}'.format(porcentagem5).replace('.', 'x').replace(',', '.').replace('x', ',')
    print(f'- 5% do valor do imóvel é: R${porcentagem5_format2}')

    comissao_imobiliaria2 = porcentagem5 / 100 * 75
    comissao_imobiliaria_format2 = '{:,.2f}'.format(comissao_imobiliaria2).replace('.', 'x').replace(',', '.').replace('x', ',')
    print(f'(75%) R${comissao_imobiliaria_format2} - imobiliária')

    comissao_corretor2 = porcentagem5 / 100 * 25
    comissao_corretor_format2 = '{:,.2f}'.format(comissao_corretor2).replace('.', 'x').replace(',', '.').replace('x', ',')
    print(f'(25%) R${comissao_corretor_format2} - corretor')
    dividir_comissao_corretor2 = comissao_corretor2 / 2
    dividir_comissao_corretor2_format = '{:,.2f}'.format(dividir_comissao_corretor2).replace('.', 'x').replace(',', '.').replace('x', ',')
    print (f'Comissão dividida fica R${dividir_comissao_corretor2_format} para cada.')

except:
    print('Digite somente números.')




