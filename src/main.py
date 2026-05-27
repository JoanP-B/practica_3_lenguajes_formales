import sys
import os

# Importaciones apuntando a las carpetas
from .P1.lexer import Lexer
from .P1.parser_rules import Parser
from .P2.interpreter import Interpreter, Environment
from .P3.analyzer import StaticAnalyzer

def parse_state_file(state_content):
    """Parsea el formato del State inicial definido en la especificación."""
    variables = {}
    active_facts = set()
    
    for line in state_content.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        if '=' in line:
            parts = line.split('=')
            var_name = parts[0].strip()
            var_val = int(parts[1].strip())
            variables[var_name] = var_val
        else:
            active_facts.add(line)
            
    return Environment(variables, active_facts)

def execute_pipeline(rules_text, state_text):
    # 1. Lexer & Parser
    lexer = Lexer(rules_text)
    parser = Parser(lexer.tokens)
    ast = parser.parse_program()
    
    # 2. Entorno e Intérprete
    env = parse_state_file(state_text)
    initial_env_copy = Environment(dict(env.variables), set(env.active_facts))
    
    interpreter = Interpreter(ast, env)
    final_facts = interpreter.evaluate()
    
    # 3. Análisis Estático
    analyzer = StaticAnalyzer(ast)
    analysis_msgs = analyzer.analyze(initial_env_copy)
    
    # --- Formateo de Salida Canónica ---
    output_lines = []
    
    # Quitar los hechos que ya venían en el estado inicial si la especificación pide solo los *activados*
    # Nota: El PDF muestra que si 'a' entra y activa 'b', la salida es b,c,d,e (no incluye 'a')
    activated_facts = final_facts - initial_env_copy.active_facts
    
    if activated_facts:
        output_lines.extend(sorted(list(activated_facts)))
    else:
        output_lines.append("(no output)")
        
    if analysis_msgs:
        output_lines.extend(analysis_msgs)
        
    return "\n".join(output_lines)

if __name__ == "__main__":
    # Permite ejecución manual rápida pasando archivos por consola
    if len(sys.argv) < 3:
        print("Uso: python -m src.main <archivo_reglas.txt> <archivo_estado.txt>")
        sys.exit(1)
        
    with open(sys.argv[1], 'r') as f:
        r_text = f.read()
    with open(sys.argv[2], 'r') as f:
        s_text = f.read()
        
    print(execute_pipeline(r_text, s_text))