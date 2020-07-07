a = ['BOLSONARO ESTÁ COM COVID-19', "Presidente diz que coronavírus é como uma chuva: 'Vai atingir você'", 'Ministros fazem exames para Covid; ao menos 3 dão negativo', 'Moro, Doria e mais autoridades desejam melhoras a Bolsonaro', 'VALDO CRUZ: Videoconferência era forma mais segura de fazer anúncio', 'GLOBONEWS: veja repercussão do diagnóstico do presidente', 'Brasil passa de 66 mil mortes e tem mais de 1,6 milhão de casos', 'Pesquisa brasileira apresenta 1º remédio com chance de eliminar o HIV', '283 mil brasileiros perderam plano de saúde na pandemia', 'Petrobras aumenta preço da gasolina pela 8ª vez desde maio']
b = ['https://g1.globo.com/politica/noticia/2020/07/07/bolsonaro-diz-que-seu-exame-para-covid-19-deu-positivo.ghtml', 'https://g1.globo.com/politica/noticia/2020/07/07/bolsonaro-diz-que-exame-de-covid-19-deu-positivo-frases.ghtml', 'https://g1.globo.com/politica/noticia/2020/07/07/ministros-fazem-exames-apos-bolsonaro-testar-positivo-para-covid-19.ghtml', 'https://g1.globo.com/politica/noticia/2020/07/07/autoridades-e-politicos-desejam-melhoras-a-bolsonaro-apos-diagnostico-de-covid.ghtml', 'https://g1.globo.com/globonews/playlist/videos-comentaristas-analisam-resultado-do-exame-para-covid-19-do-presidente-jair-bolsonaro.ghtml#video-8680204-id', 'https://g1.globo.com/globonews/ao-vivo/globonews-ao-vivo.ghtml', 'https://g1.globo.com/bemestar/coronavirus/noticia/2020/07/07/casos-e-mortes-por-coronavirus-no-brasil-7-de-julho-segundo-consorcio-de-veiculos-de-imprensa.ghtml', 'https://g1.globo.com/bemestar/aids/noticia/2020/07/07/pesquisa-brasileira-apresenta-primeiro-medicamento-com-chance-de-eliminar-o-hiv.ghtml', 'https://g1.globo.com/economia/noticia/2020/07/07/com-pandemia-planos-de-saude-perdem-283-mil-clientes-em-2-meses.ghtml', 'https://g1.globo.com/economia/noticia/2020/07/07/petrobras-anuncia-alta-de-5-para-gasolina-nas-refinarias-a-partir-de-quarta-feira.ghtml']

def algo(a, b):
  c = zip(a, b)

  for i, j in c:
    i = i.replace("'", "")
    print(i)

algo(a, b)
