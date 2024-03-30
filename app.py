import streamlit as st
from langchain_openai import ChatOpenAI
import json
import requests
import os

url = 'https://fdqmwzn8q6.execute-api.us-east-1.amazonaws.com/dev'

st.title("Avaliando o projeto de Leads")
api_key = os.getenv('API_KEY')
llm = ChatOpenAI(temperature = 0.3, api_key = api_key, model = "gpt-4-1106-preview")


# Recebendo as informações do usuário
sector = st.text_input('Setor:')
size = st.text_input('Tamanho:')
local = st.text_input('Local:')
challenges = st.text_area('Desafios:')
goals = st.text_area('Metas:')
decision_processing = st.text_area('Processamento de Decisões:')
technologies = st.text_area('Tecnologias:')
total_leads = st.text_input('Total de Leads:')
new_leads = st.text_input('Novos Leads:')

# Botão "Enviar"
if st.button('Enviar dados para a Inteligência Artificial'):
    input_user = f"""
    - setor: {sector}
    - tamanho: {size}
    - local: {local}
    - desafios: {challenges}
    - objetivos: {goals}
    - processo de decisão: {decision_processing}
    - tecnologias utilizadas: {technologies}
    - quantidade de leads totais: {total_leads}
    - quantidade de leads novos por mês: {new_leads}
    """


    query = f"""
O tipo de lead que é temperatura 10 tem o seguinte perfil:
- setor: Crédito Consignado
- tamanho: Média empresa com 100-200 funcionários
- local: Capitais e grandes cidades brasileiras
- desafios: Dificuldade em identificar clientes com alta propensão a contratar créditos adicionais sem aumentar os riscos de inadimplência
- objetivos: Aumentar o volume de contratações de crédito consignado mantendo a qualidade da carteira de clientes
- processo de decisão: Comitê de direção financeira e comercial
- tecnologias utilizadas: CRM integrado com análise de crédito
- quantidade de leads totais: 100 mil
- quantidade de leads novos por mês: 10 mil


O tipo de lead A Imobiliária Inovadora tem temperatura 8 e tem o perfil:
- setor: Mercado Imobiliário
- tamanho: Grande empresa, mais de 500 funcionários
- local: Nacional, com escritórios em todas as regiões do Brasil
- desafios: Encontrar compradores potenciais em um mercado competitivo, com especial atenção para novos lançamentos
- objetivos: Acelerar as vendas de imóveis e aumentar a eficiência de seus corretores
- processo de decisão: Decisões tomadas por uma equipe multidisciplinar incluindo marketing, vendas e análise de mercado
- tecnologias utilizadas: Plataformas de automação de marketing e análise de mercado
- quantidade de leads totais: 5 mil
- quantidade de leads novos por mês: 500

O tipo de lead O Consórcio Ágil tem temperatura 7 e tem o perfil:
- setor: Consórcios (Veículos, Motos e Imobiliário)
- tamanho: Pequena a média empresa, 50-150 funcionários
- local: Atuação regional, foco em cidades médias
- desafios: Diferenciar-se em um mercado saturado e alcançar potenciais consorciados em nichos específicos
- objetivos: Aumentar a adesão aos consórcios e melhorar o lifetime value dos clientes
- processo de decisão: Principalmente decisões rápidas, orientadas pelo dono ou pequeno comitê
- tecnologias utilizadas: CRM básico e ferramentas de e-mail marketing
- quantidade de leads totais: 8 mil
- quantidade de leads novos por mês: 800

O tipo de lead O Varejista Visionário tem temperatura 10 e tem o perfil:
- setor: Varejo (Focado em Eletrônicos e Tecnologia)
- tamanho: Grande rede com mais de 200 lojas 
- local: Presente em todo território nacional
- desafios: Personalizar o atendimento e as ofertas para diferentes perfis de consumidores
- objetivos: Maximizar vendas, especialmente em lançamentos de novos produtos e ofertas sazonais
- processo de decisão: Equipes de marketing, vendas e TI colaboram para definir estratégias
- tecnologias utilizadas: Sistemas avançados de CRM, analytics e plataformas de e-commerce
- quantidade de leads totais: 80 mil
- quantidade de leads novos por mês: 5000

O tipo de lead O Gestor de CRM Estratégico tem temperatura 2 e tem o perfil:
- setor: Serviços B2B, com foco em soluções de CRM
- tamanho: Empresa de tecnologia de médio porte, 200-300 funcionários
- local: Atuação principal em centros urbanos com forte presença empresarial
- desafios: Expandir sua base de clientes B2B em setores competitivos
- objetivos: Fortalecer o posicionamento no mercado como líder em soluções de CRM que oferecem alto ROI para clientes empresariais
- processo de decisão: Decisões são frequentemente baseadas em dados, com influência direta dos líderes de tecnologia (CTOs) e marketing (CMOs)
- tecnologias utilizadas: Utilizadas: Utilizam as mais recentes inovações em software de CRM, análise de dados e inteligência artificial para fornecer soluções personalizadas
- quantidade de leads totais: 15 mil
- quantidade de leads novos por mês: 150

O tipo de lead O Produtor de Infoprodutos de Alto Impacto tem temperatura 8 e tem o perfil:
- setor: Infoprodutos (Cursos Online e E-books)
- tamanho: Pequena empresa, equipe enxuta focada em conteúdo de alta qualidade
- local: Operação totalmente digital, sem restrição geográfica
- desafios: Aumentar a base de clientes em um mercado saturado, melhorar a conversão em lançamentos e funis de vendas
- objetivos: Escalar vendas de cursos e e-books, construir uma marca reconhecida por conteúdo de valor
- processo de decisão: Decisões rápidas e centradas no fundador, com feedback de uma comunidade engajada
- tecnologias utilizadas: Plataformas de afiliados, ferramentas de automação de marketing e análise de tráfego
- quantidade de leads totais: 90 mil
- quantidade de leads novos por mês: 5000

O tipo de lead O Varejista Expansivo tem temperatura 4 e tem o perfil:
- setor: Varejo (Casa e Decoração)
- tamanho: Grande empresa com diversas filiais nacionais
- local:Presença em todo o Brasil, com lojas físicas e forte presença online
- desafios: Manter a relevância em meio à concorrência online, personalizar a experiência de compra para diversos perfis de clientes
- objetivos: Aumentar a fidelidade do cliente e maximizar as vendas multicanal
- processo de decisão: Equipes dedicadas de marketing e vendas, com decisões baseadas em dados e tendências de mercado
- tecnologias utilizadas:  Plataformas de e-commerce, CRM, e ferramentas de análise de dados
- quantidade de leads totais: 10 mil
- quantidade de leads novos por mês: 200

O tipo de lead A Plataforma de Infoprodutos Inovadora tem temperatura 9 e tem o perfil:
- setor: Plataformas de Venda de Infoprodutos
- tamanho: Média a grande empresa com uma ampla base de usuários e produtores de conteúdo
- local: Atuação global, com foco no mercado de língua portuguesa
- desafios: Destacar-se em um mercado competitivo, melhorar a taxa de sucesso dos produtores de conteúdo
- objetivos: Ser a plataforma preferida para produtores de infoprodutos e afiliados, otimizar o matchmaking entre conteúdo e consumidor
- processo de decisão: Estratégias definidas por dados, com equipes multidisciplinares incluindo produto, marketing e tecnologia
- tecnologias utilizadas: Analytics avançado, inteligência artificial para recomendações personalizadas, automação de marketing
- quantidade de leads totais: 100 mil
- quantidade de leads novos por mês: 10 mil

O tipo de lead O Gigante Tecnológico tem temperatura 1 e tem o perfil:
- setor: Tecnologia e Eletrônicos
- tamanho: Corporação internacional com milhares de empregados
- local: Presença global, com sede nos EUA e operações em diversos países
- desafios: Manter inovação constante, gerenciar uma cadeia de suprimentos complexa, e personalizar a experiência do usuário em escala global
- objetivos: Liderar o mercado com produtos inovadores, maximizar a eficiência operacional, e fortalecer a lealdade do cliente
- processo de decisão: Decisões estratégicas tomadas em alto nível, com implementação descentralizada
- tecnologias utilizadas: Big data, inteligência artificial, sistemas de gerenciamento de relacionamento com o cliente (CRM) de última geração
- quantidade de leads totais: 6 mil
- quantidade de leads novos por mês: 150

O tipo de lead A Startup de E-commerce Visionária tem temperatura 9 e tem o perfil:
- setor: E-commerce de Moda Sustentável
- tamanho: Startup em crescimento, com 20-50 funcionários
- local: Principalmente online, com sede em São Paulo e atuação em todo o Brasil
- desafios: Construir uma base de clientes fiéis em um nicho de mercado competitivo, garantir a sustentabilidade da cadeia de suprimentos
- objetivos: Tornar-se líder no segmento de moda sustentável, criar uma experiência de compra online excepcional
- processo de decisão: Ágil e centrado no cliente, com decisões tomadas por uma equipe jovem e dinâmica liderada pelo CEO e pelo CMO
- tecnologias utilizadas: Plataformas de e-commerce, ferramentas de SEO, marketing de conteúdo, e análise de dados para personalização
- quantidade de leads totais: 50 mil
- quantidade de leads novos por mês: 5000

Com base nesses perfils classifique a temperatura do seguinte perfil:

{input_user}

responda apenas o numero da temperatura.


"""

    answer = llm.invoke(query)

    # Exibindo as informações concatenadas
    st.write('Resposta do modelo:')
    st.write("A temperatura deste perfil é: ", answer.content)

    data = {
                'query': input_user,
                'predicted': answer.content
            }
        
    payload = json.dumps(data, ensure_ascii=False).encode('utf8')

    headers = {
            'Content-Type': 'application/json'
                    }
        
    response = requests.post(url, headers=headers, data=payload)

