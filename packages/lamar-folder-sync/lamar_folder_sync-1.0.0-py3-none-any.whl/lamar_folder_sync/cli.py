import argparse
from .sync import replicate_folders

def main():
    parser = argparse.ArgumentParser(description="Replicate folders between source and destination in Lamar CMS.")
    
    parser.add_argument(
        "source_folder_id",
        type=str,
        help="The ID of the source folder."
    )
    parser.add_argument(
        "destination_folder_id",
        type=str,
        help="The ID of the destination parent folder."
    )

    args = parser.parse_args()

    replicate_folders(args.source_folder_id, args.destination_folder_id)

if __name__ == "__main__":
    main()