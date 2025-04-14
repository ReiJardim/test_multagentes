# crew.py
# Define a Crew para orquestrar o processo de criação de um novo sistema CrewAI
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


# Importar datetime para timestamp opcional no output
from datetime import datetime
tempo = datetime.now().strftime('%Y%m%d_%H%M%S')


@CrewBase
class ConstrutorCrewAI():
    """
    Crew responsável por executar o processo de desenvolvimento
    de um novo sistema multi-agente CrewAI, desde a concepção
    até a criação dos arquivos de configuração e script.
    """
    # Define os arquivos de configuração para agentes e tarefas
    # Certifique-se de que estes arquivos estejam na pasta 'config'
    # relativa à localização de crew.py, ou ajuste o caminho.
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # == Agentes da Crew de Desenvolvimento ==

    @agent
    def arquiteto_solucoes(self) -> Agent:
        """Agente responsável pela definição conceitual do sistema alvo."""
        return Agent(
            config=self.agents_config['arquiteto_solucoes'],
            verbose=True
        )

    @agent
    def designer_agentes(self) -> Agent:
        """Agente responsável por projetar os agentes do sistema alvo."""
        return Agent(
            config=self.agents_config['designer_agentes'],
            verbose=True
        )

    @agent
    def designer_tarefas(self) -> Agent:
        """Agente responsável por projetar as tarefas do sistema alvo."""
        return Agent(
            config=self.agents_config['designer_tarefas'],
            verbose=True
        )

    @agent
    def engenheiro_configuracao_yaml(self) -> Agent:
        """Agente responsável pela criação dos arquivos YAML."""
        return Agent(
            config=self.agents_config['engenheiro_configuracao_yaml'],
            verbose=True
        )

    @agent
    def desenvolvedor_orquestrador_crewai(self) -> Agent:
        """Agente responsável pela definição do fluxo e criação do script .py."""
        return Agent(
            config=self.agents_config['desenvolvedor_orquestrador_crewai'],
            verbose=True
        )

    # == Tarefas da Crew de Desenvolvimento ==
    # O @task decorator com config automaticamente associa o agente
    # definido no arquivo tasks.yaml correspondente.
    # Para processos sequenciais, as dependências são geralmente implícitas.
    # Se um fluxo mais complexo for necessário, use o argumento 'context'.
    # Ex: context=[self.nome_da_tarefa_anterior_task()]

    @task
    def definicao_conceito_sistema_task(self) -> Task:
        """Tarefa para definir o conceito do sistema alvo."""
        return Task(
            config=self.tasks_config['definicao_conceito_sistema'],
            # Contexto não é estritamente necessário aqui se o processo for sequencial
        )

    @task
    def design_agentes_sistema_alvo_task(self) -> Task:
        """Tarefa para projetar os agentes do sistema alvo."""
        return Task(
            config=self.tasks_config['design_agentes_sistema_alvo'],
            # Depende implicitamente do conceito definido na tarefa anterior
        )

    @task
    def design_tarefas_sistema_alvo_task(self) -> Task:
        """Tarefa para projetar as tarefas do sistema alvo."""
        return Task(
            config=self.tasks_config['design_tarefas_sistema_alvo'],
            # Depende implicitamente do conceito e do design dos agentes
            context=[self.definicao_conceito_sistema_task()]
        )

    @task
    def criacao_arquivo_agents_yaml_task(self) -> Task:
        """Tarefa para criar o arquivo agents.yaml."""
        return Task(
            config=self.tasks_config['criacao_arquivo_agents_yaml'],
            # Depende implicitamente do design dos agentes
            # Opcional: Definir arquivo de saída se a tarefa gerar um arquivo físico diretamente
            output_file=f"output/agents_{tempo}.yaml",
            context=[self.design_agentes_sistema_alvo_task()]
        )

    @task
    def criacao_arquivo_tasks_yaml_task(self) -> Task:
        """Tarefa para criar o arquivo tasks.yaml."""
        return Task(
            config=self.tasks_config['criacao_arquivo_tasks_yaml'],
            # Depende implicitamente do design das tarefas e da criação do agents.yaml
            # Opcional: Definir arquivo de saída
            output_file=f"output/tasks_{tempo}.yaml",
            context=[self.design_tarefas_sistema_alvo_task()]
        )

    @task
    def definicao_fluxo_orquestracao_task(self) -> Task:
        """Tarefa para definir o fluxo de orquestração."""
        return Task(
            config=self.tasks_config['definicao_fluxo_orquestracao'],
            # Depende implicitamente da definição das tarefas no tasks.yaml
            context=[self.criacao_arquivo_agents_yaml_task(
            ), self.criacao_arquivo_tasks_yaml_task()]
        )

    @task
    def implementacao_script_crew_py_task(self) -> Task:
        """Tarefa final para criar o arquivo crew.py do sistema alvo."""
        return Task(
            config=self.tasks_config['implementacao_script_crew_py'],
            # Depende implicitamente da criação dos YAMLs e da definição do fluxo
            # Define um arquivo de saída para o script python gerado
            context=[self.definicao_conceito_sistema_task(), self.design_agentes_sistema_alvo_task(), self.design_tarefas_sistema_alvo_task(
            ), self.criacao_arquivo_agents_yaml_task(), self.criacao_arquivo_tasks_yaml_task(), self.definicao_fluxo_orquestracao_task(),],
            output_file=f"output/crew{tempo}.py"
        )

    # == Definição da Crew ==
    @crew
    def crew(self) -> Crew:
        """Cria e configura a Crew ConstrutorCrewAI."""
        return Crew(
            agents=self.agents,  # Lista de agentes instanciados pelos decorators @agent
            tasks=self.tasks,    # Lista de tarefas instanciadas pelos decorators @task
            process=Process.sequential,  # O processo de desenvolvimento é tipicamente sequencial
            # Nível de verbosidade: 1 (padrão) ou 2 (mais detalhes)
            verbose=True
            # memory=True # Opcional: Habilitar memória entre tarefas
            # cache=True # Opcional: Habilitar cache para resultados de tarefas
        )

# Este arquivo define a classe da Crew.
# Para executá-la, você normalmente teria um arquivo 'main.py' que importa
# esta classe e chama o método kickoff().
#
# Exemplo (em main.py):
# from crew_creator_project.crew import ConstrutorCrewAI # Ajuste o import path
#
# if __name__ == "__main__":
#     print("## Iniciando a Crew de Construção de CrewAI...")
#     crew_construtora = ConstrutorCrewAI()
#     resultado = crew_construtora.crew().kickoff()
#
#     print("\n\n########################")
#     print("## Processo de Construção Concluído!")
#     print("## Resultado Final:")
#     print(resultado)
#     print("########################")
#     print(f"Verifique a pasta 'output/' para os arquivos gerados (se aplicável).")
