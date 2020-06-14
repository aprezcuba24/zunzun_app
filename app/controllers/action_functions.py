from main import router


@router.get("/")
def index():
    """Return a friendly index."""
    return f"Index"


@router.post("/")
def register():
    return "Register"
