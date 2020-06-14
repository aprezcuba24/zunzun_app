from zunzun import Response
from main import router


class ActionClass:
    @router.get("/class/<name>")
    def hello(self, name):
        return Response(
            f"Hello {name}"
        )
