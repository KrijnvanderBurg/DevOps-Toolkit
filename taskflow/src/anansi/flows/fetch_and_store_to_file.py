import json
import logging
import requests
from datetime import datetime
from taskflow import task
from taskflow import engines
from taskflow.patterns import linear_flow as lf
import os


# Configure logging
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


logger = setup_logging()


# Task 1: Create the output file with datetime in the filename
class CreateOutputFileTask(task.Task):
    def __init__(self):
        super(CreateOutputFileTask, self).__init__(provides="output_file")

    def execute(self):
        datetime_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"aggregated_prices_{datetime_str}.jsonl"
        if os.path.exists(output_file):
            logger.warning(
                f"Output file {output_file} already exists. It will be overwritten.")
        else:
            logger.info(f"Creating output file: {output_file}")
        open(output_file, 'w').close()  # Create or clear the file
        return output_file


# Task 2: Fetch the list of IDs
class FetchIDsTask(task.Task):
    def __init__(self):
        super(FetchIDsTask, self).__init__(provides="ids")

    def execute(self):
        url = "https://api.guildwars2.com/v2/commerce/prices"
        logger.info("Fetching IDs from the API...")
        response = requests.get(url)
        response.raise_for_status()
        ids = response.json()
        logger.info(f"Fetched {len(ids)} IDs.")
        return ids


# Task 3: Group the IDs into batches of 200
class GroupIDsTask(task.Task):
    def __init__(self):
        super(GroupIDsTask, self).__init__(
            requires=["ids"], provides="grouped_ids")

    def execute(self, ids):
        batch_size = 200
        grouped_ids = [ids[i:i + batch_size]
                       for i in range(0, len(ids), batch_size)]
        logger.info(f"Grouped {len(ids)} IDs into {len(grouped_ids)} batches.")
        return grouped_ids


# Task 4: Fetch and process each batch, then append to file
class FetchAndProcessBatchTask(task.Task):
    def __init__(self):
        super(FetchAndProcessBatchTask, self).__init__(
            requires=["grouped_ids", "output_file"])

    def execute(self, grouped_ids, output_file):
        url = "https://api.guildwars2.com/v2/commerce/prices"
        for idx, batch in enumerate(grouped_ids):
            ids_query = ",".join(map(str, batch))
            batch_url = f"{url}?ids={ids_query}"
            logger.info(
                f"Fetching batch {idx + 1}/{len(grouped_ids)}: {batch_url}")
            try:
                response = requests.get(batch_url)
                response.raise_for_status()
                batch_result = response.json()
                logger.info(
                    f"Batch {idx + 1}/{len(grouped_ids)} fetched successfully.")
                self.append_to_file(batch_result, output_file)
            except requests.RequestException as e:
                logger.error(f"Failed to fetch batch {idx + 1}: {e}")
                continue

    def append_to_file(self, batch_result, output_file):
        logger.info(f"Appending batch result to {output_file}...")
        try:
            with open(output_file, "a+") as f:
                f.write(json.dumps(batch_result) + "\n")
            logger.info(f"Batch result appended to {output_file}.")
        except IOError as e:
            logger.error(
                f"Failed to append batch result to {output_file}: {e}")


# Define the workflow
def create_workflow():
    workflow = lf.Flow("Fetch, Process, and Store Incrementally")

    # Add tasks to the workflow
    workflow.add(
        CreateOutputFileTask(),  # Create output file
        FetchIDsTask(),  # Fetch IDs
        GroupIDsTask(),  # Group IDs into batches
        FetchAndProcessBatchTask(),  # Fetch each batch and append to file
    )

    return workflow


if __name__ == "__main__":
    # Create and run the workflow
    logger.info("Starting the workflow...")
    flow = create_workflow()
    engine = engines.load(flow)
    engine.run()
    logger.info("Workflow complete.")
