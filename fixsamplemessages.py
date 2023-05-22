from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
import logging
import re

logger = logging.getLogger('MARKDOWN')

class FixSampleMessagesMarkdownBlockProcessor(BlockProcessor):
  RE = re.compile(r'''
    (?::fix-sent-sample)\s*                     # ::fix
    (?P<id>[a-zA-Z0-9-]+)\s*                    # FIX messageType (tag 35)
    (?P<path>[^\s]*)\s*                         # Path to FIX data dictionary
    ''', re.VERBOSE)

  def test(self, parent, block):
    return self.RE.search(block)

  def run(self, parent, blocks):
    block = blocks.pop(0)

    # Parse configuration params
    m = self.RE.search(block)
    id = m.group('id')
    path = m.group('path')

    with open(path, 'r') as f:
        content = f.read()

        extractSampleRegEx = re.compile(
          r'#\s*fix-sent-sample:\s*%s\s*\n.*?sends a \'(?P<messageType>[^\']*)\' message\s*\n.*?"""\n(?P<messageContent>.*?)"""' % id,
          re.MULTILINE | re.DOTALL)
        print(extractSampleRegEx)
        content_match = extractSampleRegEx.search(content)
        self.parser.parseChunk(parent, content_match.group('messageContent'))

class FixSampleMessageMarkdownExtension(Extension):
  """ Extract FIX sample messages from the Hydra cucumber tests and insert them into a markdown document """

  def extendMarkdown(self, md):
    """ Add FixSampleMessageMarkdownExtension to Markdown instance. """
    blockprocessor = FixSampleMessagesMarkdownBlockProcessor(md.parser)
    blockprocessor.config = self.getConfigs()
    md.parser.blockprocessors.add('fixsamplemessages', blockprocessor, '>code')


def makeExtension(**kwargs):  # pragma: no cover
  return FixSampleMessageMarkdownExtension(**kwargs)
