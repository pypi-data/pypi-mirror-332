import base64
import os
from http import HTTPStatus

import requests
from mistralai import Mistral, models


class MistralHelper:
    def __init__(self,
                 api_key: str):
        self.api_key = api_key or os.getenv("MISTRAL_API_KEY")

        if not self.api_key:
            raise Exception("Please provide the api_key.")

        if not self.validate_api_key(self.api_key):
            raise Exception(f"Provided api_key is invalid. Input: api_key - {str(self.api_key)}")

    @staticmethod
    def validate_api_key(api_key: str) -> bool:
        try:
            if isinstance(api_key, str):
                headers = {"Authorization": f"Bearer {api_key}"}
                response = requests.get("https://api.mistral.ai/v1/models", headers=headers)
                if response.status_code == HTTPStatus.OK:
                    return True
                else:
                    return False
            raise Exception("Provided api_key is not a valid string."
                            f" Input: api_key - {str(api_key)}")
        except Exception:
            raise

    @staticmethod
    def encode_image(image_path):
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except FileNotFoundError:
            raise Exception(f"Error: The file {image_path} was not found.")
        except Exception:
            raise

    def extract_text_using_pdf_document_url(self,
                                            pdf_document_url: str,
                                            ocr_model_name: str = "mistral-ocr-latest",
                                            include_image_url: bool = True) -> models.OCRResponse:
        try:
            client = Mistral(api_key=self.api_key)
            ocr_response = client.ocr.process(
                model=ocr_model_name,
                document={
                    "type": "document_url",
                    "document_url": pdf_document_url
                },
                include_image_base64=include_image_url
            )
            return ocr_response
        except Exception as e:
            raise Exception(f"Error in processing ocr request - {str(e)}")

    def extract_text_using_pdf(self,
                               pdf_file_path: str,
                               ocr_model_name: str = "mistral-ocr-latest",
                               include_image_url: bool = True) -> models.OCRResponse:
        try:
            client = Mistral(api_key=self.api_key)

            # Upload PDF file to Mistral
            with open(pdf_file_path, "rb") as file:
                uploaded_pdf = client.files.upload(
                    file={
                        "file_name": pdf_file_path.split("/")[-1],
                        "content": file,
                    },
                    purpose="ocr"
                )

            ocr_response = client.ocr.process(
                model=ocr_model_name,
                document={
                    "type": "document_url",
                    "document_url": client.files.get_signed_url(file_id=uploaded_pdf.id).url,
                },
                include_image_base64=include_image_url
            )
            return ocr_response
        except Exception as e:
            raise Exception(f"Error in processing ocr request - {str(e)}")

    def extract_text_using_image_url(self,
                                     image_url: str,
                                     ocr_model_name: str = "mistral-ocr-latest") -> models.OCRResponse:
        try:
            client = Mistral(api_key=self.api_key)
            ocr_response = client.ocr.process(
                model=ocr_model_name,
                document={
                    "type": "image_url",
                    "image_url": image_url
                }
            )
            return ocr_response
        except Exception as e:
            raise Exception(f"Error in processing ocr request - {str(e)}")

    def extract_text_using_image_path(self,
                                      image_path: str,
                                      ocr_model_name: str = "mistral-ocr-latest") -> models.OCRResponse:
        try:
            client = Mistral(api_key=self.api_key)
            ocr_response = client.ocr.process(
                model=ocr_model_name,
                document={
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{self.encode_image(image_path)}"
                }
            )
            return ocr_response
        except Exception as e:
            raise Exception(f"Error in processing ocr request - {str(e)}")
