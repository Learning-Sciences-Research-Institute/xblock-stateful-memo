import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.exceptions import JsonHandlerError

class StatefulMemoXBlock(XBlock):
    memo_text = String(
        default="", scope=Scope.preferences,
        help="String of memo text",
    )

    def resource_string(self, path):
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        html = self.resource_string("static/html/statefulmemo.html")
        frag = Fragment(html.format(self=self))
        frag.add_css_url("https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css")
        frag.add_javascript_url("https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js")
        frag.add_javascript_url("https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js")
        frag.add_css(self.resource_string("static/css/statefulmemo.css"))
        frag.add_javascript(self.resource_string("static/js/src/statefulmemo.js"))
        frag.initialize_js('StatefulMemoXBlock')
        return frag

    @XBlock.json_handler
    def update_memo_text(self, data, suffix=''):
        try:
            self.memo_text = data['memo_text']
            self.runtime.publish(self, "write_memo", {"memo_text": self.memo_text})
            return {"memo_text": self.memo_text}
        except KeyError:
            raise JsonHandlerError(400, "Missing memo_text parameter")
        
    @staticmethod
    def workbench_scenarios():
        return [
            ("StatefulMemoXBlock", "<statefulmemo/>"),
            ("StatefulMemoXBlock2", "<statefulmemo/>"),
            ("Multiple StatefulMemoXBlock with different initial values",
             """<vertical_demo>
                <statefulmemo/>
                <statefulmemo/>
                <statefulmemo/>
                </vertical_demo>
             """)
        ]