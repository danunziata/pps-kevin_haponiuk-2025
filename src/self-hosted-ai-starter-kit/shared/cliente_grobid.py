from grobid_client.grobid_client import GrobidClient
import os

if __name__ == "__main__":
    # Calcula la ruta absoluta de config.json en la misma carpeta que este script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.json")
    input_dir = os.path.join(script_dir, "input_papers")
    output_dir = os.path.join(script_dir, "output_papers")

    client = GrobidClient(config_path=config_path)
    client.process(
        "processFulltextDocument",
        input_dir,
        output=output_dir,
        consolidate_citations=False,
        tei_coordinates=False,
        force=True
    )