"""

Escolha um texto da internet, a partir dele faça um código que demostre as 5 palavras que aparecem com mais frequência nesse texto.


"""

from collections import Counter

texto = """A ciência de dados (em inglês: data science) é uma área interdisciplinar, que localiza-se em uma interface entre a estatística e a ciência da computação e utiliza o método científico;
processos, algoritmos e sistemas, para extrair conhecimento e tomar decisões a partir de dados dos diversos tipos, sendo eles ruidosos, nebulosos, estruturados ou não-estruturados. Sendo assim 
uma área voltada para o estudo e a análise organizada de dados científicos e mercadológicos, financeiros, sociais, geográficos, históricos, biológicos, psicológicos, dentre muitos outros. Visa, 
desse modo, a extração de conhecimento, detecção de padrões e/ou obtenção de insights para possíveis tomadas de decisão. Ciência de dados enquanto campo existe há 30 anos, porém ganhou mais destaque 
nos últimos anos devido a alguns fatores como o surgimento e a popularização de grandes bancos de dados e o desenvolvimento de áreas como machine learning. Cientistas de Dados podem trabalhar no setor 
privado, por exemplo, transformando grandes quantidades de dados brutos em insights de negócios, auxiliando empresas em tomadas de decisões para atingir melhores resultados[1] ou na academia e terceiro 
setor como pesquisadores quantitativos interdisciplinares.[2]
Há uma forte relação da área da ciência de dados com a inteligência artificial, uma vez que o principal profissional que lida com o desenvolvimento, manutenção e fiscalização de inteligências artificiais e 
machine learning é o cientistas de dados."""

palavras = texto.split()

Gabarito = Counter(palavras)

print(Gabarito.most_common(5))