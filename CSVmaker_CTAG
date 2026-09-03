import Metadata_access_token as mdat
import csv
import json
import sys
import os
from time import sleep

# 🛠️ User Input
ctag = input("Enter the ctag you want to query (e.g., DWL_WIRE): ").strip()

# 🔥 Output CSV and Tracking Files
output_csv = f"ukndr_files_with_ctag_{ctag}.csv"
queried_files_txt = "queried_files.txt"
queried_projects_txt = "queried_projects.txt"
last_incomplete_project_txt = "last_incomplete_project.txt"

# ✅ Initialize session
session = mdat.requests.Session()

# 📊 CSV field labels
labels = ["File Name", "Project ID", "File Size (MB)", "File ID", "ctag"]
numfiles = 0
totalsize = 0
batch_limit = 20000  # Stop after querying 20k files

# 💾 Load previously queried project and file IDs
queried_projects = set()
queried_files = set()

if os.path.exists(queried_projects_txt):
    with open(queried_projects_txt, "r") as f:
        queried_projects.update(line.strip() for line in f)

if os.path.exists(queried_files_txt):
    with open(queried_files_txt, "r") as f:
        queried_files.update(line.strip() for line in f)

# 🔥 Check for an incomplete project
last_incomplete_project = None
if os.path.exists(last_incomplete_project_txt):
    with open(last_incomplete_project_txt, "r") as f:
        last_incomplete_project = f.read().strip()

# 🚀 Auto-detect write mode ("a" for append, "w" for new file)
write_mode = "a" if os.path.exists(output_csv) else "w"

# 💾 Open CSV file in append mode
with open(output_csv, write_mode, newline='') as csvfile:
    woutfile = csv.DictWriter(csvfile, fieldnames=labels, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    # Write header only if creating a new file
    if write_mode == "w":
        woutfile.writeheader()

    # 1️⃣ **Step 1: Handle Incomplete Project First**
    if last_incomplete_project and last_incomplete_project not in queried_projects:
        print(f"\n🔍 Resuming from incomplete project: {last_incomplete_project}")
        project_ids = [last_incomplete_project]
    else:
        print("\n🔍 Querying for new projects with the desired ctag...")
        project_ids = []

        next_link = (
            f"https://graph.microsoft.com/v1.0/sites/{mdat.Values.Site_ID}/lists/{mdat.Values.Completeness_well}/items"
            f"?expand=fields(select=pid,released)&$search=\"{ctag}\"&$top=500"
        )

        # 🌀 Loop through all pages of results to get Project IDs
        while next_link:
            response = session.get(
                next_link,
                headers={
                    "Authorization": f"Bearer {mdat.access_token}",
                    "Content-Type": "application/json",
                    "Prefer": "HonorNonIndexedQueriesWarningMayFailRandomly"
                }
            )

            if response.status_code == 200:
                data = response.json()

                for project in data.get("value", []):
                    project_id = project["fields"].get("pid")
                    if project_id and project_id not in queried_projects:
                        project_ids.append(project_id)

                # Pagination
                next_link = data.get("@odata.nextLink")
                sleep(0.2)

            else:
                print(f"❌ Error fetching projects. HTTP Code: {response.status_code}")
                print(response.text)
                sys.exit("Exiting due to error.")

    print(f"✅ Found {len(project_ids)} new projects with the ctag '{ctag}'.")

    # 2️⃣ **Step 2: Query Files in Each Project**
    print("\n📥 Fetching files from each project...")

    for project_id in project_ids:
        print(f"\n🔍 Querying for files in project: {project_id}")

        # Query for files in each project
        next_file_link = (
            f"https://graph.microsoft.com/v1.0/sites/{mdat.Values.Site_ID}/lists/{mdat.Values.File_ID_Metadata}/items"
            f"?expand=fields(select=pid,fid,fnam,ctag,size)&$filter=fields/pid eq '{project_id}'"
        )

        while next_file_link:
            file_response = session.get(
                next_file_link,
                headers={
                    "Authorization": f"Bearer {mdat.access_token}",
                    "Content-Type": "application/json",
                    "Prefer": "HonorNonIndexedQueriesWarningMayFailRandomly"
                }
            )

            if file_response.status_code == 200:
                file_data = file_response.json()

                # Loop through all files
                for file in file_data.get("value", []):
                    file_id = file["fields"].get("fid", "N/A")

                    # Skip previously queried files
                    if file_id in queried_files:
                        continue

                    file_ctags = file["fields"].get("ctag", [])
                    
                    if ctag in file_ctags:
                        numfiles += 1
                        size_mb = float(file["fields"].get("size", 0)) / 1048576.0
                        totalsize += size_mb

                        # Write matching files to CSV
                        woutfile.writerow({
                            "File Name": file["fields"].get("fnam", "N/A"),
                            "Project ID": file["fields"].get("pid", "N/A"),
                            "File Size (MB)": f"{size_mb:.2f}",
                            "File ID": file_id,
                            "ctag": ', '.join(file_ctags)
                        })

                        csvfile.flush()

                        # Add the file ID to the queried list
                        queried_files.add(file_id)

                        # Stop querying after batch limit is reached
                        if numfiles >= batch_limit:
                            print(f"\n🔹 Reached the batch limit of {batch_limit} files. Stopping execution.")
                            # Save the current project ID as the last incomplete project
                            with open(last_incomplete_project_txt, "w") as f:
                                f.write(project_id)
                            break

                # Pagination
                next_file_link = file_data.get("@odata.nextLink")
                sleep(0.1)

            else:
                print(f"❌ Error fetching files for project {project_id}. HTTP Code: {file_response.status_code}")
                print(file_response.text)
                break

        # ✅ Mark the project as fully processed
        queried_projects.add(project_id)

        # If the project was incomplete but now fully processed, clear the incomplete project file
        if project_id == last_incomplete_project:
            if os.path.exists(last_incomplete_project_txt):
                os.remove(last_incomplete_project_txt)

# ✅ Save the queried project and file IDs
with open(queried_projects_txt, "w") as f:
    for project_id in queried_projects:
        f.write(f"{project_id}\n")

with open(queried_files_txt, "w") as f:
    for file_id in queried_files:
        f.write(f"{file_id}\n")

# ✅ Display summary
print(f"\n✅ Output CSV file: {output_csv}")
print(f"📊 Total number of new files with ctag '{ctag}': {numfiles}")
print(f"💾 Total file size: {totalsize / 1024:.2f} GB")
