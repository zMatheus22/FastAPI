from lancamentos import Lancamento
from pydantic import BaseModel # type: ignore
import json

class JsonDB(BaseModel):
    path: str

    def read_Json(self):
        file = open(self.path, "r", encoding="utf-8")
        data = json.loads(file.read())
        file.close()

        return data


    def insert(self, lancamento: Lancamento):
        data = self.read_Json()
        data.append(lancamento.dict())

        file = open(self.path, "w", encoding="utf-8")
        file.write(json.dumps(data, ensure_ascii=False))
        file.close()
