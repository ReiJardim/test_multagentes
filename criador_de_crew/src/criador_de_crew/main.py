#!/usr/bin/env python
from dotenv import load_dotenv, find_dotenv
import sys
import warnings

from datetime import datetime

from crew import ConstrutorCrewAI

_ = load_dotenv(find_dotenv())


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


SISTEMA = '''Sistema para criação de  de crew que desenvolve conteudo para um Plano de Gestão de Resíduos (PGRS). Primeiro levanta faz uma pesquisa de conteudos relevantes, levanta tópicos importantes dentro desse conteudo, desenvolve um escopo, redige a documentação do PGRS e revisa '''


def run():
    """
    Run the crew.
    """
    inputs = {
        'definicao_do_sistema_alvo': SISTEMA,

    }

    try:
        ConstrutorCrewAI().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        ConstrutorCrewAI().crew().train(n_iterations=int(
            sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ConstrutorCrewAI().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        ConstrutorCrewAI().crew().test(n_iterations=int(
            sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    run()
