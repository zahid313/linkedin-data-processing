import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrap_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    # scrap information from linkedin profiles
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/zahid313/2675606e734f8f0c4d69b94ef26de9d6/raw/124dfcb922700f51eb60b814c52ebe13e6c8a11f/zahid-ali.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        headers = {"Authorization": "Bearer " + os.environ.get("PROXYCURL_API_KEY")}
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        params = {
            "linkedin_profile_url": linkedin_profile_url,
            "extra": "include",
            "personal_contact_number": "include",
            "personal_email": "include",
            "inferred_salary": "include",
            "skills": "include",
        }
        response = requests.get(
            api_endpoint, params=params, headers=headers, timeout=10
        )

    data = response.json()
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    print(
        scrap_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/zahid-ali-1735049/",
            mock=True
        )
    )
