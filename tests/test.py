import markdown
from markdown_fixsamplemessages.fixsamplemessages import FixSampleMessageMarkdownExtension

markdown.markdown('::fix AE', extensions=[FixSampleMessageMarkdownExtension()])
