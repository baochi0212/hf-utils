from huggingface_hub import snapshot_download
import sys
# Define the model or dataset repository
repo_id = sys.argv[1]  # Replace with the actual repository ID
local_dir = f"./checkpoint_spp/{repo_id.split('/')[1]}"

# Download the snapshot
snapshot_download(repo_id, local_dir=local_dir, local_dir_use_symlinks=False)

print(f"Snapshot downloaded to {local_dir}")

