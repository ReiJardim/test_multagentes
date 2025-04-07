from crewai import Crew, Process, Agent, Task
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


# Define your agents
desenvolvedor_de_ideais = Agent(
    role='Criador de Ideias Criativas para Blog Posts',
    goal='Gerar ideias originais e relevantes para posts de blog dentro de um tema específico',
    backstory='Você é um criador criativo, sempre antenado nas últimas tendências e com uma habilidade impressionante para transformar conceitos em ideias inovadoras. Sua curiosidade e energia o ajudam a criar sugestões únicas que atraem o público-alvo de forma eficaz.',
    verbose=True
)

planejador_de_conteudo = Agent(
    role='Estrategista de Conteúdo para Blogs',
    goal='Planejar e estruturar o conteúdo de maneira eficaz, com base no briefing fornecido',
    backstory='Você é um estrategista detalhista, apaixonado por alinhar objetivos e dados com a criação de conteúdo. Você adora criar planos bem estruturados que orientam os redatores para alcançar os melhores resultados. Seu foco está sempre em garantir que o conteúdo atenda às expectativas do público e aos objetivos de marketing.',
    verbose=True
)

escritor_do_post = Agent(
    role='Redator Criativo de Blog Posts',
    goal='Escrever posts de blog envolventes e de alta qualidade, seguindo o briefing e as diretrizes definidas',
    backstory='Você é um escritor versátil, capaz de adaptar seu estilo de escrita ao tom e ao formato desejado. Seu objetivo é sempre criar conteúdo claro, interessante e que prenda a atenção do leitor, transformando ideias e informações em histórias envolventes e bem estruturadas.',
    verbose=True)

revisor_do_post = Agent(
    role='Revisor de Conteúdo de Blog Posts',
    goal='Garantir que o post esteja livre de erros e pronto para ser publicado',
    backstory='Você é um revisor minucioso e atento aos detalhes. Sua missão é corrigir erros ortográficos, melhorar a fluidez do texto e garantir que o conteúdo esteja perfeitamente alinhado com o briefing e os padrões de qualidade. Seu trabalho é garantir que cada post esteja impecável antes da publicação.',
    verbose=True)


# Define your tasks
cria_ideias = Task(
    description='Crie uma lista com 10 ideias diferentes para posts de blog sobre o tema: {tema}. As ideias devem ser criativas, relevantes e diversificadas em formato, com foco em engajar o público-alvo.',
    agent=desenvolvedor_de_ideais,
    expected_output='Uma lista com 10 ideias de posts, cada uma com um título criativo e um breve resumo do que o conteúdo abordará.'
)

seleciona_ideias = Task(
    description='Selecione a melhor ideia da lista gerada, justificando sua escolha com base na relevância e no alinhamento com os objetivos do blog.',
    agent=desenvolvedor_de_ideais,
    expected_output='A escolha de uma ideia com uma justificativa clara e concisa sobre sua relevância e alinhamento com os objetivos do conteúdo.'
)

planeja_conteudo = Task(
    description='Crie um briefing detalhado para o post de blog, incluindo informações como objetivo, público-alvo, tom de voz, palavras-chave e formato.',
    agent=planejador_de_conteudo,
    expected_output='Um briefing estruturado, abordando todos os pontos importantes para guiar a criação do conteúdo.'
)

escreve_post = Task(
    description='Escreva o conteúdo completo do post de blog, seguindo as diretrizes do briefing e a ideia selecionada. Certifique-se de que o post seja envolvente, bem estruturado e adequado ao público-alvo.',
    agent=escritor_do_post,
    expected_output='Um post de blog com introdução, desenvolvimento e conclusão, que seja claro, interessante e alinhado com o briefing.'
)

revisa_post = Task(
    description='Revise o post de blog, corrigindo erros gramaticais e de pontuação, além de melhorar a fluidez do texto. Assegure que o post esteja alinhado com o tom e objetivo definidos no briefing.',
    agent=revisor_do_post,
    expected_output='O post revisado, sem erros gramaticais e com boa fluidez, pronto para ser publicado.'
)


blog_post_creation_crew = Crew(
    agents=[desenvolvedor_de_ideais, planejador_de_conteudo,
            escritor_do_post, revisor_do_post],
    tasks=[cria_ideias, seleciona_ideias,
           planeja_conteudo, escreve_post, revisa_post],
    process=Process.sequential
)


result = blog_post_creation_crew.kickoff(
    {'tema': 'Aplicações com inteligência artificial'})
print(result.raw)
