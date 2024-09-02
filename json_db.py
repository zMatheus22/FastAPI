from releases import Releases
from pydantic import BaseModel # type: ignore
import json

class JsonDB(BaseModel):
    path: str

    def read_Json(self):
        file = open(self.path, "r", encoding="utf-8")
        data = json.loads(file.read())
        file.close()

        return data


    def insert(self, release: Releases):
        data = self.read_Json()
        data.append(release.dict())

        file = open(self.path, "w", encoding="utf-8")
        file.write(json.dumps(data, ensure_ascii=False))
        file.close()
