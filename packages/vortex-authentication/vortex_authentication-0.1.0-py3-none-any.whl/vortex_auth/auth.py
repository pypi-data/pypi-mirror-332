import requests

class VortexAuth:
    def __init__(self, base_url="https://www.vortex.best/api/license/verify"):
        self.base_url = base_url

    def login(self, license_key, ip, hwid):
        """Attempts to authenticate a user via Vortex API."""
        url = f"{self.base_url}?license={license_key}"
        payload = {
            "ip": ip, 
            "hwid": hwid
        }

        try:
            response = requests.post(url, data=payload, timeout=5)
            response.raise_for_status()
            result = response.json()

            if not result.get("success") or not result.get("valid") or result.get("user_id") is None:
                return {"status": "failed", "message": "Invalid credentials or missing user ID."}
            if not result.get("hwid_match"):
                return {"status": "failed", "message": "HWID mismatch."}
            if not result.get("ip_match"):
                return {"status": "failed", "message": "IP mismatch."}

            return {**result, "status": "success", "message": result.get("message", "Login successful")}

        except requests.exceptions.Timeout:
            return {"status": "error", "message": "Request timed out."}
        except requests.exceptions.HTTPError as e:
            return {"status": "error", "message": f"HTTP error: {e}"}
        except requests.exceptions.ConnectionError:
            return {"status": "error", "message": "Network connection error."}
        except Exception as e:
            return {"status": "error", "message": f"Unexpected error: {str(e)}"}
# Example usage
if __name__ == "__main__":
    auth = VortexAuth()
    login_response = auth.login("VORTEX-VH9F-HKM6-FW1K", "123", "321")
    print(login_response)