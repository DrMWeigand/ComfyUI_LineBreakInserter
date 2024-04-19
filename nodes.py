class LineBreakInserter:
    """
    This custom node inserts line breaks into a string based on a specified number of words per line.
    It is designed to improve readability of long text strings by breaking them into manageable lines.

    Attributes:
        INPUT_TYPES (dict): Specifies the input types and properties:
            - input_string (STRING): The string to process.
            - words_per_line (INT, default=10): The number of words after which a line break is inserted.
            
        RETURN_TYPES (tuple): Specifies the return type:
            - (STRING): The processed string with line breaks.
        
        RETURN_NAMES (tuple): Names of the return fields:
            - ("output_string"): Name of the output string with line breaks.
        
        FUNCTION (str): The function that processes the input.
        
        CATEGORY (str): The category under which this node falls in the ComfyUI menu.

    Methods:
        process(input_string, words_per_line):
            Processes the input string to insert line breaks after the specified number of words.
            
            Args:
                input_string (str): The string to be processed.
                words_per_line (int): Number of words after which to insert a line break.
                
            Returns:
                output_string (str): The string with inserted line breaks.
    """
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "input_string": ("STRING",{
                    "multiline": True,
                    "default": "Your text here...",
                    }),
            "words_per_line": ("INT", {"default": 10}),
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
