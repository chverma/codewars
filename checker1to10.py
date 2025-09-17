import sys
import subprocess

# Casos de prueba: entrada y salida esperada para ejercicios 1 a 10
cases = {
    1: {"input": "10\n4\n1335\n", "output": "1321\n"},
    2: {"input": "1\n5\n", "output": "1\n2\nFizz\n4\nBuzz\n"},
    3: {"input": "0,0,1\n", "output": "-0.460408,-0.749510,2.917140\n"},
    4: {"input": "356\n", "output": "1.74 V\n"},
    5: {"input": "11001\n10110\n", "output": "01111\n"},
    6: {"input": "6\n1\n3\n4\n12\n10\n9\n", "output": "True\n"},
    7: {"input": "3\n6\n10\n7\n", "output": "YES\nYES\nNO\n"},
    8: {"input": "14159\n", "output": "1\n"},
    9: {"input": "--xo--x--ox--\n--xx--x--xx--\n--oo--o--oo--\n--xx--x--ox--\n--xx--x--ox--\n#\n", "output": "1 4\n"},
    10: {"input": "5\n15\n", "output": "2078.93\n"}
}

def run_and_check(exercise_num, script_path):
    if exercise_num not in cases:
        print(f"No hay caso de prueba para el ejercicio {exercise_num}.")
        return

    case = cases[exercise_num]
    try:
        # Ejecuta el script externo con las entradas del caso
        process = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=case["input"], timeout=10)

        # Compara resultados
        if stdout == case["output"]:
            print(f"Ejercicio {exercise_num} realizado.")
        else:
            print(f"Ejercicio {exercise_num} no realizado.")
            print(f"Salida esperada:\n{case['output']}")
            print(f"Salida recibida:\n{stdout}")
            if stderr:
                print(f"Errores:\n{stderr}")

    except subprocess.TimeoutExpired:
        print(f"El script del ejercicio {exercise_num} tardó demasiado y fue terminado.")
    except Exception as e:
        print(f"Error al ejecutar el script: {e}")

def main():
    if len(sys.argv) != 3:
        print("Uso: python check_script.py <numero_ejercicio> <ruta_script.py>")
        sys.exit(1)
    try:
        exercise_num = int(sys.argv[1])
    except ValueError:
        print("El número de ejercicio debe ser un entero.")
        sys.exit(1)
    script_path = sys.argv[2]
    run_and_check(exercise_num, script_path)

if __name__ == '__main__':
    main()
