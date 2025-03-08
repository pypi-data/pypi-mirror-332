import requests

class NeuroSlidesClient:
    """
    A simple client to communicate with the NeuroSlides API.

    Example usage:
        client = NeuroSlidesClient(
            api_key="your_api_key_here"
        )
        pptx_content = client.generate_slide(
            title="Building Employee Wellness Programs",
            lesson="Employee wellness programs are essential for attracting and retaining talent and boosting productivity.",
            points=[
                "Effective wellness initiatives address physical, mental, emotional, and financial well-being",
                "Technology enhances the accessibility and personalization of wellness programs, promoting engagement and community."
            ],
            slide_number=9
        )
        with open("output.pptx", "wb") as f:
            f.write(pptx_content)
    """

    def __init__(self, api_key,pexels_key=None,base_url="https://testing-wasilislam.pythonanywhere.com/api/v1/neuroslides"):
        self.base_url = base_url
        self.api_key = api_key
        self.pexels_key = pexels_key

    def generate_slide(self, title, lesson, points, slide_number=None,output_path=None):
        """
        Sends a request to generate a presentation slide.

        :param title: Title for the slide.
        :param lesson: Lesson content for the slide.
        :param points: A list or comma-separated string of key points.
        :param slide_number: Optional slide number.
        :return: The binary content of the generated PPTX file.
        :raises Exception: If the API returns an error.
        """
        url = f"{self.base_url}/one-slide-from-TLP"
        headers = {
            "Content-Type": "application/json",
            "X-API-KEY": self.api_key,
            "X-PEXELS-KEY": self.pexels_key
        }
        data = {
            "title": title,
            "lesson": lesson,
            "points": points
        }
        if slide_number is not None:
            data["slide_number"] = slide_number

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            if output_path:
                with open(output_path, "wb") as f:
                    f.write(response.content)

            return response.content
        else:
            try:
                error_data = response.json()
            except Exception:
                error_data = response.text
            raise Exception(f"Error generating slide: {response.status_code} - {error_data}")