import __main__

class Gifloader_Placeholder:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return { }

    RETURN_TYPES = ()
    FUNCTION = "gifloadrr"

    CATEGORY = "marduk191/GifLoader"

    def placeholder(self):
        return ()
    
NODE_CLASS_MAPPINGS = {
    "Gifloader_Placeholder": Gifloader_Placeholder
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Gifloader_Placeholder": "marduk191's Gifloader",
}

WEB_DIRECTORY = "./web"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']