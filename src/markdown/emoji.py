from src.markdown_converter import MarkdownConverter


@MarkdownConverter.Register
class MarkdownEmoji():
    # config as you like. http://www.webpagefx.com/tools/emoji-cheat-sheet/
    config = {
        '8-)': 'sunglasses',
        '8-O': 'flushed',
        ':-(': 'worried',
        ':-)': 'simple_smile',
        '=)': 'simple_smile',
        ':-/': 'confused',
        ':-\\': 'confused',
        ':-?': 'sweat',
        ':-D': 'laughing',
        ':-P': 'stuck_out_tongue',
        ':-O': 'open_mouth',
        ':-X': 'grimacing',
        ':-|': 'expressionless',
        ';-)': 'wink',
        '^_^': 'smile',
        ':?:': 'question',
        ':!:': 'exclamation',
        'LOL': 'laughing',
    }

    def convert(self, text):
        result = text
        for key, value in MarkdownEmoji.config.items():
            result = result.replace(key, ':' + value + ':')
        return result