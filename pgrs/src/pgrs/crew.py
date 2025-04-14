
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
import yaml
from crewai.project import CrewBase, agent, crew, task
from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv
import agentops
_ = load_dotenv()

agentops.init()


serper = SerperDevTool()
scrape = ScrapeWebsiteTool()
filewite = FileWriterTool()


@CrewBase
class ProjetoTest():

    agents_config_path = '/home/rei/ISC/arena/test_multagentes/pgrs/src/pgrs/config/agents.yaml'
    tasks_config_path = '/home/rei/ISC/arena/test_multagentes/pgrs/src/pgrs/config/tasks.yaml'

    def load_yaml(self, path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)

    @agent
    def pesquisador_automatizado(self) -> Agent:
        config = self.load_yaml(self.agents_config_path)[
            'pesquisador_automatizado']
        return Agent(
            config=config,
            tools=[serper],
            verbose=True
        )

    @agent
    def analista_de_conteudo(self) -> Agent:
        config = self.load_yaml(self.agents_config_path)[
            'analista_de_conteudo']
        return Agent(
            config=config,
            tools=[scrape],
            verbose=True
        )

    @agent
    def desenvolvedor_de_escopo(self) -> Agent:
        config = self.load_yaml(self.agents_config_path)[
            'desenvolvedor_de_escopo']
        return Agent(
            config=config,
            verbose=True
        )

    @agent
    def redator_de_documentacao(self) -> Agent:
        config = self.load_yaml(self.agents_config_path)[
            'redator_de_documentacao']
        return Agent(
            config=config,
            verbose=True
        )

    @agent
    def revisor(self) -> Agent:
        config = self.load_yaml(self.agents_config_path)[
            'revisor']
        return Agent(
            config=config,
            verbose=True
        )

    @agent
    def conformidade_legal(self) -> Agent:
        config = self.load_yaml(self.agents_config_path)['conformidade_legal']
        return Agent(
            config=config,
            verbose=True
        )

    @task
    def pesquisa_automatizada(self) -> Task:
        return Task(config=self.tasks_config['pesquisa_automatizada'],
                    )

    @task
    def analise_de_conteudo(self) -> Task:
        return Task(config=self.tasks_config['analise_de_conteudo'],
                    )

    @task
    def desenvolvimento_de_escopo(self) -> Task:
        return Task(config=self.tasks_config['desenvolvimento_de_escopo'],
                    )

    @task
    def geracao_de_documentacao(self) -> Task:
        return Task(config=self.tasks_config['geracao_de_documentacao'],
                    )

    @task
    def revisao_colaborativa(self) -> Task:
        return Task(config=self.tasks_config['revisao_colaborativa'],
                    tools=[filewite],
                    )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    def kickoff(self):
        results = self.crew.run()
        print("Resultados finais do PGRS:", results)


# ### Descrição da Implementação do `crew.py`

# 1. **Carregamento de Configurações:**
#    O script carrega as configurações dos arquivos YAML correspondentes aos agentes e tarefas utilizando a função `load_yaml`.

# 2. **Definição dos Agentes:**
#    Cada agente é definido com a respectiva configuração carregada, garantindo que cada um tenha os parâmetros adequados para suas funções.

# 3. **Definição das Tarefas:**
#    As tarefas são igualmente definidas e configuradas a partir das entradas no arquivo `tasks.yaml`.

# 4. **Instanciação da Crew:**
#    A crew é instanciada com todos os agentes e tarefas, organizando-se em um processo sequencial que garante que uma tarefa seja completada antes da próxima ser iniciada.

# 5. **Início da Execução:**
#    O método `kickoff` é implementado para iniciar o processo de execução e processar os resultados finais do PGRS, exibindo-os ao final da execução.

# ### Conclusão

# O código acima fornece uma orquestração completa para criar um Plano de Gestão de Resíduos Sólidos de forma automatizada, garantindo que todas as tarefas, desde a pesquisa até a revisão final, sejam realizadas de forma eficiente e em sequência lógica. Com isso, esperamos alcançar um PGRS robusto e que atenda a todas as exigências legais e práticas do setor.
