"""
A device that allows us to implement operation on a single qudit. The backend is a remote simulator.
"""

import requests, json, time
from pennylane import DeviceError, QubitDevice

from .kq_device import KoreaQuantumDevice


class KoreaQuantumHardware(KoreaQuantumDevice):
    """
    The base class for all devices that call to an external server.
    """

    name = "Korea Quantum Hardware"
    short_name = "kq.hardware"
    pennylane_requires = ">=0.16.0"
    version = "0.0.1"
    author = "Inho Jeon"
    accessToken = None
    resourceId = "18208724-e51f-4bab-b635-298ea07070b2"
    cloud_url = "https://qc.kisti.re.kr"
    operations = {"PauliX", "PauliY", "PauliZ", "RX", "CNOT", "RY", "RZ"}

    def __init__(
        self, wires=4, shots=1024, pollingTime=1, accessKeyId=None, secretAccessKey=None
    ):
        super().__init__(wires=wires, shots=shots)
        self.accessKeyId = accessKeyId
        self.secretAccessKey = secretAccessKey
        self.pollingTime = pollingTime
        # self.hardware_options = hardware_options or "kqEmulator"

    def apply(self, operations, **kwargs):
        self.run(self._circuit)

    def _get_token(self):
        print("\r[info] get KQ Cloud Token", end="")
        api_url = f"{self.cloud_url}/oauth/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "apikey",
            "accessKeyId": self.accessKeyId,
            "secretAccessKey": self.secretAccessKey,
        }
        requestData = requests.post(api_url, data=data, headers=headers, verify=False)
        if requestData.status_code == 200:
            jsondata = requestData.json()
            self.accessToken = jsondata.get("accessToken")
            return True
        else:
            raise DeviceError(
                f"/oauth/token error. req code : {requestData.status_code}"
            )

    def _job_submit(self, circuit):
        print("\r[info] job submit   ", end="")
        URL = f"{self.cloud_url}/v2/jobs"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.accessToken}",
        }
        data = {
            "resource": {"id": self.resourceId},
            "code": circuit.to_openqasm(wires=sorted(circuit.wires)),
            "shot": self.shots,
            "name": "test job",
            "type": "QASM",
        }
        res = requests.post(URL, data=json.dumps(data), headers=headers, verify=False)

        if res.status_code == 201:
            return res.json().get("id")
        else:
            raise DeviceError(f"Job sumbit error. req code : {res.status_code}")

    def _check_job_status(self, jobId):
        timeout = 6000
        timeout_start = time.time()
        # wait_string = ""

        iter = 0
        while time.time() < timeout_start + timeout:
            iter = iter + 1
            time.sleep(self.pollingTime)
            URL = f"{self.cloud_url}/v2/jobs/{jobId}"
            headers = {"Authorization": f"Bearer {self.accessToken}"}
            res = requests.get(URL, headers=headers, verify=False)
            status = res.json().get("status")
            # wait_string = wait_string + "."
            # print(f"\r[info] job status : {status} {wait_string}", end="")

            loading = ["*", "|", "/", "-", "\\", "|", "/", "-", "\\"]
            print(f"\r[info] job status : {status} {loading[iter % 9]}", end="")

            if status == "SUCCESS":
                print(f"\r", " " * 40, end="")
                print(f"\r", end="")
                return res.json().get("result")
        raise DeviceError("Job timeout")

    def batch_execute(self, circuits):
        if not self.accessToken:
            self._get_token()

        res_results = []
        for circuit in circuits:
            jobUUID = self._job_submit(circuit)
            res_result = self._check_job_status(jobUUID)
            res_results.append(res_result)

        results = []
        for circuit, res_result in zip(circuits, res_results):
            # for circuit in circuits:
            self._samples = self._convert_counts_to_samples(
                res_result, circuit.num_wires
            )

            res = self.statistics(circuit)
            single_measurement = len(circuit.measurements) == 1
            res = res[0] if single_measurement else tuple(res)
            results.append(res)

        return results
