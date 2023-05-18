import markdown
from fixsamplemessages import FixSampleMessageMarkdownExtension

markdown.markdown('::fix AE', extensions=[FixSampleMessageMarkdownExtension()])
