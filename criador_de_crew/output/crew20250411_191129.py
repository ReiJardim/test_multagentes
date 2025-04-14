
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import yaml


@CrewBase
class ProjetoTest():

    agents_config_path = 'config/agents.yaml'
    tasks_config_path = 'config/tasks.yaml'

    def load_yaml(self, path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)

    @agent
    def researcher(self) -> Agent:
        config = self.load_yaml(self.agents_config_path)[
            'pesquisador_automatizado']
        return Agent(
            config=config,
            verbose=True
        )

    @agent
    def content_analyst(self) -> Agent:
        config = self.load_yaml(self.agents_config_path)[
            'analista_de_conteudo']
        return Agent(
            config=config,
            verbose=True
        )

    @agent
    def scope_developer(self) -> Agent:
        config = self.load_yaml(self.agents_config_path)[
            'desenvolvedor_de_escopo']
        return Agent(
            config=config,
            verbose=True
        )

    @agent
    def documentation_writer(self) -> Agent:
        config = self.load_yaml(self.agents_config_path)[
            'redator_de_documentacao']
        return Agent(
            config=config,
            verbose=True
        )

    @agent
    def collaborative_reviewer(self) -> Agent:
        config = self.load_yaml(self.agents_config_path)[
            'revisor_colaborativo']
        return Agent(
            config=config,
            verbose=True
        )

    @agent
    def legal_checker(self) -> Agent:
        config = self.load_yaml(self.agents_config_path)['conformidade_legal']
        return Agent(
            config=config,
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        config = self.load_yaml(self.tasks_config_path)[
            'pesquisa_automatizada']
        return Task(
            config=config,
        )

    @task
    def content_analysis_task(self) -> Task:
        config = self.load_yaml(self.tasks_config_path)['analise_de_conteudo']
        return Task(
            config=config,
        )

    @task
    def scope_development_task(self) -> Task:
        config = self.load_yaml(self.tasks_config_path)[
            'desenvolvimento_de_escopo']
        return Task(
            config=config,
        )

    @task
    def documentation_generation_task(self) -> Task:
        config = self.load_yaml(self.tasks_config_path)[
            'geracao_de_documentacao']
        return Task(
            config=config,
        )

    @task
    def collaborative_review_task(self) -> Task:
        config = self.load_yaml(self.tasks_config_path)['revisao_colaborativa']
        return Task(
            config=config,
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
