class LineBreakInserter:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "input_string": ("STRING", ),
            "words_per_line": ("INT", {"default": 10}),  # Default to 10 words per line
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_string",)
    FUNCTION = "process"

    CATEGORY = "Text Formatting"

    def process(self, input_string, words_per_line):
        words = input_string.split()
        lines = [' '.join(words[i:i + words_per_line]) for i in range(0, len(words), words_per_line)]
        output_string = '\n'.join(lines)
        return (output_string,)

NODE_CLASS_MAPPINGS = {
    "LineBreakInserter": LineBreakInserter,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "LineBreakInserter": "Line Break Inserter",
}
