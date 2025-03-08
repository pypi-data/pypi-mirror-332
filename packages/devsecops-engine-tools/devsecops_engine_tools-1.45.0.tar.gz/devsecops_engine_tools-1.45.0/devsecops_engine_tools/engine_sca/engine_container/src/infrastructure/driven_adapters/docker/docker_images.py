from datetime import datetime
from devsecops_engine_tools.engine_sca.engine_container.src.domain.model.gateways.images_gateway import (
    ImagesGateway,
)
import docker

from devsecops_engine_tools.engine_utilities.utils.logger_info import MyLogger
from devsecops_engine_tools.engine_utilities import settings

logger = MyLogger.__call__(**settings.SETTING_LOGGER).get_logger()


class DockerImages(ImagesGateway):
    def list_images(self, image_to_scan):
        try:
            client = docker.from_env()
            images = client.images.list()

            matching_image = None
            for image in images:
                if any(image_to_scan in tag for tag in image.tags):
                    matching_image = image
                    break

            if matching_image:
                print("ID matching image:", matching_image.id)
                print("Tag matching image:", matching_image.tags)
                print("Created date matching image:", matching_image.attrs["Created"])
                return matching_image

        except Exception as e:
            logger.error(
                f"Error listing images, docker must be running and added to PATH: {e}"
            )

    def get_base_image(self, matching_image):
        try:
            image_details = self.get_image_details(matching_image.id)
            if not image_details:
                return None

            labels = image_details.get("Config", {}).get("Labels", {})
            return self.extract_base_image_from_labels(labels, matching_image)
        except Exception as e:
            logger.warning(f"Error obtaining base image: {e}")
            return None

    def validate_base_image_date(self, matching_image, referenced_date):
        if matching_image is None or matching_image.id is None:
            logger.error("Error: matching_image ID is None")
            return False
        image_details = self.get_image_details(matching_image.id)
        if not image_details:
            return False

        labels = image_details.get("Config", {}).get("Labels", {})
        baseline_date = labels.get("x86.baseline.date")

        if baseline_date:
            date_image = self.parse_date(baseline_date)
        else:
            base_image = self.extract_base_image_from_labels(labels)
            date_image = self.extract_date_from_image(base_image)

        return self.validate_date(date_image, referenced_date)

    def get_image_details(self, image_id):
        try:
            client = docker.from_env()
            return client.api.inspect_image(image_id)
        except Exception as e:
            logger.error(f"Error obtaining image details for '{image_id}': {e}")
            return None

    def extract_base_image_from_labels(self, labels, matching_image=None):
        try:
            source_image = labels.get("x86.image.name") or labels.get(
                "image.base.ref.name"
            )
            if not source_image:
                source_image = labels.get("source_images") or labels.get("source-image")

            if source_image and matching_image:
                logger.info(f"Base image for '{matching_image}' found: {source_image}")
            elif matching_image:
                logger.warning(f"Base image not found for '{matching_image}'.")

            return source_image
        except Exception as e:
            logger.error(f"Error extracting base image from labels: {e}")
            return None

    def extract_date_from_image(self, image_name):
        if not image_name:
            return None
        try:
            date = image_name.split("_")[-1]
            return self.parse_date(date)
        except Exception as e:
            logger.error(f"Error extracting date from image name '{image_name}': {e}")
            return None

    def parse_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%Y%m%d")
        except ValueError:
            logger.error(f"Invalid date format: {date_str}")
            return None

    def validate_date(self, date, referenced_date):
        if not date:
            raise ValueError("Cannot validate date: Invalid or missing date.")

        reference_date = self.parse_date(referenced_date)
        if not reference_date:
            raise ValueError("Cannot validate date: Referenced date is invalid.")

        if date < reference_date:
            raise ValueError(
                f"Compliance issue: the source base image date ({date.strftime('%Y-%m-%d')}) is older than the referenced date ({reference_date.strftime('%Y-%m-%d')})."
            )
        return True
