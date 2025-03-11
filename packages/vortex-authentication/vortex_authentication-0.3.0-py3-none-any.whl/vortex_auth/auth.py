import requests
import uuid
import platform
import subprocess

class VortexAuth:
    def __init__(self, base_url="https://www.vortex.best/api/license/verify"):
        self.base_url = base_url

    def get_hwid(self):
        """Generate or retrieve a unique HWID for a Windows system."""
        if platform.system() == "Windows":
            hwid = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.getnode())))

            try:
                serial_number = subprocess.check_output("wmic diskdrive get serialnumber", shell=True).decode().split('\n')[1].strip()
                hwid = f"{hwid}-{serial_number}"
            except Exception as e:
                print(f"Error getting serial number: {e}")

        else:
            hwid = str(uuid.uuid4())

        return hwid

    def get_ip(self):
        """Fetch the public IP address of the system."""
        try:
            response = requests.get("https://api.ipify.org?format=json", timeout=5)
            response.raise_for_status()
            ip = response.json().get("ip")
            return ip
        except requests.exceptions.RequestException as e:
            print(f"Error fetching IP: {e}")
            return None

    def login(self, license_key, ip=None, hwid=None):
        """Attempts to authenticate a user via Vortex API."""
        if not license_key:
            return {"status": "error", "message": "Missing required parameters: license_key."}

        if not hwid:
            hwid = self.get_hwid()
        
        if not ip:
            ip = self.get_ip()

        url = f"{self.base_url}?license={license_key}"
        data = {
            "ip": ip, 
            "hwid": hwid
        }

        try:
            response = requests.post(url, data=data, timeout=5)
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