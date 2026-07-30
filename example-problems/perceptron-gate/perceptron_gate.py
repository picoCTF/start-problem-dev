#!/usr/bin/env python3
import sys, os, random

BANNER = """Welcome to Perceptron Gate.
Commands:
  QUERY a b        # a,b in {0,1}, up to 8 queries
  SUBMIT w1 w2 b   # floats or ints; must exactly match my truth table on all 4 inputs
"""

MAX_QUERIES = 8

def perceptron(w1, w2, b, x1, x2):
    return 1 if (w1 * x1 + w2 * x2 + b) >= 0 else 0

def choose_gate(rng):
    # Small, clean gates with integer params and exact thresholds
    gates = {
        "AND":  (1.0,  1.0, -1.5),
        "OR":   (1.0,  1.0, -0.5),
        "NAND": (-1.0, -1.0,  1.5),
        "NOR":  (-1.0, -1.0,  0.5),
    }
    name = rng.choice(list(gates.keys()))
    w1, w2, b = gates[name]
    return (w1, w2, b)

def read_flag():
    try:
        with open("flag.txt") as f:
            return f.read().strip()
    except Exception:
        return "academy{flag_missing_contact_admin_00000000}"

def main():
    rng = random.Random(os.urandom(16))
    w1, w2, b = choose_gate(rng)

    queries = 0
    sys.stdout.write(BANNER + "\n")
    sys.stdout.flush()

    while True:
        sys.stdout.write("> ")
        sys.stdout.flush()
        line = sys.stdin.readline()
        if not line:
            break
        parts = line.strip().split()
        if not parts:
            continue
        cmd = parts[0].upper()

        if cmd == "QUERY" and len(parts) == 3:
            if queries >= MAX_QUERIES:
                print("No queries left.")
                continue
            try:
                a = int(parts[1]); bb = int(parts[2])
                if a not in (0,1) or bb not in (0,1):
                    raise ValueError
            except Exception:
                print("Use: QUERY a b  with a,b in {0,1}")
                continue
            y = perceptron(w1, w2, b, a, bb)
            print(y)
            queries += 1

        elif cmd == "SUBMIT" and len(parts) == 4:
            try:
                sw1 = float(parts[1]); sw2 = float(parts[2]); sb = float(parts[3])
            except Exception:
                print("Bad weights.")
                continue
            ok = True
            for a in (0,1):
                for bb in (0,1):
                    y_true = perceptron(w1, w2, b, a, bb)
                    y_pred = perceptron(sw1, sw2, sb, a, bb)
                    if y_true != y_pred:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                print(read_flag())
                break
            else:
                print("Model mismatch.")

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()

