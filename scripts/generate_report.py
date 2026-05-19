"""
Générateur de rapport d'audit LLM.

Lit les résultats YAML produits par les notebooks (étapes 1-6),
fusionne les données et génère un rapport professionnel.

Usage:
    python scripts/generate_report.py --audit-name audit_demo_chatbot_rh --format md
    python scripts/generate_report.py --audit-name audit_demo_chatbot_rh --format pdf

Formats supportés :
- md  : Markdown (toujours généré)
- pdf : PDF via weasyprint (nécessite weasyprint installé)

Pré-requis :
- Les notebooks 01-06 doivent avoir été exécutés
- Les fichiers YAML de résultats doivent exister dans output/<audit-name>/
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime

import yaml
from jinja2 import Environment, FileSystemLoader


def load_results(output_dir: Path) -> dict:
    """Charge tous les fichiers YAML de résultats des étapes."""
    results = {}
    yaml_files = sorted(output_dir.glob("*_results.yaml"))

    for yf in yaml_files:
        step_key = yf.stem  # ex: "02_etape2_results"
        with open(yf, encoding="utf-8") as f:
            results[step_key] = yaml.safe_load(f)

    return results


def render_markdown(results: dict, audit_name: str, template_dir: Path) -> str:
    """Génère le rapport Markdown à partir des résultats et du template."""
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=False,
    )

    # Utiliser rapport_audit.md comme template si disponible
    template_path = template_dir / "rapport_audit.md"
    if template_path.exists():
        template = env.get_template("rapport_audit.md")
    else:
        # Template minimal de fallback
        template = env.from_string(_FALLBACK_TEMPLATE)

    # Préparer les variables du template
    context = {
        "audit_name": audit_name,
        "date": datetime.now().strftime("%d/%m/%Y"),
        "results": results,
    }

    # Extraire les scores par étape si disponibles
    for key, data in results.items():
        if data is None:
            continue
        if "fairness_score" in data:
            context["fairness_score"] = data["fairness_score"]
        if "redteam_score" in data:
            context["redteam_score"] = data["redteam_score"]
        if "global_score" in data:
            context["robustness_score"] = data["global_score"]
            context["robustness_grade"] = data.get("grade", "N/A")

    return template.render(**context)


def export_pdf(markdown_content: str, output_path: Path) -> None:
    """Convertit le Markdown en PDF via weasyprint."""
    try:
        import markdown as md_lib
        from weasyprint import HTML
    except ImportError:
        print("ERREUR : weasyprint et/ou markdown non installés.")
        print("  pip install weasyprint markdown")
        sys.exit(1)

    html_content = md_lib.markdown(
        markdown_content,
        extensions=["tables", "fenced_code", "toc"],
    )

    # Envelopper dans du HTML avec styles
    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <style>
        body {{ font-family: 'Helvetica Neue', Arial, sans-serif; margin: 2cm; line-height: 1.6; }}
        h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
        h2 {{ color: #34495e; margin-top: 1.5em; }}
        h3 {{ color: #7f8c8d; }}
        table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
        th, td {{ border: 1px solid #ddd; padding: 8px 12px; text-align: left; }}
        th {{ background-color: #3498db; color: white; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
        code {{ background: #f4f4f4; padding: 2px 6px; border-radius: 3px; }}
        pre {{ background: #f4f4f4; padding: 1em; border-radius: 5px; overflow-x: auto; }}
        .score-A {{ color: #27ae60; font-weight: bold; }}
        .score-B {{ color: #27ae60; }}
        .score-C {{ color: #f39c12; }}
        .score-D {{ color: #e67e22; font-weight: bold; }}
        .score-E {{ color: #e74c3c; font-weight: bold; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""

    HTML(string=full_html).write_pdf(str(output_path))


_FALLBACK_TEMPLATE = """# Rapport d'audit IA — {{ audit_name }}

**Date** : {{ date }}

---

## 1. Synthèse exécutive

Cet audit a été réalisé selon la méthodologie d'audit LLM v1.0.

{% if fairness_score %}
### Score de fairness : {{ fairness_score.score | round(1) }}/100 (Grade {{ fairness_score.grade }})
{% endif %}

{% if redteam_score %}
### Score de red-teaming : {{ redteam_score.score }}/100 (Grade {{ redteam_score.grade }})
- Tests exécutés : {{ redteam_score.total_tests }}
- Vulnérabilités détectées : {{ redteam_score.vulnerabilities_found }}
- Vulnérabilités critiques : {{ redteam_score.critical_vulns }}
{% endif %}

{% if robustness_score %}
### Score de robustesse : {{ robustness_score | round(1) }}/100 (Grade {{ robustness_grade }})
{% endif %}

---

## 2. Résultats détaillés

{% for step_key, step_data in results.items() %}
### {{ step_key }}

{% if step_data %}
{% for key, value in step_data.items() %}
- **{{ key }}** : {{ value }}
{% endfor %}
{% endif %}

{% endfor %}

---

*Rapport généré automatiquement par la méthodologie d'audit LLM v1.0*
*Auteur : Hanen Mizouni — IA au féminin*
"""


def main():
    parser = argparse.ArgumentParser(description="Génération du rapport d'audit IA")
    parser.add_argument("--audit-name", required=True, help="Nom de l'audit")
    parser.add_argument(
        "--format", default="md", choices=["md", "pdf"],
        help="Format de sortie (md ou pdf)"
    )
    parser.add_argument(
        "--output-dir", default=None,
        help="Dossier de sortie (défaut: output/<audit-name>/)"
    )
    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent
    output_dir = Path(args.output_dir) if args.output_dir else base_dir / f"output/{args.audit_name}"
    template_dir = base_dir / "templates"

    if not output_dir.exists():
        print(f"ERREUR : dossier {output_dir} introuvable.")
        print("Exécutez d'abord les notebooks pour générer les résultats.")
        sys.exit(1)

    print(f"Chargement des résultats depuis {output_dir}...")
    results = load_results(output_dir)

    if not results:
        print("AVERTISSEMENT : aucun fichier de résultats trouvé.")

    print(f"Résultats chargés : {list(results.keys())}")

    # Génération Markdown
    md_content = render_markdown(results, args.audit_name, template_dir)
    md_path = output_dir / f"rapport_{args.audit_name}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Rapport Markdown généré : {md_path}")

    # Génération PDF si demandé
    if args.format == "pdf":
        pdf_path = output_dir / f"rapport_{args.audit_name}.pdf"
        print("Génération du PDF...")
        export_pdf(md_content, pdf_path)
        print(f"Rapport PDF généré : {pdf_path}")

    print("\nRapport généré avec succès.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
