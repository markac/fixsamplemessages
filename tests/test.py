from markdown.test_tools import TestCase
from markdown_fixsamplemessages.fixsamplemessages import FixSampleMessageMarkdownExtension

class TestDDMarkdown(TestCase):
    default_kwargs = {'extensions': ['fixsamplemessages']}

    def test_fix_render(self):
        self.assertMarkdownRenders(
            self.dedent(
                """
                ::fix-sent-sample AE tests/data/AE.txt
                """
            ),
            self.dedent(
                """
                *FIX*: `AE`
                """
            )
        )
