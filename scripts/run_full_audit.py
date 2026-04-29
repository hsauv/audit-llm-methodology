"""
Script d'orchestration d'un audit complet.

Usage:
    python scripts/run_full_audit.py --audit-name mon_audit --model claude-sonnet-4-6

Ce script enchaîne les 6 notebooks de l'audit, en passant le contexte de
l'un à l'autre via les fichiers YAML d'output.

Pré-requis :
- Les notebooks 01 à 06 doivent avoir été exécutés au moins une fois
- Les variables d'environnement ANTHROPIC_API_KEY ou OPENAI_API_KEY doivent
  être définies pour les appels réels
"""

import argparse
import sys
from pathlib import Path
import subprocess
import yaml
from datetime import datetime


def run_notebook(notebook_path: Path, output_dir: Path) -> bool:
    """
    Exécute un notebook et le sauvegarde dans le dossier output.
    """
    print(f"\n{'='*60}")
    print(f"  Exécution : {notebook_path.name}")
    print(f"{'='*60}\n")
    
    result = subprocess.run(
        [
            "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute", str(notebook_path),
            "--output-dir", str(output_dir),
            "--output", f"{notebook_path.stem}_executed.ipynb"
        ],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(f"✅ {notebook_path.name} exécuté avec succès")
        return True
    else:
        print(f"❌ Erreur sur {notebook_path.name}")
        print(result.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Orchestration d'un audit IA complet")
    parser.add_argument("--audit-name", required=True, help="Nom de l'audit (sans espaces)")
    parser.add_argument("--model", default="claude-sonnet-4-6", help="Modèle à auditer")
    parser.add_argument("--steps", default="all", help="Étapes à exécuter (1,2,3 ou 'all')")
    args = parser.parse_args()
    
    # Configuration
    base_dir = Path(__file__).parent.parent
    notebooks_dir = base_dir / "notebooks"
    output_dir = base_dir / f"output/{args.audit_name}"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Sélection des étapes
    all_notebooks = [
        notebooks_dir / "01_cadrage_systeme.ipynb",
        notebooks_dir / "02_analyse_donnees.ipynb",
        notebooks_dir / "03_fairness_metrics.ipynb",
        notebooks_dir / "04_redteaming_llm.ipynb",
        notebooks_dir / "05_robustesse_tests.ipynb",
        notebooks_dir / "06_synthese_remediation.ipynb",
    ]
    
    if args.steps == "all":
        steps_to_run = all_notebooks
    else:
        indices = [int(s) - 1 for s in args.steps.split(",")]
        steps_to_run = [all_notebooks[i] for i in indices]
    
    print(f"\n🚀 DÉMARRAGE AUDIT : {args.audit_name}")
    print(f"   Modèle : {args.model}")
    print(f"   Étapes : {len(steps_to_run)}")
    print(f"   Output : {output_dir}\n")
    
    # Exécution séquentielle
    start_time = datetime.now()
    success_count = 0
    
    for nb in steps_to_run:
        if run_notebook(nb, output_dir):
            success_count += 1
        else:
            print(f"\n⚠️  Arrêt prématuré suite à l'erreur sur {nb.name}")
            break
    
    duration = (datetime.now() - start_time).total_seconds() / 60
    
    print(f"\n{'='*60}")
    print(f"  AUDIT TERMINÉ")
    print(f"{'='*60}")
    print(f"  Étapes réussies : {success_count}/{len(steps_to_run)}")
    print(f"  Durée totale : {duration:.1f} minutes")
    print(f"  Outputs dans : {output_dir}")
    
    if success_count == len(steps_to_run):
        print(f"\n✅ Audit complet. Vous pouvez maintenant générer le rapport :")
        print(f"   python scripts/generate_report.py --audit-name {args.audit_name}")
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
