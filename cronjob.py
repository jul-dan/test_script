import argparse
import random
import sys

def parse_failure_rate(value: str) -> float:
    value = value.strip().lower()
    if value == "never":
        return 0.0
    if value == "always":
        return 1.0
    if value.endswith("%"):
        return float(value[:-1]) / 100.0
    raise argparse.ArgumentTypeError(
        f"Valeur invalide '{value}'. Utilisez 'never', 'always', ou un pourcentage comme '50%'."
    )

parser = argparse.ArgumentParser(description="Script cronjob avec taux d'échec configurable.")
parser.add_argument(
    "--failure-rate",
    type=parse_failure_rate,
    default=0.0,
    metavar="RATE",
    help="Fréquence d'échec : 'never', 'always', ou un pourcentage (ex: '50%%'). Défaut: never.",
)
args = parser.parse_args()

if random.random() < args.failure_rate:
    print("Hello World - CRONJOB - FAILED", flush=True)
    sys.exit(1)

print("Hello World - CRONJOB", flush=True)
