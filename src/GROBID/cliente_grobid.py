from grobid_client.grobid_client import GrobidClient

if __name__ == "__main__":
    client = GrobidClient(config_path="./config.json")
    client.process("processFulltextDocument", "input_papers", output="output_papers/", consolidate_citations=False, tei_coordinates=False, force=True)